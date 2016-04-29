import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "Tumload.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QDialog, Ui_MainWindow):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.init()

    def init(self):
        self.borseButton.clicked.connect(self.showDialog)
        self.fileName = ''

    def showDialog(self):
        self.fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                                                          'C:\\')
        self.fileEdit.setText(self.fileName)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
