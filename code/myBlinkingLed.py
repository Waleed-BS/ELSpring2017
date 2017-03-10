import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

print "PRESS CTRL+C TO QUIT THE INFINITE LOOP"

def Blink():
 
 for i in range(0,3):
	print "blink #" + str(i + 1)
        GPIO.output(18,True)
        time.sleep(0.1)
        GPIO.output(18,False)
        time.sleep(0.1)
 time.sleep(1)

 for i in range(0,4):
	print "blink #" + str(i + 1) 
        GPIO.output(18,True)
        time.sleep(0.1)
        GPIO.output(18,False)
        time.sleep(0.1)	
 time.sleep(1)
 	
while True:
	
 	  Blink()
	  
	

print "done!!"
GPIO.cleanup()

