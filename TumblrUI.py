# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Tumload.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
from PyQt4 import QtWebKit

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
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(612, 396)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        Dialog.setFont(font)
        Dialog.setMouseTracking(False)
        Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Dialog.setAcceptDrops(True)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.webView = QtWebKit.QWebView(Dialog)
        self.webView.setGeometry(QtCore.QRect(0, 0, 611, 81))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.lcdNumber = QtGui.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(470, 290, 131, 41))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 150, 451, 181))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(480, 250, 71, 31))
        self.label.setObjectName(_fromUtf8("label"))
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
        self.fileEdit.setObjectName(_fromUtf8("fileEdit"))
        self.borseFile = QtGui.QPushButton(self.tab)
        self.borseFile.setGeometry(QtCore.QRect(500, 10, 81, 23))
        self.borseFile.setObjectName(_fromUtf8("borseFile"))
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
        self.urlEdit.setObjectName(_fromUtf8("urlEdit"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.startButton = QtGui.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(470, 150, 131, 41))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.stopButton = QtGui.QPushButton(Dialog)
        self.stopButton.setGeometry(QtCore.QRect(470, 200, 131, 41))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.Ad1 = QtGui.QLabel(Dialog)
        self.Ad1.setGeometry(QtCore.QRect(10, 340, 161, 41))
        self.Ad1.setOpenExternalLinks(True)
        self.Ad1.setObjectName(_fromUtf8("Ad1"))
        self.Ad2 = QtGui.QLabel(Dialog)
        self.Ad2.setGeometry(QtCore.QRect(220, 340, 161, 41))
        self.Ad2.setOpenExternalLinks(True)
        self.Ad2.setObjectName(_fromUtf8("Ad2"))
        self.Ad3 = QtGui.QLabel(Dialog)
        self.Ad3.setGeometry(QtCore.QRect(430, 340, 161, 41))
        self.Ad3.setOpenExternalLinks(True)
        self.Ad3.setObjectName(_fromUtf8("Ad3"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Tumload--等英软件出品", None))
        self.label.setText(_translate("Dialog", "共发现视频：", None))
        self.borseFile.setText(_translate("Dialog", "浏览", None))
        self.label_2.setText(_translate("Dialog", "文件路径", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "文件", None))
        self.label_3.setText(_translate("Dialog", "主页地址", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "网址", None))
        self.startButton.setText(_translate("Dialog", "开始处理", None))
        self.stopButton.setText(_translate("Dialog", "停止处理", None))
        self.Ad1.setText(_translate("Dialog", "AD1", None))
        self.Ad2.setText(_translate("Dialog", "AD2", None))
        self.Ad3.setText(_translate("Dialog", "AD3", None))
