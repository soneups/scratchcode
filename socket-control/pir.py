#!/usr/bin/python
# this file - https://github.com/soneups/CamJamMeEduKit2/raw/master/Kit2/KIT2_WS5.py
# Edukit2 - Worksheet #5 - 
# Import Python header files
import RPi.GPIO as GPIO
import time
import urllib
# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set a variable to hold the GPIO Pin identity
PinPIR = 17
print "PIR Module Test (CTRL-C to exit)"
# Set pin as input
GPIO.setup(PinPIR, GPIO.IN)
# Variables to hold the current and last states
Current_State = 0
Previous_State = 0
try:
  print "Waiting for PIR to settle ..."
  # Loop until PIR output is 0
  while GPIO.input(PinPIR)==1:
    Current_State = 0
  print " Ready"
  # Loop until users quits with CTRL-C
  while True:
    # Read PIR state
    Current_State = GPIO.input(PinPIR)
    # If the PIR is triggered
    if Current_State==1 and Previous_State==0:
      print " "+(time.strftime("%H:%M:%S"))+" - Motion detected!"
      a = urllib.urlopen('http://192.168.1.97/4/1')
      # Record previous state
      Previous_State=1
    # If the PIR has returned to ready state
    elif Current_State==0 and Previous_State==1:
      print " Ready"
      Previous_State=0
    # Wait for 10 milliseconds
    time.sleep(0.01)
except KeyboardInterrupt:
  print " Quit"
  # Reset GPIO settings
  GPIO.cleanup()
