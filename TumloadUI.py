# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tumload.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.setEnabled(True)
        Dialog.resize(619, 467)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(619, 467))
        Dialog.setMaximumSize(QtCore.QSize(619, 467))
        Dialog.setSizeIncrement(QtCore.QSize(619, 467))
        Dialog.setBaseSize(QtCore.QSize(619, 467))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        Dialog.setFont(font)
        Dialog.setMouseTracking(False)
        Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Dialog.setAcceptDrops(True)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.webView = QtWebKit.QWebView(Dialog)
        self.webView.setGeometry(QtCore.QRect(0, 0, 611, 81))
        self.webView.setMaximumSize(QtCore.QSize(611, 81))
        self.webView.setAutoFillBackground(True)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 601, 71))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.fileEdit = QtGui.QLineEdit(self.tab)
        self.fileEdit.setGeometry(QtCore.QRect(70, 10, 421, 21))
        self.fileEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.fileEdit.setObjectName(_fromUtf8("fileEdit"))
        self.borseButton = QtGui.QPushButton(self.tab)
        self.borseButton.setGeometry(QtCore.QRect(500, 10, 81, 23))
        self.borseButton.setObjectName(_fromUtf8("borseButton"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.label_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.urlEdit = QtGui.QLineEdit(self.tab_2)
        self.urlEdit.setGeometry(QtCore.QRect(70, 10, 491, 21))
        self.urlEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.urlEdit.setObjectName(_fromUtf8("urlEdit"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(370, 150, 241, 241))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.linkBrowser = QtGui.QTextBrowser(self.groupBox)
        self.linkBrowser.setGeometry(QtCore.QRect(0, 70, 241, 171))
        self.linkBrowser.setOpenLinks(False)
        self.linkBrowser.setObjectName(_fromUtf8("linkBrowser"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.lcdNumber = QtGui.QLCDNumber(self.groupBox)
        self.lcdNumber.setGeometry(QtCore.QRect(100, 20, 131, 41))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 230, 351, 161))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 341, 71))
        self.label_4.setAcceptDrops(True)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.logLabel = QtGui.QLabel(self.groupBox_2)
        self.logLabel.setGeometry(QtCore.QRect(10, 80, 331, 71))
        self.logLabel.setMaximumSize(QtCore.QSize(331, 91))
        self.logLabel.setAcceptDrops(True)
        self.logLabel.setStyleSheet(_fromUtf8("background-color:rgb(242, 255, 183)"))
        self.logLabel.setLineWidth(80)
        self.logLabel.setText(_fromUtf8(""))
        self.logLabel.setTextFormat(QtCore.Qt.LogText)
        self.logLabel.setScaledContents(True)
        self.logLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.logLabel.setWordWrap(True)
        self.logLabel.setIndent(1)
        self.logLabel.setObjectName(_fromUtf8("logLabel"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 390, 601, 61))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.Ad1 = QtGui.QLabel(self.groupBox_3)
        self.Ad1.setGeometry(QtCore.QRect(10, 20, 191, 31))
        self.Ad1.setStyleSheet(_fromUtf8("background-color:rgb(255, 24, 112)"))
        self.Ad1.setOpenExternalLinks(True)
        self.Ad1.setObjectName(_fromUtf8("Ad1"))
        self.Ad2 = QtGui.QLabel(self.groupBox_3)
        self.Ad2.setGeometry(QtCore.QRect(210, 20, 181, 31))
        self.Ad2.setStyleSheet(_fromUtf8("background-color:rgb(0, 85, 255)"))
        self.Ad2.setOpenExternalLinks(True)
        self.Ad2.setObjectName(_fromUtf8("Ad2"))
        self.Ad3 = QtGui.QLabel(self.groupBox_3)
        self.Ad3.setGeometry(QtCore.QRect(400, 20, 191, 31))
        self.Ad3.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 0)"))
        self.Ad3.setOpenExternalLinks(True)
        self.Ad3.setObjectName(_fromUtf8("Ad3"))
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 150, 351, 80))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.comboBox = QtGui.QComboBox(self.groupBox_4)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 111, 41))
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setStyleSheet(_fromUtf8("padding-left:10px"))
        self.comboBox.setDuplicatesEnabled(True)
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.startButton = QtGui.QPushButton(self.groupBox_4)
        self.startButton.setGeometry(QtCore.QRect(130, 30, 101, 41))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.stopButton = QtGui.QPushButton(self.groupBox_4)
        self.stopButton.setGeometry(QtCore.QRect(240, 30, 101, 41))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(510, 440, 101, 31))
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 439, 54, 31))
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Tumload - Tumblr视频下载神器 - 等英软件出品", None))
        self.borseButton.setText(_translate("Dialog", "浏览", None))
        self.label_2.setText(_translate("Dialog", "文件路径", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "从文件读取链接", None))
        self.label_3.setText(_translate("Dialog", "主页地址", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "直接输入链接", None))
        self.groupBox.setTitle(_translate("Dialog", "下载链接", None))
        self.label.setText(_translate("Dialog", "共发现视频：", None))
        self.groupBox_2.setTitle(_translate("Dialog", "系统日志", None))
        self.label_4.setText(_translate("Dialog",
                                        "<html><head/><body><p>由于国内网速问题，请不要选择【保存视频到本地】将下载链接复制到迅雷中下载，效果最好！更多帮助请看<a href=\"http://www.waitig.com/soft/tumload-help.html\" target=\"_blank\">在线帮助文档</a></p></body></html>",
                                        None))
        self.groupBox_3.setTitle(_translate("Dialog", "赞助链接", None))
        self.Ad1.setText(_translate("Dialog", "AD1", None))
        self.Ad2.setText(_translate("Dialog", "AD2", None))
        self.Ad3.setText(_translate("Dialog", "AD3", None))
        self.groupBox_4.setTitle(_translate("Dialog", "控制", None))
        self.comboBox.setItemText(0, _translate("Dialog", "只保存下载链接", None))
        self.comboBox.setItemText(1, _translate("Dialog", "保存视频到本地", None))
        self.startButton.setText(_translate("Dialog", "开始处理", None))
        self.stopButton.setText(_translate("Dialog", "停止处理", None))
        self.label_5.setText(
            _translate("Dialog", "<a href=\"http://www.waitig.com/\" target=\"_blank\">等英博客</a>|荣耀出品|", None))
        self.label_6.setText(_translate("Dialog", "<a href=\"http://www.waitig.com\">我要赞助！</a>", None))


from PyQt4 import QtWebKit