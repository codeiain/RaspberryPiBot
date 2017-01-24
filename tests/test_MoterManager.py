import unittest

import sys
sys.path.append('..\src')
from main import MoterManager

class TestMoterManager(unittest.TestCase):
    in1Pin=67
    in2Pin=68

    def test_init(self):
        mm = MoterManager(self.in1Pin,self.in1Pin)
        self.assertEquals(1,1)

    def test_stop(self):
        mm = MoterManager(self.in1Pin,self.in1Pin)
        self.assertEquals(1,1)

    def test_brake(self):
        mm = MoterManager(self.in1Pin,self.in1Pin)
        self.assertEquals(1,1)

    def test_rotateClockwise(self):
        mm = MoterManager(self.in1Pin,self.in1Pin)
        self.assertEquals(1,1)

    def test_rotateCounterClockwise(self):
        mm = MoterManager(self.in1Pin,self.in1Pin)
        self.assertEquals(1,1)