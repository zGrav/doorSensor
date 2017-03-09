#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from time import gmtime, strftime
import paho.mqtt.client as mqtt
import sys

# MQTT stuff

broker = "broker.hivemq.com"
pub_path = "/adentis/doorStatus"

def on_connect(client, userdata, flags, rc):
    if rc != 0:
        sys.exit(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - Bad response code, exiting!")

    print strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - " + "Listening on broker: " + broker + " and pub_path " + pub_path + " for MQTT messages"
    client.subscribe(pub_path)

def on_message(client, userdata, msg):
    print str(msg.payload)

try:
    client = mqtt.Client()
    client.connect_async(broker, 1883, 3600)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()
except (KeyboardInterrupt):
    print "\n CTRL+C"
except Exception as e:
    sys.exit(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " " + str(e) + " - Caught exception, exiting!")
finally:
    print strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " - Clean disconnect from broker: " + broker + " and pub_path " + pub_path + " , no longer receiving MQTT messages."
    client.disconnect()
