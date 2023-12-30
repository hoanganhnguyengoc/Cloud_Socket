# -*- coding: utf-8 -*-

import os
from utilz.method import *
from utilz.constant import *
from utilz.RC4 import *
from utilz.Server import Server
import threading 
import socket
ROOT = os.getcwd()
dataPath  = ROOT+"/Data"
dataRawPath  = ROOT+"/Data_Raw"
makeDir(dataPath)
makeDir(dataRawPath)
HOST=socket.gethostbyname(socket.gethostname())
PORT=8000
key = b"MMT_CDDMTK"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
import time


def connect(sc):
    print("Waiting...")
    while True:
        try: 
            client, addr = sc.accept()
            print('Connected by', addr)
            break
        except:
            print("Listen to client...")
            time.sleep(0.5)
    return client, addr

def run(server):
    while True:
        option = server.recvInt()
        if (option == OPTIONS["GET_LIST"]):
            server.sendListOfData(dataPath)
        if (option == OPTIONS["PUSH_FILE"]):
            file_name = server.recv_data(HEADER).decode("utf8")
            data_raw = server.recv_raw_data(HEADER)
            data = dec(server.key, data_raw)

            file_path = dataPath+"/"+file_name
            file_raw_path = dataRawPath+"/"+file_name
            status = saveData(file_raw_path, data_raw)
            status = saveData(file_path, data)
            server.sendInt(status) # status feedback
        elif (option == OPTIONS["DOWNLOAD_FILE"]):
            file_name = server.recv_data(HEADER).decode("utf8")
            full_path = dataPath + "/" + file_name
            
            if os.path.isfile(full_path): # check file
                status = 2
            else: status = 3
            server.sendInt(status) # send status
            
            if status == 2: # send file
                server.sendFile(full_path)
        elif option == OPTIONS["DELETE_FILE"]:
            file_name = server.recv_data(HEADER).decode("utf8")
            full_path = dataPath + "/" + file_name
            
            if os.path.isfile(full_path): # check file
                os.remove(full_path)
                print("Deleted")
                status = 0
            else: status = 3
            server.sendInt(status) # send status

        elif(option == 5):
            # create a thread to listen new client
            print("Closed a client")
            server.close()
            break
        elif(option == 1000000): # fix some errors of option 3
            continue

print(f"Server address: {HOST} : {PORT}")
while True:
    client, addr = connect(s)
    ser = Server(client, addr, key)
    thread = threading.Thread(target=run, args=(ser,))
    thread.start()
    print(f"[ACTIVE CONNECTIONS {threading.activeCount() - 1}]")









