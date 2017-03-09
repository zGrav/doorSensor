#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from time import gmtime, strftime
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

# MQTT stuff

broker = "broker.hivemq.com"
pub_path = "/adentis/doorStatus"

def on_connect(client, userdata, flags, rc):
    if rc != 0:
        sys.exit(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - Bad response code, exiting!")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker, 1883, 3600)

# GPIO stuff

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

name = "ADENTIS RaspberryPi 3 Model B located somewhere"
doorSensor = 4
doorStatus = "Door "

GPIO.setup(doorSensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "Script called at " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " , fetching status and publishing to MQTT to broker: " + broker + " and pub_path " + pub_path + "!"

try:
    #while True:
        doorStatus += "open" if GPIO.input(doorSensor) == 1 else "closed"

        #time.sleep(0.1)

        print "GPIO doorStatus: " + doorStatus
        client.publish(pub_path, strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - " + name + " - doorStatus: " + doorStatus)
        print "Published GPIO doorStatus: " + doorStatus + " to broker: " + broker + " and pub_path " + pub_path
except (KeyboardInterrupt):
    print "\n CTRL+C"
except Exception as e:
    GPIO.cleanup()
    sys.exit(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " " + str(e) + " - Caught exception, exiting!")
finally:
    GPIO.cleanup()
