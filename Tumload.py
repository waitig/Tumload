# -*- coding: utf-8 -*-
# --------------------------------------
# Author:waitig.com
# Date:2016-04-16
# Desc:Tumblr下载器界面脚本
# --------------------------------------
import sys
import time, uuid
from TumloadUI import Ui_Dialog
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from TumblrModel import TumblrClass
from SplashScreen import SplashScreen
import pyqt_rc


# qtCreatorFile = "Tumload.ui"  # Enter file here.
# Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
# class ADThread(QThread):
#     def __init__(self,tc,parent=None):
#         super(ADThread,self).__init__(parent)
#         self.tc=tc

class WorkThread(QThread):
    def __int__(self, parent=None):
        super(WorkThread, self).__init__(parent)
        self.stoped = False
        self.type = None
        self.sourceUrl = None
        self.isSave = None
        self.tc = None

    def setParam(self, tc, type, sourceUrl, isSave,proxyHost,proxyPort,setProxy):
        self.mutex = QMutex()  # Locker
        self.tc = tc
        self.type = type
        self.sourceUrl = sourceUrl
        self.isSave = isSave
        self.proxyHost = proxyHost
        self.proxyPort = proxyPort
        self.setProxy = setProxy


    def run(self):
        with QMutexLocker(self.mutex):
            self.stoped = False
        self.tc.reset()
        self.tc.setUIClass(self)
        print self.setProxy
        if (self.setProxy == 1):
            self.tc.setProxy(self.proxyHost,self.proxyPort)
        self.tc.main(self.type, self.sourceUrl, self.isSave)
        self.emit(QtCore.SIGNAL('loadingEnd'))

    def log(self, value):
        self.emit(QtCore.SIGNAL("updateLog"), str(value))

    def setVideoNum(self, num):
        self.emit(QtCore.SIGNAL("setVideoNum"), str(num))

    def insertDownloadUrl(self, url):
        self.emit(QtCore.SIGNAL("insertDownloadUrl"), str(url))

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped = True


class TumloadClass(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        print 'tumload init'
        QtGui.QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
        self.isDebug = 1
        self.isVIP = 0
        self.fileName = ''
        self.indexUrl = ''
        self.sourceUrl = ''
        self.logFile = open('log.txt', 'w')
        self.uid = ''
        self.wk = None
        self.chkUrl = 'http://check.waitig.com/software/tumload.php'
        self.header = {}
        self.tc = TumblrClass(self)
        self.init()

    def init(self):
        self.readSettings()
        self.borseButton.clicked.connect(self.showDialog)
        self.startButton.clicked.connect(self.startLoad)
        self.stopButton.clicked.connect(self.stopLoad)
        self.urlEdit.textChanged.connect(self.setIndexUrl)
        self.setWindowIcon(QtGui.QIcon(':/favico.ico'))

        # self.connect(self.timer, QtCore.SIGNAL("updateresult"),self.updateResult)

        # -----------get uuid-------------------
        # self.uid = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'waitig.com'))
        # self.tc.set_uid(self.uid)
        settings = QSettings('tumloadSetting')
        self.uid = str(settings.value('uuid').toString())
        print self.uid
        if (self.uid == ''):
            self.uid = str(uuid.uuid1())
            settings.setValue('uuid', self.uid)
        self.tc.set_uid(self.uid)
        self.sn_line.setText(self.uid)
        self.check_ads()
        print 'tumload init end'

    def initThread(self, type, sourceUrl, isSave,proxyHost,proxyPort,setProxy):
        self.wk = None
        self.wk = WorkThread()
        self.wk.setParam(self.tc, type, sourceUrl, isSave ,proxyHost,proxyPort,setProxy)
        self.connect(self.wk, QtCore.SIGNAL("loadingEnd"), self.loadingEnd)
        self.connect(self.wk, QtCore.SIGNAL("updateLog"), self.log)
        self.connect(self.wk, QtCore.SIGNAL("setVideoNum"), self.setVideoNum)
        self.connect(self.wk, QtCore.SIGNAL("insertDownloadUrl"), self.insertDownloadUrl)

    def startThread(self):
        self.wk.start()

    def stopThread(self):
        self.wk.stop()
        self.disconnect(self.wk, QtCore.SIGNAL("updateLog"), self.log)
        self.disconnect(self.wk, QtCore.SIGNAL("setVideoNum"), self.setVideoNum)
        self.disconnect(self.wk, QtCore.SIGNAL("insertDownloadUrl"), self.insertDownloadUrl)

    def debug(self, log):
        if self.isDebug == 1:
            print log

    def getProxyText(self):
        self.proxyIps = str(self.proxyHost.text())
        self.proxyPorts = str(self.proxyPort.text())
        #setProxy = self.setProxy
        if(self.setProxy.isChecked()):
            self.setProxys=1
        else:
            self.setProxys=0

    def readSettings(self):
        settings = QSettings('tumloadSetting')
        self.fileName = str(settings.value('fileName').toString())
        self.indexUrl = str(settings.value('indexUrl').toString())
        self.proxyHosts = str(settings.value('proxyHost').toString())
        if(self.proxyHosts == ''):
            self.proxyHosts='http://127.0.0.1'
        self.proxyPorts = str(settings.value('proxyPort').toString())
        if(self.proxyPorts == ''):
            self.proxyPorts='1080'
        self.fileEdit.setText(self.fileName)
        self.urlEdit.setText(self.indexUrl)
        self.proxyHost.setText(self.proxyHosts)
        self.proxyPort.setText(self.proxyPorts)
        self.setProxy.setChecked(False)

    def writeSettings(self):
        settings = QSettings('tumloadSetting')
        settings.setValue('fileName', self.fileName)
        settings.setValue('indexUrl', self.indexUrl)
        settings.setValue('proxyHost',self.proxyHosts)
        settings.setValue('proxyPort',self.proxyPorts)
        if(self.setProxy.isChecked()):
            settings.setValue('setProxy','1')
        else:
            settings.setValue('setProxy','0')

    def showDialog(self):
        file_Name = QtGui.QFileDialog.getOpenFileName(self, 'Open file', self.fileName)
        if ('' != file_Name):
            self.fileName = file_Name
        self.fileEdit.setText(self.fileName)

    def setIndexUrl(self):
        self.indexUrl = self.urlEdit.text()

    def startLoad(self):
        isSave = self.comboBox.currentIndex()
        type = self.tabWidget.currentIndex()

        if (type == 0):
            self.sourceUrl = str(self.fileName)
        elif (type == 1):
            self.sourceUrl = str(self.indexUrl)
        self.log('Started to load:' + self.sourceUrl + '...')
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        # try:
        #    thread.start_new_thread(self.loadThread, (type, self.sourceUrl, isSave))
        # except:
        #    print "Error: unable to start thread"
        self.getProxyText()
        self.initThread(type, self.sourceUrl, isSave,self.proxyIps,self.proxyPorts,self.setProxys)
        self.startThread()

    def stopLoad(self):
        # self.threadAlive = 0
        # self.tc.exit()
        self.stopThread()
        self.loadingEnd()

    def loadingEnd(self):
        self.log('Loading End!')
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)

    def log(self, log):
        tm = time.strftime('%m-%d %H:%M:%S', time.localtime(time.time()))
        log = '[' + tm + ']:' + log
        self.logLabel.setText(log)
        self.logFile.write(log + '\n')
        self.logFile.flush()

    def setVideoNum(self, num):
        self.lcdNumber.display(num)

    def insertDownloadUrl(self, url):
        self.linkBrowser.append(url)
        self.linkBrowser.verticalScrollBar().setValue(self.linkBrowser.verticalScrollBar().maximum())

    def setAD1(self, text):
        self.Ad1.setText(text)

    def setAD2(self, text):
        self.Ad2.setText(text)

    def setAD3(self, text):
        self.Ad3.setText(text)

    def setTopUrl(self, url):
        self.webView.load(QtCore.QUrl(url))

    def setVIP(self, isVIP):
        self.isVIP = isVIP
        if (self.isVIP == 0):
            self.vipText.setText(
                u'您是【普通用户】 普通用户每次只能获取十个视频，<a href="http://www.waitig.com/tumload-vip.html" target="_blank">点此升级</a>！')
        else:
            self.vipText.setText(u'您是<span style=" color:#ff0000;">【VIP用户】</span> VIP用户使用无限制，感谢您的支持！')

    def check_ads(self):
        try:
            self.tc.check_ads(self.sourceUrl, 1)
        except BaseException, e:
            print(str(e))
            return

    def closeEvent(self, QCloseEvent):
        self.writeSettings()
        self.logFile.close()

    def __del__(self):
        self.writeSettings()
        self.logFile.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    # splash=QtGui.QSplashScreen(QtGui.QPixmap(':/tumload.png'))
    # splash.show()
    splash = SplashScreen()
    # splash.effective()
    splash.effect()
    # splash.effect_show()
    app.processEvents()
    window = TumloadClass()
    # splash.checkEnd()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())
