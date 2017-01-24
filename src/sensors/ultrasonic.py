import RPi.GPIO as GPIO
import time
from Event import Event

class Ultrasonic:
    @classmethod
    def __init__(self, TRIG, ECHO, Mode):
        self.__trig = TRIG
        self.__echo = ECHO
        GPIO.setmode(Mode)
        GPIO.setup(self.__trig, GPIO.OUT)
        GPIO.setup(self.__echo, GPIO.IN)
        self.gotData = Event()

    @classmethod
    def watchforData(self):
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

#Ultrasonic.gotData += function(distance) to catch the event
