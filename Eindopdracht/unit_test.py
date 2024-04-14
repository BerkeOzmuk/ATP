import unittest
from ctypes import CDLL, c_float, c_int
from main import calc_runtime

sensor = CDLL('./hardware.so')
sensor.fahrenheitToCelsius.restype = c_float

class unit_test(unittest.TestCase):
    @calc_runtime
    def test_fahrenheit_to_celsius1(self):
        result = round(sensor.fahrenheitToCelsius(c_float(70.0)),1)
        self.assertEqual(result, 21.1, "Het resultaat moet 21.1 zijn!")

    @calc_runtime
    def test_fahrenheit_to_celsius2(self):
        result = round(sensor.fahrenheitToCelsius(c_float(75.0)),1)
        self.assertEqual(result, 23.9, "Het resultaat moet 23.9 zijn!")
    
    @calc_runtime    
    def test_fahrenheit_to_celsius3(self):
        result = round(sensor.fahrenheitToCelsius(c_float(80.0)),1)
        self.assertEqual(result, 26.7, "Het resultaat moet 26.7 zijn!")

if __name__ == '__main__':
    unittest.main()