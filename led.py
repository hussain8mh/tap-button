import RPi.GPIO as GPIO
import time 
import sys
from client import Client

server_ip = sys.argv[1]
port = sys.argv[2]

client_handle = Client(server_ip , port)

BUTTON = 23 
CLICK_CONSTANT =  0.3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)
s = e = 0.0




#when button is pressed  button state is false
while True:
  button_state =GPIO.input(BUTTON)
#  print "Button state " , button_state

# This Condition is true when button is NOT pressed
  if button_state ==  True:
        pressed_time = e-s
        if pressed_time >=  CLICK_CONSTANT  :
                client_handle.send("right")
        elif ( pressed_time < CLICK_CONSTANT and pressed_time > 0):
                client_handle.send("left")

        s = time.time() 

# This Condition is true when button IS pressed
  if button_state == False:
        e = time.time()

  #to mitigate human errors in pressing

  time.sleep(0.1)

