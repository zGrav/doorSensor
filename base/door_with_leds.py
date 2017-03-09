#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from time import gmtime, strftime

# GPIO stuff

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

greenLED = 19
redLED = 26
doorSensor = 4
doorStatus = ""

GPIO.setup(doorSensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    #while True:
        if (GPIO.input(doorSensor) == 1):
            GPIO.setup(redLED,GPIO.OUT)
            GPIO.output(redLED,GPIO.LOW)
            GPIO.setup(greenLED,GPIO.OUT)
            GPIO.output(greenLED,GPIO.HIGH)
            doorStatus = "Door open"
        elif (GPIO.input(doorSensor) == 0):
            GPIO.setup(redLED,GPIO.OUT)
            GPIO.output(redLED,GPIO.HIGH)
            GPIO.setup(greenLED,GPIO.OUT)
            GPIO.output(greenLED,GPIO.LOW)
            doorStatus = "Door closed"

        #time.sleep(0.1)

        print "GPIO doorStatus: " + doorStatus
except (KeyboardInterrupt):
    print "\n CTRL+C"
except:
    print strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - Caught exception, restarting!"
    GPIO.cleanup()
finally:
    GPIO.cleanup()
