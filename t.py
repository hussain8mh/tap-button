import RPi.GPIO as GPIO
import time
import socket                
s = socket.socket()          

port = 1235               
server_ip = '192.168.43.158'
BUTTON = 23 
CLICK_CONSTANT =  0.3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)
s.connect((server_ip, port)) 


st = e = 0.0

def print_util(content):
	print content
    

#when button is pressed  button state is false
while True:
  button_state =GPIO.input(BUTTON)
#  print "Button state " , button_state

# This Condition is true when button is NOT pressed
  if button_state ==  True:

	pressed_time = e-st
        if pressed_time >=  CLICK_CONSTANT  :
                print_util("right click ")
                s.send("right")
        elif ( pressed_time < CLICK_CONSTANT and pressed_time > 0):
                print_util("left click ")
                s.send("left")
        st = time.time() 
#	print s.recv(1024) 

# This Condition is true when button IS pressed
  if button_state == False:
        e = time.time()

  #to mitigate human errors in pressing

  time.sleep(0.1)

s.close()
