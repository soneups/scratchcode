# button press test/hack
# Gary Sone
# 17-Dec-2014 1.0 initial POC
#
# Using a big red button on GPIO 18,BRB
# Using two tactile buttons on GPIO 14,TB2 & GPIO 15,TB1
#
# HT - http://razzpisampler.oreilly.com/ch07.html
# HT - https://energenie4u.co.uk/res/software/ENER002-2PI.py
# HT - https://energenie4u.co.uk/res/pdfs/ENER314%20UM.pdf
#
# Source - https://github.com/soneups/CamJamMeEduKit2/blob/master/BRB/autorun2.py
# RealSource - https://raw.githubusercontent.com/soneups/CamJamMeEduKit2/master/BRB/autorun2.py
#

# add to  /etc/rc.local
#
#import libraries
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #Set the GPIO pin naming mode
#GPIO.setwarnings(False)

# Give the GPIO buttons a meaningful name!
BRB = 21 # was 18 (black)
TB1 = 20 # was 15 (white)
TB2 = 16 # was 14 (green)
GPIO.setup(BRB,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(TB1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(TB2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(24,GPIO.IN)

#os.system('clear')

#while True:
#	print "TB1:"+str(GPIO.input(TB1)) +" TB2:"+str(GPIO.input(TB2))+" BRB:"+str(GPIO.input(BRB))

#while True:
#    input_state = GPIO.input(BRB)
#    if input_state == False:
#        print('Button Pressed')
#        time.sleep(0.2)
#        os.system('clear')
#        #subprocess.call("sudo halt", shell=True)
#        os.system("echo 'BRB: system shutdown has been initiated.' | wall")
#        os.system("sudo halt")
#        time.sleep(1)

def BRBEventHandler (channel):
  print "BRB: system shutdown has been initiated."
  os.system("echo 'BRB: system shutdown has been initiated.' | wall")
  os.system("sudo halt")
  time.sleep(1)


#def TB1EventHandler (pin):
#    print "TB1: You just pressed the 1st tactile button!"
    
#def TB2EventHandler (pin):
#    print "TB2: TB1: You just pressed the 2nd tactile button!"

#def main():
#  # tell the GPIO library to look out for an event on pin <BRB> and deal with it by calling the (appropiate) function
#  GPIO.wait_for_edge(BRB, GPIO.RISING)
GPIO.add_event_detect(BRB,GPIO.FALLING,callback=BRBEventHandler, bouncetime=300)
#  GPIO.add_event_callback(BRB,BRBEventHandler)

#while True:
#        time.sleep(0.2)

#GPIO.cleanup()

#if __name__=="__main__":
#    main()

try:  
    print "Waiting for rising edge on port BRB"  
    GPIO.wait_for_edge(24, GPIO.RISING)  
    print "Rising edge detected on port 24. Here endeth the third lesson."  
  
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit 
