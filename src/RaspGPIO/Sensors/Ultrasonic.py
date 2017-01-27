import imp
try:
    imp.find_module('RPi.GPIO')
    found = True
    import RPi.GPIO as GPIO
except ImportError:
    found = False
    print 'not found'
    import _RPi.GPIO as GPIO

import threading
import time
from RaspGPIO.Event import Event

# https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
# Modified from the above example

class Ultrasonic:

    @classmethod
    def __init__(self, TRIG, ECHO, Mode):
        self.__trig = TRIG
        self.__echo = ECHO
        GPIO.setmode(Mode)
        GPIO.setup(self.__trig, GPIO.OUT)
        GPIO.setup(self.__echo, GPIO.IN)
        self.gotData = Event()
        thread = threading.Thread(target=self.watchforData, args=())
        thread.daemon = False                           
        thread.start()                                  

    @classmethod
    def watchforData(self):
        """ 
        Method that runs forever and watches for data from the Ultrasonic sensor 
        Ultrasonic.gotData += function(distance) to catch the event
        """
        while True:
            GPIO.output(self.__trig, True)
            time.sleep(0.00001)
            GPIO.output(self.__trig, False)
            while GPIO.input(ECHO)==0:
                pulse_start = time.time()

            while GPIO.input(ECHO)==1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance, 2)
            self.gotData(distance)

# Ultrasonic.gotData += function(distance) to catch the event
