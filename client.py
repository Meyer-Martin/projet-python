import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 80))
s.send(b"Je m'appelle Martin")
# msg = input("Commande que vous voulez executer:")
# s.send(msg.encode())
# r = s.recv(2048)
# print(r)
info = input("1: pour recevoir l IP \n 2: pour recevoir le port \n 3: pour interompre la connection \n >> ")
s.send(info.encode())
while True:
    r = s.recv(2048)
    print (r.decode()) 
 



# #!/usr/bin/env python3

# import socket
# import threading

# HOST = '127.0.0.1'
# PORT = 80

# class MonThread (threading.Thread):
#     def __init__(self, jusqua):
#         threading.Thread.__init__(self)
#         self.jusqua = jusqua

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'Je suis connecter, je mappelle Martin')
# *
#     # m = MonThread(1)
#     #  m2 = MonThread(2)   
#     #  m.start()     
#     # while s.recv(1024) == 0 : 
#     #     break
#     # else :  
#     #     s.recv(1024)
#     # m2.start()
#     message = input('')
#     s.sendall(message.encode())

# print('Received', repr(data))