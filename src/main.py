import RPi.GPIO as GPIO

class MoterManager:
    def __init__(self, in1Pin, in2Pin):
        self.__in1Pin = in1Pin
        self.__in2Pin = in2Pin

    def stop(self):
        self.__offIn1()
        self.__offIn2()

    def brake(self):
        elf.__onIn1()
        self.__onIn2()

    def rotateClockwise(self):
        self.__onIn1()
        self.__offIn2()

    def rotateCounterClockwise(self):
        self.__offIn1()
        self.__onIn2()

    def __onIn1(self):
        GPIO.output( self.__in1Pin, True)
        print "In1 on"

    def __onIn2(self):
        GPIO.output( self.__in2Pin, True)
        print "In2 on"

    def __offIn1(self):
        GPIO.output( self.__in1Pin, False )
        print "In1 off"

    def __offIn2(self):
        GPIO.output( self.__in2Pin, False )
        print "In2 off"
