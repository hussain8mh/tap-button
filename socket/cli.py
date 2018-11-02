import socket                
s = socket.socket()          

port = 1235               
server_ip = '127.0.0.1'

s.connect((server_ip, port)) 

command = raw_input("Command ")
s.send(command)
print s.recv(1024) 

s.close()  
