import unittest
from ctypes import CDLL, c_float, c_int
from main import calc_runtime

sensor = CDLL('./hardware.so')
sensor.fahrenheitToCelsius.restype = c_float
sensor.setKachel.restype = c_float

class system_test(unittest.TestCase):
    @calc_runtime
    def test_set_kachel_on_off(self):
        temperature = round(sensor.fahrenheitToCelsius(c_float(67.1)),1) #19.5 C
        result = round(sensor.setKachel(c_float(temperature)),1)
        while sensor.getKachelStatus():
            result = round(sensor.setKachel(c_float(result)),1)
        self.assertEqual(result, 20.0, "Het resultaat moet 20.0 zijn!")

if __name__ == '__main__':
    unittest.main()      