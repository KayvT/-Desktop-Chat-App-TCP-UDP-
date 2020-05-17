# -*- coding: utf-8 -*-
# from PyQt5.QtCore import QObject, pyqtSignal
from playsound import playsound
import os
import time
from datetime import datetime
import json
import ast
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from threading import Thread
import socket
import errno
import select
import sys
from soundwindow import Ui_MainWindow
import requests


class Ui_appWindow(QThread):
    def __init__(self):
        super(Ui_appWindow, self).__init__()
        self.uiElements()
        self.soundCounter = 0
        self.currentTime = None
        self.futureTime = 0
        self.timerStarted = True    
    def uiElements(self):
        appWindow.setObjectName("appWindow")
        appWindow.resize(686, 468)
        appWindow.setMinimumSize(QtCore.QSize(686, 468))
        appWindow.setMaximumSize(QtCore.QSize(690, 470))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        appWindow.setFont(font)
        appWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(appWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(510, 340, 171, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.soundBTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.soundBTN.setObjectName("soundBTN")
        self.verticalLayout.addWidget(self.soundBTN)
        self.sendFileBTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sendFileBTN.setObjectName("sendFileBTN")
        
        self.verticalLayout.addWidget(self.sendFileBTN)
        self.sendBTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sendBTN.setObjectName("sendBTN")
        self.verticalLayout.addWidget(self.sendBTN)
        self.input_area = QtWidgets.QLineEdit(self.centralwidget)
        self.input_area.setGeometry(QtCore.QRect(10, 340, 491, 81))
        self.input_area.setText("") 
        self.input_area.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.input_area.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.input_area.setClearButtonEnabled(False)
        self.input_area.setObjectName("input_area")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(11, 320, 671, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.chat_window = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.chat_window.setGeometry(QtCore.QRect(10, 40, 491, 251))
        self.chat_window.setTabChangesFocus(False)
        self.chat_window.setReadOnly(True)
        self.chat_window.setObjectName("chat_window")
        self.chat_label = QtWidgets.QLabel(self.centralwidget)
        self.chat_label.setGeometry(QtCore.QRect(175, 10, 100, 21))
        self.chat_label.setMinimumSize(QtCore.QSize(0, 0))
        self.chat_label.setObjectName("chat_label")
        self.room_label = QtWidgets.QLabel(self.centralwidget)
        self.room_label.setGeometry(QtCore.QRect(570, 20, 71, 21))
        self.room_label.setMinimumSize(QtCore.QSize(0, 0))
        self.room_label.setObjectName("room_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(500, 40, 20, 291))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(160, 30, 118, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(510, 30, 171, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(542, 130, 121, 17))
        self.label.setObjectName("label")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(670, 40, 20, 291))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.connectBTN = QtWidgets.QPushButton(self.centralwidget)
        self.connectBTN.setGeometry(QtCore.QRect(530, 260, 131, 21))
        self.connectBTN.setObjectName("connectBTN")
        self.connectBTN.clicked.connect(self.connect)
        self.load_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.load_bar.setGeometry(QtCore.QRect(520, 300, 151, 16))
        self.load_bar.setProperty("value", 0)
        self.load_bar.setTextVisible(False)
        self.load_bar.setObjectName("load_bar")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(520, 150, 150, 81))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.IpInput_area = QtWidgets.QLineEdit(self.widget)
        self.IpInput_area.setObjectName("IpInput_area")
        self.verticalLayout_2.addWidget(self.IpInput_area)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(540, 220, 116, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TCPcheckBox = QtWidgets.QCheckBox(self.widget1)
        self.TCPcheckBox.setObjectName("TCPcheckBox")
        self.horizontalLayout.addWidget(self.TCPcheckBox)
        self.UDPcheckBox = QtWidgets.QCheckBox(self.widget1)
        self.UDPcheckBox.setObjectName("UDPcheckBox")
        self.horizontalLayout.addWidget(self.UDPcheckBox)
        appWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(appWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu_About = QtWidgets.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")
        appWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(appWindow)
        self.statusBar.setObjectName("statusBar")
        appWindow.setStatusBar(self.statusBar)
        # ACTIONS:
        self.actionExit = QtWidgets.QAction(appWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.quitWindow)

        self.actionAboutUS = QtWidgets.QAction(appWindow)
        self.actionAboutUS.setObjectName("actionAboutUS")
        self.actionAboutUS.triggered.connect(self.InfoAboutUs)

        self.menuFile.addAction(self.actionExit)
        self.menu_About.addAction(self.actionAboutUS)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())

        self.NameInput_area = QtWidgets.QLineEdit(self.centralwidget)
        self.NameInput_area.setGeometry(QtCore.QRect(520, 80, 148, 25))
        self.NameInput_area.setObjectName("NameInput_area")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(530, 60, 131, 17))
        self.nameLabel.setObjectName("nameLabel")
        self.Download_CancelBTN = QtWidgets.QPushButton(self.centralwidget)
        self.Download_CancelBTN.setGeometry(QtCore.QRect(180, 300, 151, 21))
        self.Download_CancelBTN.setObjectName("Download_CancelBTN")
        self.Download_CancelBTN.setVisible(False)
        self.Download_CancelBTN.clicked.connect(lambda x: self.client.handleDownloadCancelBTN(self.Download_CancelBTN))
        self.FileName = QtWidgets.QLabel(self.centralwidget)
        self.FileName.setGeometry(QtCore.QRect(40, 290, 171, 41))
        self.FileName.setObjectName("FileName")
        self.LoadingSpeed = QtWidgets.QLabel(self.centralwidget)
        self.LoadingSpeed.setGeometry(QtCore.QRect(350, 300, 300, 20))
        self.LoadingSpeed.setObjectName("LoadingSpeed")
        appWindow.show()
        self.retranslateUi(appWindow)
        QtCore.QMetaObject.connectSlotsByName(appWindow)

        # TRIGGERS:
        self.soundBTN.clicked.connect(self.open_sound_window)
        self.sendFileBTN.clicked.connect(self.open_fileDialog)

        #STYLES: 
        self.connectBTN.setStyleSheet(":hover:!pressed{background-color: lawngreen}")
        self.soundBTN.setStyleSheet(":hover:!pressed{background-color: lightgreen}")
        self.sendBTN.setStyleSheet(":hover:!pressed{background-color: lightgreen}")
        self.sendFileBTN.setStyleSheet(":hover:!pressed{background-color: lightgreen}")



    def retranslateUi(self, appWindow):
        _translate = QtCore.QCoreApplication.translate
        appWindow.setWindowTitle(_translate("appWindow", "MainWindow"))
        self.soundBTN.setText(_translate("appWindow", "SOUND"))
        self.sendFileBTN.setText(_translate("appWindow", "BROWSE"))
        self.sendBTN.setText(_translate("appWindow", "SEND"))
        # self.LoadingSpeed.setText("300 kb/s")
        self.input_area.setPlaceholderText(_translate("appWindow", "Type your message here!"))
        self.chat_label.setText(_translate("appWindow", "CHAT ROOM"))
        self.room_label.setText(_translate("appWindow", "OPTIONS"))
        self.label.setText(_translate("appWindow", "HOST ADDRESS"))
        self.connectBTN.setText(_translate("appWindow", "CONNECT"))
        self.load_bar.setStatusTip(_translate(
            "appWindow", "Loading bar: will start loading when you click connect"))
        self.label_2.setText(_translate("appWindow", "PICK THE PROTOCOL:"))
        self.nameLabel.setText(_translate("appWindow", "YOUR USERNAME"))
        self.TCPcheckBox.setText(_translate("appWindow", "TCP"))
        self.UDPcheckBox.setText(_translate("appWindow", "UDP"))
        self.menuFile.setTitle(_translate("appWindow", "&File"))
        self.menu_About.setTitle(_translate("appWindow", "&About"))
        self.actionExit.setText(_translate("appWindow", "&Exit"))
        self.actionAboutUS.setText(_translate("appWindow", "&US"))
        appWindow.setWindowTitle("Reach ChatApp")
        self.sendBTN.setDisabled(True)
        self.soundBTN.setDisabled(True)
        self.sendFileBTN.setDisabled(True)
        self.input_area.setReadOnly(True)

    def quitWindow(self):
        sys.exit()

    def InfoAboutUs(self):
        info_pop_up_msg = QtWidgets.QMessageBox()
        info_pop_up_msg.setWindowTitle("Who are we?")
        info_pop_up_msg.setText("Reach ChatApp was developed by 2 Egyptian Friends in Istanbul Sehir University. It was done as practice of sockets programming, Pyqt5, and finally signals and threads. We hope you like this app, because we really loved making it!")
        info_pop_up_msg.setIcon(QtWidgets.QMessageBox.Information)
        info_pop_up_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        info_pop_up_msg.exec_()
    def open_sound_window(self):
        self.window = QtWidgets.QMainWindow()
        self.soundUI = Ui_MainWindow()
        self.soundUI.setupUi(self.window)
        self.window.show()
        self.soundUI.trigger.connect(self.soundButtonClicked)

    def soundButtonClicked(self, clickedButton):
        
        if self.soundCounter > 5 and self.timerStarted:
            self.currentTime = time.time()
            self.timerStarted = False
            self.futureTime = self.currentTime + 10
        elif self.futureTime > time.time():
            pop_up_msg = QtWidgets.QMessageBox()
            pop_up_msg.setWindowTitle("Too many clicks")
            pop_up_msg.setText("You sent too many. Wait for 10 seconds...")
            pop_up_msg.setIcon(QtWidgets.QMessageBox.Warning)
            pop_up_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            pop_up_msg.exec_()
            return 
        elif self.futureTime < time.time() and not self.timerStarted: 
            self.soundCounter = 0
            self.timerStarted = True
            

        self.soundCounter += 1
        try: 
            self.serverAddressPort = (self.hostIp, 20001)
        except: 
            self.serverAddressPort = ('127.0.0.1', 20001)
        self.bufferSize = 1024
        soundMessage = '$ou#+'
        message = (soundMessage + ' ' + str(clickedButton)).encode('utf-8')

        if self.TCPcheckBox.isChecked():
            self.client.TCPclientSocket.send(message)
        else:
            ###### TODO CHANGE THIS 
            self.serverAddressPort = ('127.0.0.1', 20001)
            self.client.UDPClientSocket.sendto(message, self.serverAddressPort)

    def connect(self):
        # to make sure the user is not just clicking connect without typing in info.      
        while  (not (self.TCPcheckBox.isChecked() or self.UDPcheckBox.isChecked()) or not(self.IpInput_area.text() and self.NameInput_area.text()) or ( self.TCPcheckBox.isChecked() and  self.UDPcheckBox.isChecked())):
            pop_up_msg = QtWidgets.QMessageBox()
            pop_up_msg.setWindowTitle("Come on, really?")
            pop_up_msg.setText(
                "You cannot do that. You have to enter a name, an Ip, and check one of the protocols.")
            pop_up_msg.setIcon(QtWidgets.QMessageBox.Warning)
            pop_up_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            pop_up_msg.exec_()
            if pop_up_msg.buttonClicked:
                return
                
                # return 
    
        if self.TCPcheckBox.isChecked():
            checked = self.TCPcheckBox
            print("whoop, TCP connection!")
        else:
            checked = self.UDPcheckBox
            print('UDP connection')
            # quit()
            # i do not need to check if atleast one of them is checked already because I have already done that in the while loop.
        self.load_bar.setTextVisible(True)
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.00015
            self.load_bar.setValue(self.completed)
        # getting the values:
        self.hostIp = self.IpInput_area.text()
        hostName = self.NameInput_area.text()
        # the following lines are to make sure the user does not crash the application by changing his optins and clicking connect again.
        self.connectBTN.setDisabled(True)
        self.sendBTN.setDisabled(False)
        self.soundBTN.setDisabled(False)
        self.sendFileBTN.setDisabled(False)
        self.TCPcheckBox.setDisabled(True)
        self.UDPcheckBox.setDisabled(True)
        self.input_area.setReadOnly(False)
        self.IpInput_area.clear()
        self.IpInput_area.setReadOnly(True)
        self.NameInput_area.clear()
        self.NameInput_area.setReadOnly(True)
        self.load_bar.setValue(0)
        self.load_bar.setTextVisible(False)
        # actually connecting is done here
        self.client = Client(hostName, self.hostIp, checked)
        self.client.startConnection()
        self.client.start()  # starting the threads
        # connecting to the signal of the client
        self.client.trigger.connect(self.connect_slots)

    def connect_slots(self, receivedMessage):
        playSound = False
        if '$ou#+' in receivedMessage:
            soundNumber = receivedMessage.split(' ')[-1]
            receivedMessage = f'Sound number {soundNumber} was played!!'
            playSound = True
        elif 'clearFileUI' in receivedMessage:
            self.FileName.setText('')
            self.Download_CancelBTN.setText('')
            self.LoadingSpeed.setText('')
            self.Download_CancelBTN.setVisible(False)
            self.LoadingSpeed.setVisible(False)
            return
        elif '$file$l#' in receivedMessage:
            self.FileName.setText(receivedMessage.split('-')[-1])
            self.Download_CancelBTN.setText('Download')
            self.Download_CancelBTN.setVisible(True)
            self.LoadingSpeed.setVisible(True)
            return 
        elif 'updateRate' in receivedMessage:
            s =  receivedMessage.split('-')[1]
            self.LoadingSpeed.setText(s)
            return 
        receivedMessage = f'{receivedMessage}  ({datetime.fromtimestamp(int(time.time())).strftime("%H:%M")})'
        ui.chat_window.insertPlainText(receivedMessage)
        ui.chat_window.insertPlainText("\n")
        ui.chat_window.repaint()
        if playSound:
            soundFile = os.path.join(os.getcwd(), f'SOUNDS/{soundNumber}.mp3')
            playsound(soundFile)

    def open_fileDialog(self):
        file_, _ = QFileDialog.getOpenFileName(
            appWindow, "Open File", options=QFileDialog.DontUseNativeDialog)
        chosenFileName = file_.split('/')[-1]
        self.FileName.setText(chosenFileName)
        self.Download_CancelBTN.setVisible(True)
        self.Download_CancelBTN.setText('Cancel')
        self.LoadingSpeed.setVisible(True)
        if  self.TCPcheckBox.isChecked():
            self.client.sendFileTCP(chosenFileName)
        else: 
            self.client.sendFileUDP(chosenFileName)


class Client(QThread):
    """ signal the client uses to send the received message
        to the GUI then, the GUI inserts the message 
    """
    trigger = pyqtSignal(str)
    HEADER_LENGTH = 10
    def __init__(self, name, ip, checkbox):
        super(Client, self).__init__()
        self.requestedIp = ip
        self.user_name = name
        self.checkboxState = checkbox
        self.PORT = 5000
        self.filename = None
        self.metadata = None
        # self.gui = Ui_appWindow()
        
    def startConnection(self):
        if self.checkboxState.text() == "TCP":
            self.TCPserverInit(self.requestedIp, 4)
        else:
            self.UDPserverInit(self.requestedIp)

    def UDPserverInit(self, ip):

        # TODO may send the names first here

        self.bufferSize = 1024
        # Create a UDP socket at client side
        self.UDPClientSocket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)

        NameLengthtoSend = f'$name$#:{len(self.user_name)}'.encode('utf-8')
        Name_toSend = self.user_name.encode('utf-8')
        try:
            self.serverAddressPort = (ip, 20001)
                  # send names first (to be added to clients list)
            self.UDPClientSocket.sendto(NameLengthtoSend, self.serverAddressPort)
            self.UDPClientSocket.sendto(Name_toSend, self.serverAddressPort)
        except: 
            self.serverAddressPort = ("127.0.0.1", 20001)
            self.UDPClientSocket.sendto(NameLengthtoSend, self.serverAddressPort)
            self.UDPClientSocket.sendto(Name_toSend, self.serverAddressPort)

  

        welcome_ = f"You are connected, {self.user_name}! Start Messaging!! \n -Reach Chat App Assistant \n ---------------------------------------------------------------\n"
        ui.chat_window.insertPlainText(welcome_)
        ui.sendBTN.clicked.connect(self.sendBTN_handle)

        """ send message when enter is pressed """
        ui.input_area.returnPressed.connect(self.sendBTN_handle)

        ui.chat_window.repaint()


    def TCPserverInit(self, ip, var_):
        self.TCPclientSocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        try: 
            self.TCPclientSocket.connect((ip, self.PORT))
        except: 
            self.TCPclientSocket.connect(("127.0.0.1", self.PORT))
            
        self.TCPclientSocket.setblocking(False)
        self.encoded_username = self.user_name.encode('utf-8')
        self.username_header = f"{len(self.encoded_username):<{self.HEADER_LENGTH}}".encode(
            'utf-8')

        self.TCPclientSocket.send(self.username_header + self.encoded_username)
        welcome_ = f"You are connected, {self.user_name}! Start Messaging!! \n -Reach Chat App Assistant \n ---------------------------------------------------------------\n"

        ui.chat_window.insertPlainText(welcome_)
        ui.sendBTN.clicked.connect(self.sendBTN_handle)

        """ send message when enter is pressed """
        ui.input_area.returnPressed.connect(self.sendBTN_handle)

        ui.chat_window.repaint()


    def run(self):
        if self.checkboxState.text() == "TCP":
            while True:
                self.receiveMessage(self.TCPclientSocket)
        else:
            while True:
                self.receiveMessageUDP()

    def sendBTN_handle(self):

        if self.checkboxState.text() == "TCP":
            self.TCPcommunicate_msgs(self.TCPclientSocket, ' ')
        elif self.checkboxState.text() == "UDP":
            self.udpSending()
        ui.input_area.clear()
        ui.chat_window.repaint()

    def udpSending(self):
        self.unEncodedMessage = ui.input_area.text()
        if self.unEncodedMessage:
            msgLengthHeader = f'$msg#{len(self.unEncodedMessage)}'
            self.message = self.unEncodedMessage.encode('utf-8')
            self.UDPClientSocket.sendto(msgLengthHeader.encode('utf-8'), self.serverAddressPort)
            self.UDPClientSocket.sendto(self.message, self.serverAddressPort)
            own_chat_text = self.user_name + ">>" + self.unEncodedMessage
            own_chat_text = f'{own_chat_text}  ({datetime.fromtimestamp(int(time.time())).strftime("%H:%M")})'
            ui.chat_window.insertPlainText(own_chat_text)
            ui.chat_window.insertPlainText("\n")
            ui.chat_window.repaint()

    def TCPcommunicate_msgs(self, sock, var_):
        self.unEncodedMessage = ui.input_area.text()
        if self.unEncodedMessage:
            self.message = self.unEncodedMessage.encode('utf-8')
            self.message_header = f"{len(self.message):<{self.HEADER_LENGTH}}".encode(
                'utf-8')
            sock.send(self.message_header + self.message)

            own_chat_text = self.user_name + ">>" + self.unEncodedMessage
            own_chat_text = f'{own_chat_text}  ({datetime.fromtimestamp(int(time.time())).strftime("%H:%M")})'
            ui.chat_window.insertPlainText(own_chat_text)
            ui.chat_window.insertPlainText("\n")

            """ repainting the widget after appending text to it """
            ui.chat_window.repaint()


    def receiveMessageUDP(self):
        message_header = self.UDPClientSocket.recvfrom(10)
        msg =  message_header[0].decode('utf-8')
        if not msg: return
         
        if '$msg#' in msg:
            msgLength = int(message_header[0].decode('utf-8').split('#')[1])
            message = self.UDPClientSocket.recvfrom(msgLength)
            self.trigger.emit(message[0].decode('utf-8'))
        elif '$ou#+' in msg:
            self.trigger.emit(msg)
        elif '$file$l#' in msg:
            lengName = int(msg.split('#')[-1])
            self.filename = self.UDPClientSocket.recvfrom(lengName)[0].decode('utf-8')
            self.trigger.emit(msg+'-'+self.filename)
            clean = self.UDPClientSocket.recvfrom(10)[0].decode('utf-8').split('#')[0]
            print(f'The file {self.filename} is {clean}')
        elif '$cancelDd$' in msg:
            self.trigger.emit('clearFileUI')
        elif '$acceptDd$' in msg:
            seqNumber = 1
            filetosend = open(self.filename, "rb")
            data = filetosend.read(1000)
            self.UDPClientSocket.sendto('filep:    '.encode('utf-8'), self.serverAddressPort)
            self.UDPClientSocket.sendto(f'{seqNumber}'.encode(), self.serverAddressPort)
            self.UDPClientSocket.sendto(data, self.serverAddressPort)
            bytesSend = 0
            now = time.time()
            t = int(now % 60)
            while data:
                print(f"Sending packet: {seqNumber}")
                bytesSend += len(data) * 8
                t = time.time() - t 
                self.trigger.emit(f'updateRate-{round(bytesSend/t, 5)} bits/s')
                print(f'updateRate-{round(bytesSend/t, 5)} bits/s')
                time.sleep(.2)
                data = filetosend.read(1000)
                seqNumber += 1
                self.UDPClientSocket.sendto(f'{seqNumber}'.encode(), self.serverAddressPort)
                self.UDPClientSocket.sendto(data, self.serverAddressPort)

            filetosend.close()
            self.trigger.emit('clearFileUI')
            print("Done Sending.")
        
        elif '$fileData$' in msg:
            bytesSend = 0
            now = time.time()
            t = int(now % 60)
            packets = []
            seq_num = self.UDPClientSocket.recvfrom(50)
            data = self.UDPClientSocket.recvfrom(1000)
            while True:
                print(f"Receving Packet: {seq_num[0].decode()}")
                if '$#end^$'.encode('utf-8') in data[0]:
                    packets.append((seq_num[0], data[0]))
                    break
                bytesSend += len(data) * 8
                t = time.time() - t 
                self.trigger.emit(f'updateRate-{round(bytesSend/t, 5)} bits/s')
                print(f'updateRate-{round(bytesSend/t, 5)} bits/s')
                time.sleep(.2)
                packets.append((seq_num[0], data[0]))
                seq_num = self.UDPClientSocket.recvfrom(50)
                data = self.UDPClientSocket.recvfrom(1000)  

            print("Done Receiving.")

            #packet losses
            packet_losses = int(packets[-1][0].decode()) - len(packets)
            print(f'Packet Losses: {packet_losses}')
            
            #changed order
            changed_order = 0
            for i in range(1, len(packets)+1):
                if int(packets[i-1][0].decode()) != i:
                    changed_order+=1
            print(f'Packets Changed Order: {changed_order}')

            # fix changed order (to test changed order)
            x = packets[:-1]
            x.sort(key=lambda x: int(x[0].decode()))

            #writing to the file
            f = open(f'copy{self.filename}', 'wb')
            for seq, pk in x:
                f.write(pk)
                  
            self.trigger.emit('clearFileUI')

    def handleDownloadCancelBTN(self, btn):
        txt = btn.text()
        if txt == 'Download':
            if self.checkboxState.text() == 'TCP':
                self.TCPclientSocket.send('$acceptDd$'.encode('utf-8'))
            else: 
                self.UDPClientSocket.sendto('$acceptDd$'.encode('utf-8'), self.serverAddressPort)
        elif txt == 'Cancel':
            if self.checkboxState.text() == 'TCP':
                self.TCPclientSocket.send('$cancelDd$'.encode('utf-8'))
                self.trigger.emit('clearFileUI')
            else:
                self.UDPClientSocket.sendto('$cancelDd$'.encode('utf-8'), self.serverAddressPort)
                self.trigger.emit('clearFileUI')


    def receiveMessage(self, sock):
        try:
            soundMessage = False
            self.otherUserNamesHeader = sock.recv(self.HEADER_LENGTH)
            if '$ou#+' in self.otherUserNamesHeader.decode('utf-8'):
                self.trigger.emit(self.otherUserNamesHeader.decode('utf-8'))
                return
            if '$file$l#' in self.otherUserNamesHeader.decode('utf-8'):
                lengName = int(self.otherUserNamesHeader.decode('utf-8').split('#')[-1])
                self.filename = sock.recv(lengName).decode('utf-8')
                self.trigger.emit(self.otherUserNamesHeader.decode('utf-8')+'-'+self.filename)
                clean = sock.recv(10).decode('utf-8').split('#')
                print(f'The file {self.filename} is {clean[0]}')
                #metadata 
                lenPackets = self.TCPclientSocket.recv(10).decode().split('-')
                read = lenPackets[1]
                to_read = int(lenPackets[0]) - len(read) 
                metadata = self.TCPclientSocket.recv(to_read)
                self.metadata = ast.literal_eval(read + metadata.decode())
                return 
            if '$acceptDd$' in self.otherUserNamesHeader.decode('utf-8'):
                self.startUploading(self.TCPclientSocket)
                return 
            if '$cancelDd$' in self.otherUserNamesHeader.decode('utf-8'):
                self.trigger.emit('clearFileUI')
                return 
            if '$fileData$' in self.otherUserNamesHeader.decode('utf-8'):
                seq_packets = []
                dataReceived = b''
                bytesSend = 0
                now = time.time()
                t = int(now % 60)
                f = open(f'copy{self.filename}', 'wb')
                for seq, size in self.metadata:
                    data = sock.recv(size)
                    bytesSend += len(data) * 8
                    time.sleep(.1)
                    t = time.time() - t 
                    self.trigger.emit(f'updateRate-{round(bytesSend/t, 5)} bits/s')
                    dataReceived += data  
                f.write(dataReceived)
                f.close()
                self.trigger.emit('clearFileUI')
                print("Done Receiving.")
                return 
            if not len(self.otherUserNamesHeader):
                ui.chat_window.insertPlainText(
                    "connection closed by the server")
                sys.exit()
            self.otherUserNamesLength = int(
                self.otherUserNamesHeader.decode('utf-8').strip())

            self.otherUserName_s = sock.recv(self.otherUserNamesLength)
            message_header = sock.recv(self.HEADER_LENGTH)  # message header
            lengthOfMessage = int(message_header.decode(
                'utf-8').strip())  # length of the message
            # reading the message using the length(header) of it
            message = sock.recv(lengthOfMessage)
            recvd_msg = f"{self.otherUserName_s.decode('utf-8').strip()}>> {message.decode('utf-8').strip()}"

            self.trigger.emit(recvd_msg)

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: ', str(e))
                sys.exit()
            # continue
        except Exception as e:
            print('General Error: ', str(e))
            sys.exit()

    def sendFileUDP(self, filename):
        self.filename = filename
        self.UDPClientSocket.sendto(f'$file$l#{len(filename)}'.encode('utf-8'), self.serverAddressPort)
        self.UDPClientSocket.sendto(self.filename.encode('utf-8'), self.serverAddressPort)
        if self.cleanIsFile(filename):
            self.UDPClientSocket.sendto('clean####$'.encode('utf-8'), self.serverAddressPort)
        else: 
            self.UDPClientSocket.sendto('notclean##'.encode('utf-8'), self.serverAddressPort)


    def sendFileTCP(self, filename):
        self.filename = filename
        self.TCPclientSocket.send((f'$file$l#{len(filename)}').encode('utf-8'))
        self.TCPclientSocket.send(filename.encode('utf-8'))
        if self.cleanIsFile(filename):
            self.TCPclientSocket.send('clean####$'.encode('utf-8'))
        else: 
            self.TCPclientSocket.send('notclean##'.encode('utf-8'))
        #send metadata 
        packets = []
        seqNumber = 1
        filetosend = open(self.filename, "rb")
        data = filetosend.read(1000)
        while data:
            packets.append((seqNumber, len(data)))
            data = filetosend.read(1000)
            seqNumber+=1
        filetosend.close()
        self.TCPclientSocket.send(f'{len(str(packets))}-'.encode())
        self.TCPclientSocket.send(f'{packets}'.encode())

    def cleanIsFile(self, filename):
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        params = {'apikey':'59a867cceeef5a71ecdb5d49cfdad284ca89fe086b0a141693c3849485d46f22'}
        f = {'file': (filename, open(filename, 'rb'))}
        response = requests.post(url, files=f, params=params)
        return response.json()['response_code']

    def startUploading(self, sock):
        # divide data into packets 
        packets = {}
        seqNumber = 1
        filetosend = open(self.filename, "rb")
        data = filetosend.read(1000)

        if self.checkboxState.text() == "TCP":
            sock.send('filep:    '.encode('utf-8'))
        else:
            sock.sendto('filep:    '.encode('utf-8'), self.serverAddressPort)
      
        sock.send(data)
        bytesSend = 0
        now = time.time()
        t = int(now % 60)
        while data:
            print("Sending...")
            sock.send(data)
            bytesSend += len(data) * 8
            t = time.time() - t 
            self.trigger.emit(f'updateRate-{round(bytesSend/t, 5)} bits/s')
            print(f'updateRate-{round(bytesSend/t, 5)} bits/s')
            time.sleep(.1)
            packets[seqNumber] = data
            data = filetosend.read(1000)
            seqNumber += 1

        # for pk in packets:
            # print('length of packet', len(packets[pk]), 'seqNum:', pk)
            # print(packets[pk])
        filetosend.close()
        self.trigger.emit('clearFileUI')
        print("Done Sending.")
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion') 
    appWindow = QtWidgets.QMainWindow()
    ui = Ui_appWindow()
    ui.start()
    sys.exit(app.exec_())
