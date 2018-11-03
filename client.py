import socket
class Client():
    def __init__(self , server_ip  , port ):
        self.s = socket.socket()
        self.s.connect((server_ip, port)) 
    
    def send(self,command):
        self.s.send(command)
    
    def recv(self):
        return self.s.recv()

    def close(self):
        self.s.close()
