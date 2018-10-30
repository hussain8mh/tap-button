import RPi.GPIO as GPIO
import time
BUTTON = 23 
LED = 24
CLICK_CONSTANT =  0.3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def left_click(button_state):
  if button_state == False:
    GPIO.output(LED,True)
  else:
    GPIO.output(LED,False)

s = e = 0.0

#when button is pressed  button state is false
while True:
  button_state =GPIO.input(BUTTON)
#  print "Button state " , button_state

#  time.sleep(0.1)
#  left_click(button_state)

 
  if button_state ==  True:
        if e - s >=  CLICK_CONSTANT  :
                print "right click"
        elif (e - s < CLICK_CONSTANT and e-s > 0):
                print "left click"

        s = time.time() 
  if button_state == False:
        e = time.time()

  #to mitigate human errors in pressing
  time.sleep(0.01)

