import unittest
from ctypes import CDLL, c_float, c_int, c_bool
from main import calc_runtime

sensor = CDLL('./hardware.so')
sensor.fahrenheitToCelsius.restype = c_float
sensor.setKachel.restype = c_float
sensor.getKachelStatus.restype = c_bool

class integration_test(unittest.TestCase):
    @calc_runtime
    def test_set_kachel_on(self):
        temperature = round(sensor.fahrenheitToCelsius(c_float(67.1)),1) #19.5 C
        round(sensor.setKachel(c_float(temperature)),1)
        result = sensor.getKachelStatus()
        self.assertEqual(result, True, "Het resultaat moet True zijn!")

if __name__ == '__main__':
    unittest.main()