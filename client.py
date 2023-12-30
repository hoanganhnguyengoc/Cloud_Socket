# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QFileDialog
import os
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import socket
from utilz.method import *
from utilz.constant import *
from utilz.Client import Client
import os

host_name=socket.gethostname()
HOST=socket.gethostbyname(host_name)
ROOT = os.getcwd()

class Ui_Client(object):
    def __init__(self, HOST, PORT, key, save_fol_path = "./Data_client"):
        self.save_fol = save_fol_path
        self.host, self.port = HOST, PORT
        self.key = key
        self.ClientSC = Client(self.host, self.port, key)
        self.isConnect = False
        self.count = 0

    def setupUi(self, Client):
        Client.setObjectName("Client")
        Client.resize(850, 397)
        self.centralwidget = QtWidgets.QWidget(Client)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 851, 121))
        self.frame.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(480, 0, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(110, 0, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 40, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 80, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_2.setObjectName("label_2")
        self.ipclent = QtWidgets.QTextEdit(self.frame)
        self.ipclent.setGeometry(QtCore.QRect(110, 40, 371, 41))
        self.ipclent.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ipclent.setObjectName("ipclent")
        self.ipclent.setText(socket.gethostbyname(socket.gethostname()))

        self.portclient = QtWidgets.QTextEdit(self.frame)
        self.portclient.setGeometry(QtCore.QRect(480, 40, 371, 41))
        self.portclient.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.portclient.setObjectName("portclient")
        self.portclient.setText(str(self.ClientSC.SOURCE_PORT))
        

        self.ipserver = QtWidgets.QTextEdit(self.frame)
        self.ipserver.setGeometry(QtCore.QRect(110, 80, 371, 41))
        self.ipserver.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ipserver.setObjectName("ipserver")
        self.ipserver.setText(socket.gethostbyname(socket.gethostname()))

        self.portserver = QtWidgets.QTextEdit(self.frame)
        self.portserver.setGeometry(QtCore.QRect(480, 80, 371, 41))
        self.portserver.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.portserver.setObjectName("portserver")
        self.portserver.setText(str(self.ClientSC.server_address[1]))

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.B_delete = QtWidgets.QToolButton(self.centralwidget)
        self.B_delete.setGeometry(QtCore.QRect(630, 330, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.B_delete.setFont(font)
        self.B_delete.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.B_delete.setObjectName("B_delete")
        self.B_delete.clicked.connect(self.on_clicked_delete)
        self.B_add = QtWidgets.QToolButton(self.centralwidget)
        self.B_add.setGeometry(QtCore.QRect(90, 330, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.B_add.setFont(font)
        self.B_add.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.B_add.setObjectName("B_add")
        self.B_add.clicked.connect(self.pushButton_handler)
        self.buttonconnect = QtWidgets.QToolButton(self.centralwidget)
        self.buttonconnect.setGeometry(QtCore.QRect(700, 125, 111, 30))
        self.buttondisconnect = QtWidgets.QToolButton(self.centralwidget)
        self.buttondisconnect.setGeometry(QtCore.QRect(700, 155, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonconnect.setFont(font)
        self.buttonconnect.setObjectName("buttonconnect")
        self.buttonconnect.clicked.connect(self.button_clicked)
        self.buttondisconnect.setFont(font)
        self.buttondisconnect.setObjectName("buttondisconnect")
        self.buttondisconnect.clicked.connect(self.button_clicked2)
        self.text_label = QtWidgets.QLabel(self.centralwidget)
        self.text_label.setGeometry(QtCore.QRect(20, 130, 661, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.text_label.setFont(font)
        self.text_label.setObjectName("text_label")
        self.B_refresh = QtWidgets.QToolButton(self.centralwidget)
        self.B_refresh.setGeometry(QtCore.QRect(280, 330, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.B_refresh.setFont(font)
        self.B_refresh.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.B_refresh.setObjectName("B_refresh")
        self.B_refresh.clicked.connect(self.update1)
        self.B_refresh_2 = QtWidgets.QToolButton(self.centralwidget)
        self.B_refresh_2.setGeometry(QtCore.QRect(450, 330, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.B_refresh_2.setFont(font)
        self.B_refresh_2.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.B_refresh_2.setObjectName("B_refresh_2")
        self.B_refresh_2.clicked.connect(self.on_clicked_download)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(90, 190, 681, 121))
        self.listView.setObjectName("listView")
        Client.setCentralWidget(self.centralwidget)
        self.retranslateUi(Client)
        QtCore.QMetaObject.connectSlotsByName(Client)

    def retranslateUi(self, Client):
        _translate = QtCore.QCoreApplication.translate
        Client.setWindowTitle(_translate("Client", "MainWindow"))
        self.label_4.setText(_translate("Client", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Port</span></p></body></html>"))
        self.label_3.setText(_translate("Client", "<html><head/><body><p align=\"center\">IP</p></body></html>"))
        self.label.setText(_translate("Client", "<html><head/><body><p align=\"center\">Client</p></body></html>"))
        self.label_2.setText(_translate("Client", "<html><head/><body><p align=\"center\">Server</p></body></html>"))
        self.label_5.setText(_translate("Client", "List file"))
        self.B_delete.setText(_translate("Client", "Delete"))
        self.B_add.setText(_translate("Client", "Add"))
        self.buttonconnect.setToolTip(_translate("Client", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\"><br/></span></p></body></html>"))
        self.buttonconnect.setText(_translate("Client", "Connect"))
        self.buttondisconnect.setToolTip(_translate("Client", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\"><br/></span></p></body></html>"))
        self.buttondisconnect.setText(_translate("Client", "Disconnect"))
        self.text_label.setToolTip(_translate("Client", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\"><br/></span></p></body></html>"))
        self.text_label.setText(_translate("Client", ""))
        self.B_refresh.setText(_translate("Client", "Refresh"))
        self.B_refresh_2.setText(_translate("Client", "Download"))
        self.listView.setToolTip(_translate("Client", ""))
        self.listView.setWhatsThis(_translate("Client", ""))



    values = []
    def get_list(self):
        client = self.ClientSC
        client.sendInt(OPTIONS["GET_LIST"]) # send option 1
        list_data = client.recv_data(HEADER)
        return convByteToList1D(list_data,"|")
    # cap nhat list view
    def update_list(self):
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        for i in self.values:
            self.model.appendRow(QStandardItem(i))

    def button_clicked(self):
        # get port client
        portclient = self.portclient.toPlainText()
        #get ip server
        ipserver = self.ipserver.toPlainText()
        # get port server
        portserver = self.portserver.toPlainText()
        try:
            portserver = int(portserver)
        except:
            # print("Server port isn't interger")
            self.text_label.setText("Server port isn't interger")
            return
        if not self.isConnect:
            self.ClientSC = Client(self.host, self.port, self.key)
            self.ClientSC.SOURCE_PORT+= self.count
            self.ClientSC.server_address = (ipserver, portserver)
            self.portclient.setText(str(self.ClientSC.SOURCE_PORT))
            self.ClientSC.connect()
            self.isConnect = True
            # cap nhat thanh cong
            self.update1()
            self.text_label.setText("Connect successfully :  " + str(ipserver) + " : " + str(portserver))   
        else:
            # print("Client is connecting to another network!")
            self.text_label.setText("Client is connecting to another network!")
        self.update()

    def button_clicked2(self):
        if self.isConnect:
            self.ClientSC.sendInt(OPTIONS["EXIT"])
            self.ClientSC.s.shutdown(socket.SHUT_RDWR)
            self.ClientSC.s.close()
            self.text_label.setText("Disconnected")
            self.isConnect = False
        else:
            # print("Client is not connected")
            self.text_label.setText("Client is not connected")
        self.update()

    # Cap nhap lai label
    def update(self):
        self.text_label.adjustSize()
    def pushButton_handler(self):
        self.open_dialog_box()
    
    def update1 (self):
        if self.isConnect:
            self.values = self.get_list()
            self.update_list()
            # print("Update list successfully")
            self.text_label.setText("Update list successfully")
        else:
            self.text_label.setText("Client is not connected")
            # print("Client is not connected")
        self.update()
     
    def open_dialog_box(self):
        if self.isConnect:
            filename = QFileDialog.getOpenFileName()
            path = filename[0]
            if(path == ''):
                return
            basename = os.path.basename(path)
            self.values = self.values + [basename]
            client = self.ClientSC
            client.sendInt(OPTIONS["PUSH_FILE"])
            client.sendFileName(basename)
            client.sendFile(path)
            status = client.recvInt()
            self.update1() # update list
            # print(STATUS[status])
            self.text_label.setText(STATUS[status])
        else:
            self.text_label.setText("Client is not connected")
            # print("")
        self.update()

    def on_clicked_download(self):
        if self.isConnect:
            row = self.listView.currentIndex().row()
            client = self.ClientSC
            client.sendInt(OPTIONS["DOWNLOAD_FILE"])
            client.sendFileName(self.values[row])
            status = client.recvInt()
            if (status == 2):
                f_name = self.values[row]
                data = client.recv_data(HEADER)
                # print(f"Downloaded ({len(data)} bytes)")
                
                save_path = self.save_fol + "/" + f_name
                st = saveData(save_path, data)
                self.text_label.setText(f"Downloaded:{f_name} ({len(data)} bytes). \n{STATUS[st]}")
                # print(STATUS[st])
            elif (status == 3):
                self.text_label.setText(STATUS[status])
                # print(STATUS[status])
        else:
            self.text_label.setText("Client is not connected")
        self.update()

    def on_clicked_delete(self, index):
        if self.isConnect:
            row = self.listView.currentIndex().row()
            client = self.ClientSC
            if(0<=row<=len(self.values)):
                client.sendInt(OPTIONS["DELETE_FILE"])
                file_name = self.values[row]
                client.sendFileName(file_name)
                status = client.recvInt()
                self.update1() #update list
                if (status == 2):
                    # print(STATUS[status])
                    self.text_label.setText(STATUS[status])
                elif (status == 3):
                    # print(STATUS[status])
                    self.text_label.setText(STATUS[status])
                elif(status == 0):
                    self.text_label.setText("Deleted file: "+ file_name)
            else:
                # print("Error")
                self.text_label.setText("Error")
        else:
            self.text_label.setText("Client is not connected")
        self.update()

if __name__ == "__main__":
    import sys
    HOST='localhost'
    PORT=8000
    key = b"MMT_CDDMTK"
    fol_save = ROOT+"/Data_client"
    makeDir(fol_save)
    app = QtWidgets.QApplication(sys.argv)
    Cl = QtWidgets.QMainWindow()
    ui = Ui_Client(HOST, PORT, key, fol_save)
    ui.setupUi(Cl)
    Cl.show()
    
    sys.exit(app.exec_())
