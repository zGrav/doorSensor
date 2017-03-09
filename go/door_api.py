#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from time import gmtime, strftime

# GPIO stuff

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

doorSensor = 4
doorStatus = "Door "

GPIO.setup(doorSensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    #while True:
        doorStatus += "open" if GPIO.input(doorSensor) == 1 else "closed"

        #time.sleep(0.1)

        print doorStatus
except (KeyboardInterrupt):
    print "\n CTRL+C"
except Exception as e:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
