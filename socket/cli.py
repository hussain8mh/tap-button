import socket
import sys
import logging
                
s = socket.socket()          

port = 1235               
server_ip = sys.argv[1]

s.connect((server_ip, port)) 

command = raw_input("Command ")
s.send(command)

logging.info("Command " , command , " sent")
s.close()  
