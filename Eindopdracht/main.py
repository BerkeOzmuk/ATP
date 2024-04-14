from datetime import datetime
from ctypes import CDLL, c_float, c_int, c_bool
import time

sensor = CDLL('./hardware.so')
sensor.readTemperature.restype = c_float
sensor.readCO2.restype = c_int
sensor.fahrenheitToCelsius.restype = c_float
sensor.setKachel.restype = c_float
sensor.setKachel.restype = c_float
sensor.setServo.restype = c_int
sensor.getKachelStatus.restype = c_bool


def calc_runtime(f):
    def wrapper(*args, **kwargs):
        start_timer = datetime.now()
        x = f(*args, **kwargs)
        print("{} runtime: {} seconds".format(f.__name__, datetime.now() - start_timer))
        return x
    return wrapper

if __name__ == "__main__":
    while True:
        temperature = round(sensor.readTemperature())
        print("Temperatuur: ", temperature)
        print("-" * 20)
        time.sleep(2)
        CO2 = sensor.readCO2()
        print("CO2: ", CO2)
        print("-" * 20)
        time.sleep(2) 
        ventilatorKachel = round(sensor.setKachel(c_float(temperature)),1)
        time.sleep(2)
        servo = sensor.setServo(c_int(CO2))
        time.sleep(2)

