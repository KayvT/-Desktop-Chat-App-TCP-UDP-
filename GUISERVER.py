# -*- coding: utf-8 -*-
import socket
import select
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import concurrent.futures
from soundwindow import Ui_MainWindow
# from _thread import *
import threading
class Ui_appWindow(object):

    def connect(self):
        ip = self.IpInput_area.text()
        self.server = Server(ip)
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.load_bar.setValue(self.completed)
    def open_sound_window(self):
        self.window = QtWidgets.QMainWindow()
        self.soundUI = Ui_MainWindow()
        self.soundUI.setupUi(self.window)
        self.window.show()
    def open_fileDialog(self):
        name, _ = QFileDialog.getOpenFileName(appWindow, "Open File", options=QFileDialog.DontUseNativeDialog)

    def setupUi(self, appWindow):
      
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
        

        self.retranslateUi(appWindow)
        QtCore.QMetaObject.connectSlotsByName(appWindow)


            # TRIGGERS
        self.connectBTN.clicked.connect(self.connect)
        self.emojiBTN.clicked.connect(self.open_sound_window)
        self.sendFileBTN.clicked.connect(self.open_fileDialog)

    def retranslateUi(self, appWindow):
        _translate = QtCore.QCoreApplication.translate
        appWindow.setWindowTitle(_translate("appWindow", "MainWindow"))
        self.emojiBTN.setText(_translate("appWindow", "SOUND"))
        self.sendFileBTN.setText(_translate("appWindow", "ATTACH A FILE"))
        self.sendBTN.setText(_translate("appWindow", "SEND"))
        self.input_area.setPlaceholderText(_translate("appWindow", "Type your message here!"))
        self.chat_label.setText(_translate("appWindow", "CHAT ROOM"))
        self.room_label.setText(_translate("appWindow", "OPTIONS"))
        self.label.setText(_translate("appWindow", "HOST ADDRESS"))
        self.connectBTN.setText(_translate("appWindow", "CONNECT"))
        self.load_bar.setStatusTip(_translate("appWindow", "Loading bar: will start loading when you click enter"))
        self.label_2.setText(_translate("appWindow", "PICK THE PROTOCOL:"))
        self.nameLabel.setText(_translate("appWindow", "YOUR USERNAME"))
        self.TCPcheckBox.setText(_translate("appWindow", "TCP"))
        self.UDPcheckBox.setText(_translate("appWindow", "UDP"))
        self.menuFile.setTitle(_translate("appWindow", "&File"))
        self.menu_About.setTitle(_translate("appWindow", "&About"))
        self.actionExit.setText(_translate("appWindow", "&Exit"))
        self.actionHome.setText(_translate("appWindow", "&Home"))
        self.actionAboutUS.setText(_translate("appWindow", "&US"))

   

class Server():
    HEADER_LENGTH = 10  # FOR NOW IT IS AN ARBITRARY VALUE
    def __init__(self, ip):
        self.requestedIP = ip
        self.PORT = 5000
        self.clients = {}

        self.TCPserverInit()       
        
    def TCPserverInit(self):
        print("Server is running: \nWaiting for Connections...")
        self.TCPserver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.TCPserver_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.TCPserver_socket.bind((self.requestedIP, self.PORT))
        self.TCPserver_socket.listen(10)
        self.sockets_list = [self.TCPserver_socket]
        threading._start_new_thread(self.communicate_msgs, (self.TCPserver_socket, ' '))
        
    def recv_message(self, client_socket):
        try:
            message_header = client_socket.recv(self.HEADER_LENGTH)
            print(message_header)
            if not len(message_header):
                print(len(message_header))
                return False
            else:
                message_length = int(message_header.decode("utf-8").strip())
                return {"header": message_header, "data": client_socket.recv(message_length)}
        except Exception as e:
            print(str(e))
            return False

    def communicate_msgs(self, server, var_):
        #var_ here is needed because when we create a thread, we must pass a tuple as the function parametes. We do not need to pass anything else other than the server so I had to make a dummy variable. text me if you do not get it.
        print("I came here")
        while True:
            self.readSockets, self.dummyVar, self.exceptionSockets = select.select(self.sockets_list, [], self.sockets_list)
            for new_connected_socket in self.readSockets:
                if new_connected_socket == server:
                    clientSock, clientAddr = server.accept()
                    # print(clientSock, clientAddr)
                    print("why?")
                    new_user = self.recv_message(clientSock)
                    if new_user is False:
                        print(new_user)
                        continue
                    self.sockets_list.append(clientSock)
                    self.clients[clientSock] = new_user
                    print(f"Accepted new connection from {clientAddr}: {clientAddr[1]} Username: {new_user['data'].decode('utf-8')}")
                else:
                    message = self.recv_message(new_connected_socket)
                    if message is False:
                        # name_of_socket = 
                        print(f"Closed connection from {self.clients[new_connected_socket]['data'].decode('utf-8')}")
                        self.sockets_list.remove(new_connected_socket)
                        del self.clients[new_connected_socket]
                        continue

                    new_user = self.clients[new_connected_socket]
                    print(f"Recevied message from {new_user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

                    # actual sending.
                    for client in self.clients:
                        if client != new_connected_socket:
                            print(new_user['header'] + new_user['data'] + message['header'] + message['data'])
                            client.send(new_user['header'] + new_user['data'] + message['header'] + message['data'])

            for new_connected_socket in self.exceptionSockets:
                self.sockets_list.remove(new_connected_socket)
                del self.clients[new_connected_socket]

            # threading._start_new_thread(self.send_recv_Msg, (self.client, self.client_addr))




    # def send_recv_Msg(self, client, addr):
    #     print(client, addr)
    #     test_message = " "
    #     client_name = client.recv(4096)
    #     welcome_message = "Hey there"
    #     client.send(welcome_message.encode('utf-8'))
    #     self.clients['name'] = client_name
    #     print(self.clients['name'])

    #     while True:
    #         data = client.recv(4096)
    #         # print(data +b' Whoops')
    #         if not data: break
    #         text_message = data
    #         print(text_message.decode('utf-8'))
    #         print(self.sockets_list)
    #         for c in self.sockets_list:
    #             if c != client:
    #                 c.send(text_message)
        
    def UDPserverInit(self):
        pass


 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    appWindow = QtWidgets.QMainWindow()
    ui = Ui_appWindow()
    ui.setupUi(appWindow)
    appWindow.show()
    sys.exit(app.exec_())












   # def serverOn(self):



    #     while True:
    #         self.readSockets, self.dummyVar, self.exception_sockets = select.select(self.sockets_list, [], self.sockets_list)
    #         # print('I came in')
    #         #select takes in 3 parameters the "read" list and the "write" lists and the sockets we might server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) error on.
    #         for notified_socket in self.readSockets:
    #             # print("I came in here as well!")
    #             if notified_socket == self.TCPserver_socket:
    #                 self.client_socket, self.client_address = self.TCPserver_socket.accept()

    #                 self.user = self.recv_message(self.client_socket)
    #                 if self.user is False:
    #                     continue
                    
    #                 self.sockets_list.append(self.client_socket)
    #                 print(self.sockets_list[0])
    #                 self.clients[self.client_socket] = self.user

    #                 print(f"accepted new connection from {self.client_address}:{self.client_address[1]} username: {self.user['data'].decode('utf-8')}")
                    


    #             else:
    #                 self.message_ = self.recv_message(notified_socket)
    #                 if self.message_ is False:
    #                     print(f"Closed connection from {self.clients[notified_socket]['data'].decode('utf-8')}")
    #                     self.sockets_list.remove(notified_socket)
    #                     del self.clients[notified_socket]
    #                     continue

    #                 self.user = self.clients[notified_socket]
    #                 print(f"Recevied Message from {self.user['data'].decode('utf-8')}: {self.message_['data'].decode('utf-8')}")

    #                 for client_socket in self.clients:
    #                     if client_socket != notified_socket:
    #                         client_socket.send(self.user['header'] + self.user['data'] + self.message_['header'] + self.message_['data'])
                            
    #         for notified_socket in self.exception_sockets:
    #             self.sockets_list.remove(notified_socket)
    #             del self.clients[notified_socket]
    

