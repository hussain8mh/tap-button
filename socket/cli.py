import socket
import sys
                
s = socket.socket()          

port = 1235               
server_ip = sys.argv[1]

s.connect((server_ip, port)) 

command = raw_input("Command ")
s.send(command)
print s.recv(1024) 

s.close()  
