"""
Model of a single battery module
"""
import math

from battery_pack import internalResistanceOfPack

class BatteryModule:

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
    def run(current, time):
        
        pass
    """