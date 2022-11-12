"""
Model of a single battery module
"""
import math

from battery_pack import internalResistanceOfPack

#comments left by Manthan and Byrn:

#variables that fluctuate (we may have to account for it later): internal resistance of the battery, the voltage of the battery, temperature
    #for now they are assumed to be constant
#the overall structure of the battery: one battery module consists of 9 batteries in parallel
#                                      one battery pack consists of 32 battery modules in series

#there is power lost and power generated of the battery
#power loss refers to the inefficiency of the battery, so if it is 0.5 watts, then to get 8 watts as the power outputted the battery would have to generate 8.5 watts
#
#to do: 
#calculate power generated = voltage * current (of each module)
#calculate power lost = current^2 * internal resistance (of each module)
#add them up in the main
#add them together (pack)
#multiply by delta T time (can be called: lostCapacity)
#divide it by the overall capacity to calculate it in percents 
#return that and in the main class add lostCapacity to static battery capacity variable


class BatteryModule:

    """
    constructor
    """
    #def __init__(self, voltage, temperature, capacity, resistance):
        #self.temperature = temperature #most likely will not be needed


    def __init_(self, capacity, current):
        #voltage given; should be a constant value
        self.voltage = 0
        #internal resistance is a given constant value
        self.resistance = 0 #0 for now, will be calculated later
        #current calculated from KCL of array, motor, electronics
        self.current = current
        #current battery capacity in percent
        self.capacity = capacity

    def internalResistanceOfModule(self, CellResistance):#calc resistance of a module
        n = 9
        while(n!=0):
            self.resistance += 1/CellResistance
            n-=1
        self.resistance = pow(self.resistance, -1)
        return self.resistance
    
    def voltageOfModule(self):#same as for the cell 
        return self.voltage
    

    def powerGeneratedByModule(self):#pass current calculated from array, electronics, and motor
        return self.voltage * self.current

    def powerLostByModule(self):
        return pow(self.current, 2) *  self.internalResistanceOfModule(self.resistance)

    """
    run the battery module with a certain current for a certain time 
    """
    def run(current, time):
        # TODO
        pass