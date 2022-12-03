import battery_module
# model of the battery pack

class BatteryPack:

    #current calculated in main from KCL of electronics, motor, array
    def __init__(self, capacity, current):
        self.modules = []
        for i in range (32):
            self.modules.append(battery_module.BatteryModule(capacity, current))
        
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
        
    def LostCapacity(self, deltaT):
        lostCapacity = self.updatePowerGeneratedByPack() + self.updatePowerLostByPack()
        lostCapacity*=deltaT
        #lostCapacity/=totalCapacity
        return lostCapacity

    """
    run the battery at a specific current for a specific time
    TODO:
    def run(self, current):
        # TODO: implement this
        pass
    """
