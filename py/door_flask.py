#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from time import gmtime, strftime
from flask import Flask
from flask import jsonify

try:
        # Flask stuff

        app = Flask(__name__)

        @app.route('/api/getDoorStatus', methods=['GET'])
        def get_sensor():
            # GPIO stuff

            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)

            name = "ADENTIS RaspberryPi 3 Model B located somewhere"
            doorSensor = 4
            doorStatus = "Door "

            GPIO.setup(doorSensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

            doorStatus += "open" if GPIO.input(doorSensor) == 1 else "closed"
            print doorStatus

            data = [{'name': name, 'status': doorStatus}]
            return jsonify(data)

        if __name__ == '__main__':
            app.run(host='0.0.0.0',port=80)

except (KeyboardInterrupt):
    print "\n CTRL+C"
except Exception as e:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
