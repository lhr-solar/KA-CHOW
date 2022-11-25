from lib2to3.pgen2.pgen import DFAState
from logging.handlers import DEFAULT_HTTP_LOGGING_PORT
from multiprocessing.dummy import Array
#mechanical
import aeroshell
import dynamics
#electronics, array, mottor 
import array
import electronics
import motor
import weather

import battery_pack
import battery_module
# model of the solar car

#notes: the car class doesnt necessarily provide recommendations as to what to change
# it instead creates objects of each of the subclasses and depending on the return values 
# for the functions inside these subclasses, it passes them as parameters to other subclasses
# example: all energyloss/energygain from array, electronics, and motor needs to be converted to current, summed up, 
# and then passed as a parameter to the battery module to calculate the power of the battery

class Car:
    #batteryCharge = 100
    #voltageOfASingleCell = 80 #to be removed later

    def __init__(self, speed, time, slope, batteryCharge, voltageOfaSingeCell):
        self.batteryCharge = batteryCharge
        self.time = time
        self.voltageOfaSingeCell = voltageOfaSingeCell
        #aero = aeroshell(speed, 45, 1.225, 45, (speed*time))
        mot = motor.Motor(speed, slope)
        arr = array()
        elec = electronics.Electronics()
        self.electronics_current = elec.run()
        #need to return the get power as well. Aaron did it different than everyone else
        self.motor_current = mot.currentMotor()
        ArrayVoltage = self.voltageOfASingleCell*242
        self.currentFromArray = arr/ArrayVoltage

        self.total_current = self.motor_current + self.electronics_current - self.currentFromArray


    def drive(self):
        batteryPack = battery_pack.BatteryPack(self.batteryCharge,self.total_current)
        batteryPack.updateModuleInternalResistance()
        #I guess this needs to be done?
        self.batteryCharge -= batteryPack.LostCapacity(self.time, self.batteryCharge) #is batteryCharge the same thing as capactiy?
        return self.batteryCharge

#main function to test the simulator for one set of inputs
def main():
    solar_mcqueen = Car(20,20,0,100,80)
    solar_mcqueen.drive()
    print(solar_mcqueen)

if __name__=="__main__":
    main()