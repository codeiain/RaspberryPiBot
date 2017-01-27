import imp
try:
    imp.find_module('RPi.GPIO')
    found = True
    import RPi.GPIO as GPIO
except ImportError:
    found = False
    print 'not found'
    import _RPi.GPIO as GPIO


class Motor:
    
    def __init__(self,pin1,pin2,mode):
        """

        """
        self._pin1 = pin1
        self._pin2 = pin2
        GPIO.setmode(mode)
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        set("delayed", "0")
        set("mode", "pwm")
        set("frequency", "500")
        set("active", "1")

    def set(property, value):
        try:
            f = open("/sys/class/rpi-pwn/pwm0/"+ property, 'w')
            f.write(value)
            f.close()
        except:
            return "Error writing to: " + property + " value: "+ValueError

    def clockwise(self):
        """
        runs the motor clockwise
        :return:
        """
        GPIO.output(self._pin1, True)    
        GPIO.output(self._pin2, False)

    def counter_clockwise(self):
        """
        runs the motor counter clockwise
        :return:
        """
        GPIO.output( self._pin1, False)    
        GPIO.output(self._pin2, True)
    
    def set_speed(self, value):
        """
        sets the motors speed
        :param value:
        :return:
        """
        if value < 0 and value > 9:
            return "speed must be between 0 and 9"
        else:
            speed = int (value) * 11
            set("duty", str(speed))