# -*- coding: utf-8 -*-
# from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from threading import Thread
import socket
import errno
import select
import sys

class Ui_appWindow(QThread):

    def __init__(self):
        super(Ui_appWindow, self).__init__()
        self.uiElements()
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
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.emojiBTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.emojiBTN.setObjectName("emojiBTN")
        self.verticalLayout.addWidget(self.emojiBTN)
        self.sendFileBTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sendFileBTN.setObjectName("sendFileBTN")
        self.verticalLayout.addWidget(self.sendFileBTN)
        self.sendBTN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sendBTN.setObjectName("sendBTN")
        self.verticalLayout.addWidget(self.sendBTN)
        self.input_area = QtWidgets.QLineEdit(self.centralwidget)
        self.input_area.setGeometry(QtCore.QRect(10, 340, 491, 81))
        self.input_area.setText("")
        self.input_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.input_area.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.input_area.setClearButtonEnabled(False)
        self.input_area.setObjectName("input_area")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(11, 320, 671, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.chat_window = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.chat_window.setGeometry(QtCore.QRect(10, 40, 491, 281))
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
        self.actionExit = QtWidgets.QAction(appWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHome = QtWidgets.QAction(appWindow)
        self.actionHome.setObjectName("actionHome")
        self.actionAboutUS = QtWidgets.QAction(appWindow)
        self.actionAboutUS.setObjectName("actionAboutUS")
        self.menuFile.addAction(self.actionHome)
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
        appWindow.show()
        self.retranslateUi(appWindow)
        QtCore.QMetaObject.connectSlotsByName(appWindow)

    def retranslateUi(self, appWindow):
        _translate = QtCore.QCoreApplication.translate
        appWindow.setWindowTitle(_translate("appWindow", "MainWindow"))
        self.emojiBTN.setText(_translate("appWindow", "EMOJI"))
        self.sendFileBTN.setText(_translate("appWindow", "ATTACH A FILE"))
        self.sendBTN.setText(_translate("appWindow", "SEND"))
        self.input_area.setPlaceholderText(_translate("appWindow", "Type your message here!"))
        self.chat_label.setText(_translate("appWindow", "CHAT ROOM"))
        self.room_label.setText(_translate("appWindow", "OPTIONS"))
        self.label.setText(_translate("appWindow", "HOST ADDRESS"))
        self.connectBTN.setText(_translate("appWindow", "CONNECT"))
        self.load_bar.setStatusTip(_translate("appWindow", "Loading bar: will start loading when you click connect"))
        self.label_2.setText(_translate("appWindow", "PICK THE PROTOCOL:"))
        self.nameLabel.setText(_translate("appWindow", "YOUR USERNAME"))
        self.TCPcheckBox.setText(_translate("appWindow", "TCP"))
        self.UDPcheckBox.setText(_translate("appWindow", "UDP"))
        self.menuFile.setTitle(_translate("appWindow", "&File"))
        self.menu_About.setTitle(_translate("appWindow", "&About"))
        self.actionExit.setText(_translate("appWindow", "&Exit"))
        self.actionHome.setText(_translate("appWindow", "&Home"))
        self.actionAboutUS.setText(_translate("appWindow", "&US"))
        appWindow.setWindowTitle("Reach ChatApp")


    def connect(self):
        
        #to make sure the user is not just clicking connect without typing in info.
        while self.TCPcheckBox.isChecked() != True or self.UDPcheckBox.isChecked() != True and not self.IpInput_area or not self.NameInput_area:
            pop_up_msg = QtWidgets.QMessageBox()
            pop_up_msg.setWindowTitle("Come on, really? like, really?")
            pop_up_msg.setText("You cannot do that. You have to enter a name, an Ip, and check one of the protocols.")
            pop_up_msg.setIcon(QtWidgets.QMessageBox.Warning)
            pop_up_msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            pop_up_msg.exec_()
            if pop_up_msg.buttonClicked:
                break
        else:
           
            if self.TCPcheckBox.isChecked():
                checked = self.TCPcheckBox
            else:
                checked = self.UDPcheckBox
                print('UDP connection')
                # i do not need to check if atleast one of them is checked already because I have already done that in the while loop.
            self.load_bar.setTextVisible(True)
            self.completed = 0
            while self.completed < 100:
                self.completed += 0.00015
                self.load_bar.setValue(self.completed)
            #getting the values:
            hostIp = self.IpInput_area.text()
            hostName = self.NameInput_area.text()
            # the following lines are to make sure the user does not crash the application by changing his optins and clicking connect again.
            self.connectBTN.setDisabled(True)
            self.TCPcheckBox.setDisabled(True)
            self.UDPcheckBox.setDisabled(True)
            self.IpInput_area.clear()
            self.IpInput_area.setReadOnly(True)
            self.NameInput_area.clear()
            self.NameInput_area.setReadOnly(True)
            self.load_bar.setValue(0)
            self.load_bar.setTextVisible(False)
            #actually connecting is done here
            #### changes #####
            self.client = Client(hostName, hostIp, checked)
            self.client.startConnection()
            self.client.start() # starting the threads
            self.client.trigger.connect(self.connect_slots) # connecting to the signal of the client

    def connect_slots(self, receivedMessage):
    
        ui.chat_window.insertPlainText(receivedMessage)
        ui.chat_window.insertPlainText("\n")
        ui.chat_window.repaint()

class Client(QThread):
    """ signal the client uses to send the received message
        to the GUI then, the GUI inserts the message 
    """
    trigger = pyqtSignal(str) 
    HEADER_LENGTH = 10
    # self.Gui = Ui_appWindow()
    def __init__(self, name, ip, checkbox):
        super(Client, self).__init__()
        self.requestedIp = ip
        self.user_name = name
        self.checkboxState = checkbox
        self.PORT = 5000
    
    def startConnection(self):
        if self.checkboxState.text() == "TCP":
            # threading._start_new_thread(self.TCPserverInit, (self.requestedIp, ' '))
            self.TCPserverInit(self.requestedIp, 4)
        else:
            #UDP CODE HERE
            print('UDP connection')
        
    def TCPserverInit(self, ip, var_):
        # self.my_username = input("Type in your username: ")
        self.TCPclientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.TCPclientSocket.connect((ip, self.PORT))
        self.TCPclientSocket.setblocking(False)
        self.encoded_username = self.user_name.encode('utf-8')
        self.username_header = f"{len(self.encoded_username):<{self.HEADER_LENGTH}}".encode('utf-8')
        
        self.TCPclientSocket.send(self.username_header + self.encoded_username)
        welcome_ = f"You are connected, {self.user_name}! Start Messaging!! \n -Reach Chat App Assistant \n ---------------------------------------------------------------\n"

        ui.chat_window.insertPlainText(welcome_)
        ui.sendBTN.clicked.connect(self.sendBTN_handle)
        
        #######  My changes  ########
        """ send message when enter is pressed """ 
        ui.input_area.returnPressed.connect(self.sendBTN_handle)

        ui.chat_window.repaint()

        ###########################

    def run(self):
        while True:
            self.receiveMessage(self.TCPclientSocket)

    def sendBTN_handle(self):        
        self.TCPcommunicate_msgs(self.TCPclientSocket, ' ')

        ### MyChanges ###
        ui.input_area.clear()
        ################


    def TCPcommunicate_msgs(self, sock, var_):
        self.unEncodedMessage = ui.input_area.text()
        if self.unEncodedMessage:
            self.message = self.unEncodedMessage.encode('utf-8')
            self.message_header = f"{len(self.message):<{self.HEADER_LENGTH}}".encode('utf-8')
            sock.send(self.message_header + self.message)

            own_chat_text = self.user_name + ">>" + self.unEncodedMessage
            ui.chat_window.insertPlainText(own_chat_text)
            ui.chat_window.insertPlainText("\n")
        
            ###### My changes #######
            """ repainting the widget after appending text to it """
            ui.chat_window.repaint()

            #########################

       
        # self.receiveMessage(sock) # receive messages from the server of the other clients
        

    def receiveMessage(self, sock):
        try:
        #this is where I receive things
            # FOR USERNAME
            self.otherUserNamesHeader = sock.recv(self.HEADER_LENGTH)
            if not len(self.otherUserNamesHeader):
                ui.chat_window.insertPlainText("connection closed by the server")
                sys.exit()
            self.otherUserNamesLength = int(self.otherUserNamesHeader.decode('utf-8').strip())

            #######  My changes  ########

            self.otherUserName_s = sock.recv(self.otherUserNamesLength) 
            message_header = sock.recv(self.HEADER_LENGTH) # message header
            lengthOfMessage = int(message_header.decode('utf-8').strip()) # length of the message
            message = sock.recv(lengthOfMessage)  # reading the message using the length(header) of it
            recvd_msg = f"{self.otherUserName_s.decode('utf-8').strip()}>> {message.decode('utf-8').strip()}"
            
            self.trigger.emit(recvd_msg)
         

            #########################
        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: ', str(e))
                sys.exit()
            # continue
        except Exception as e:
            print('General Error: ', str(e))
            sys.exit()

  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # app.setWindowTitle("Reach ChatApp")
    appWindow = QtWidgets.QMainWindow()
    ui = Ui_appWindow()
    ui.start()
    sys.exit(app.exec_())

