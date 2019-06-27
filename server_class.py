import socket
import threading

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 
   
        print("Connexion de %s %s" % (self.ip, self.port, ))
        while True:
            r = self.clientsocket.recv(2048)
            print(r.decode())

            if r.decode() == "1":

                print("envoie de l IP")
                clientsocket.send(str(self._get_ip()).encode())


            if r.decode() == "3":
                
                print("end")
                clientsocket.send(b"end")
                clientsocket.close()
                #r = ""
                break

            #elif r != 3:
            #    s.send(b"NON")

    def _get_ip(self):
        return self._ip
    def _set_ip(self,ip):
        self._ip=ip
    ip = property(_get_ip,_set_ip)

    def _get_port(self):
        return self._port
    def _set_port(self,port):
        self._port=port
    port = property(_get_port,_set_port)

    def _get_listen(self):
        return self._listen
    def _set_listen(self,listen):
        self._listen = listen
    listen = property(_get_listen,_set_listen)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1",80))

while True:
    s.listen(80)
    print( "En écoute...")
    (clientsocket, (ip, port)) = s.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()



# from threading import Thread
# import socket

# class Server(Thread):
#     ''' 
#     * CONSTRUCTOR *
#     '''
#     def __init__(self,ip,port,listen):
#         self._ip = ip
#         self._port = port
#         self._listen = listen
#         self._sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
#     def run(self):
#         self._sock.bind((str(self.ip),self.port))
#         self._sock.listen(self.listen)
#         return self._sock.accept()

#     def stop(self):
#         self._sock.close()
#     ''' 
#     * ACCESSEUR MUTATEUR PROPERTIES *
#     '''
#     def _get_ip(self):
#         return self._ip
#     def _set_ip(self,ip):
#         self._ip=ip
#     ip = property(_get_ip,_set_ip)

#     def _get_port(self):
#         return self._port
#     def _set_port(self,port):
#         self._port=port
#     port = property(_get_port,_set_port)

#     def _get_listen(self):
#         return self._listen
#     def _set_listen(self,listen):
#         self._listen = listen
#     listen = property(_get_listen,_set_listen)


# p = Server('127.0.0.1',80,5)
# client,conn = p.run()
# msg_recv=b""
# while msg_recv != b"end":
#     msg_recv = client.recv(1024)
#     print(msg_recv.decode())
#     if msg_recv == b"end":
#         client.send(b"end")
#         client.close()
#         p.stop()