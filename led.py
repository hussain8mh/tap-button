import RPi.GPIO as GPIO
import time

BUTTON = 23 
CLICK_CONSTANT =  0.3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)


s = e = 0.0

def print_util(content):
	print content

#when button is pressed  button state is false
while True:
  button_state =GPIO.input(BUTTON)
#  print "Button state " , button_state

# This Condition is true when button is NOT pressed
  if button_state ==  True:

	pressed_time = e-s
        if pressed_time >=  CLICK_CONSTANT  :
                print_util("right click ")
        elif ( pressed_time < CLICK_CONSTANT and pressed_time > 0):
                print_util("left click ")

        s = time.time() 


# This Condition is true when button IS pressed
  if button_state == False:
        e = time.time()

  #to mitigate human errors in pressing

  time.sleep(0.1)

