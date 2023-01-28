import battery
import solar_array
import motor

import time
import datetime

import numpy as np

from track import Track
class Car:
    def __init__(self, track: Track, time: int) -> None:
        max_capacity = 5400 # Wh
        self.lon, self.lat = track.coords
        self.temperature = 25 #update
        self.time = time
        
        self.battery = battery.Battery(max_capacity)
        self.array = solar_array.Array(self, self.temperature)
        self.motor = motor.Motor()

    def drive(self, speed, slope, time):
        print("Car is driving")
        deltaTime = time - self.time
        
        arrayPower = self.array.get_power()
        electronicsPower = 77 #power draw from constantly used systems
        
        self.motor.updateParameters(speed, slope, time)
        motorPower = self.motor.getCurrent() * 96 #no clue what the voltage of the battery is
        if motorPower < 0:
            motorPower = 0

        used_power = (arrayPower - electronicsPower - motorPower)*deltaTime/3600 # Wh
        
        self.battery.update(used_power)
        print("Motor Power: " + str(motorPower) + " W")
        print("Battery: " + str(self.battery.get_capacity()) + " Wh")
        self.time = time

        return speed * deltaTime * np.cos(slope)
        
if __name__ == "__main__":
    t = Track("track2.json")
    car = Car(t, datetime.datetime(2023, 1, 10, 9, 0, 0).timestamp())
    i = 0
    while True:
        car.drive(10, 0, i)
        i += 1
        time.sleep(1)