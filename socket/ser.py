
# first of all import the socket library 
import socket                
import util
# next create a socket object 
s = socket.socket()          
print "Socket successfully created"

port = 1235               
s.bind(('', port))         
print "socket binded to %s" %(port) 
  
# put the socket into listening mode 
s.listen(5)      
print "socket is listening"            
c, addr = s.accept()      
print 'Got connection from', addr 

try :
    while True: 
        command = c.recv(1024)
        print "Command recv ",command

        if command == "close":
                c.close() 
                break

        util.handle_command(command)

except:
    c.close() 
