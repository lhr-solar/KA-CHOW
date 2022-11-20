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
    batteryCharge = 100
    voltageOfASingleCell = 80 #to be removed later

    def __init__(self, speed, time):
        aero = aeroshell(speed, 45, 1.225, 45, (speed*time))
        dynam = dynamics(1000, 0.4, 0.7 )
        batteryPack = battery_pack(self.batteryCharge, 0)


    
    def drive(self, speed, time):
       
        array = array(self.weather)
        ArrayVoltage = self.voltageOfASingleCell*242

        def __init__(self, velocity, referenceArea, mediumDensity, dragCoefficient, distance):

        # simulate mechanical losses

            #simulating losses from aeroshell
            
            totalMechLoss = self.aero.energyLostv1(self.aero.dr)

            #simulating energy loss from dynamics (assuming it would also return energyloss in joules)
            #code below will need to be altered once dynamics subclass is finished
            
            totalMechLoss += self.dynam.energyLost()#get energyLoss


        # simulate electronics, array, and motor losses to figure out current provided/requested
            
            #simulating losses from the array 
            #some function to return power
            #convert power to current (power/voltage = current)
            
            #for now array is assumed to be a constant value, need the array subsystem to give algorithm/formula to calculate voltage
            array = array(self.weather)
            currentFromArray = array.get_power()/ArrayVoltage
            
            #do the same for electronics and motor            
           


        # simulate battery losses/gains 
            
            batteryPack.updateModuleInternalResistance()
            batteryCharge -= batteryPack.LostCapacity(0, 0)
        # provide CAN outputs (it will depend on what race strategies will end up looking like and what inputs will be needed)