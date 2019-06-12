from threading import Thread
import socket

class Server(Thread):
    ''' 
    * CONSTRUCTOR *
    '''
    def __init__(self,ip,port,listen):
        self._ip = ip
        self._port = port
        self._listen = listen
        self._sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    def run(self):
        self._sock.bind((str(self.ip),self.port))
        self._sock.listen(self.listen)
        return self._sock.accept()

    def stop(self):
        self._sock.close()
    ''' 
    * ACCESSEUR MUTATEUR PROPERTIES *
    '''
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


p = Server('0.0.0.0',80,5)
client,conn = p.run()
msg_recv=b""
while msg_recv != b"end":
    msg_recv = client.recv(1024)
    print(msg_recv.decode())
    client.send(b"end")
client.close()
p.stop()
