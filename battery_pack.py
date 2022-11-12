import battery_module
# model of the battery pack

class BatteryPack:

    """
    Constructor
    """

    #return that and in the main class add lostCapacity to static battery capacity variable


    #def __init__(self, modules):
     #   self.modules = modules
     #   self.current = 0
     #   self.voltage = 0

    #current calculated in main from KCL of electronics, motor, array
    def __init__(self, capacity, current):
        modules = []
        for i in range (32):
            modules.append(battery_module(capacity, current))
        
    def updateModuleInternalResistance(self):
        runningSum = 0
        for i in range (32):
            runningSum += self.modules[i].internalResistanceOfModule(0)
        return runningSum

    def updatePowerGeneratedByPack(self):
        runningSum = 0
        for i in range (32):
            runningSum += self.modules[i].powerGeneratedByModule(0)
        return runningSum

    def updatePowerLostByPack(self):
        runningSum = 0
        for i in range (32):
            runningSum += self.modules[i].powerLostByModule(0)
        return runningSum
        
    def LostCapacity(self, deltaT, totalCapacity):
        lostCapacity = self.updatePowerGeneratedByPack() + self.updatePowerLostByPack()
        lostCapacity*=deltaT
        lostCapacity/=totalCapacity
        return lostCapacity




    """
    run the battery at a specific current for a specific time
    TODO: should we be specifying power instead of current?
    """
    def run(self, current):
        # TODO: implement this
        pass

#current is given