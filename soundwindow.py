# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'soundWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
class Ui_MainWindow(QObject):
    trigger = pyqtSignal(int)
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(668, 133)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(10, 30, 89, 71))
        self.one.setObjectName("one")
        self.one.clicked.connect(self.buttonClicked) # connect signal to slot
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(120, 30, 89, 71))
        self.two.setObjectName("two")
        self.two.clicked.connect(self.buttonClicked) # connect signal to slot
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(230, 30, 89, 71))
        self.three.setObjectName("three")
        self.three.clicked.connect(self.buttonClicked) # connect signal to slot
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(350, 30, 89, 71))
        self.four.setObjectName("four")
        self.four.clicked.connect(self.buttonClicked) # connect signal to slot
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(460, 30, 89, 71))
        self.five.setObjectName("five")
        self.five.clicked.connect(self.buttonClicked) # connect signal to slot
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(570, 30, 89, 71))
        self.six.setObjectName("six")
        self.six.clicked.connect(self.buttonClicked) # connect signal to slot
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.one.setText(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.three.setText(_translate("MainWindow", "3"))
        self.four.setText(_translate("MainWindow", "4"))
        self.five.setText(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))

    def buttonClicked(self):
        sender = self.MainWindow.sender()
        self.trigger.emit(int(sender.text()))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

