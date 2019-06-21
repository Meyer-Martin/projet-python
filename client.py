#!/usr/bin/env python3

import socket
import threading

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 80           # The port used by the server

class MonThread (threading.Thread):
    def __init__(self, jusqua):
        threading.Thread.__init__(self)
        self.jusqua = jusqua
        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Je suis connecter, je mappelle Martin')

    m = MonThread(1)     # crée le thread
    m.start()                  # démarre le thread,
    while s.recv(1024) == 0 : 
        break
    else :  
        s.recv(1024)

    m2 = MonThread(2)
    m2.start()    

    message = input('')
    s.sendall(message.encode())

print('Received', repr(data))