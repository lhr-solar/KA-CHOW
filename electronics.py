"""
model of the low-voltage electrical system
"""
#return a simple value for electronics voltage, ask power system later for the power value that is not supposed to fluctuate a lot
#the plan for now is to convert it somehow to current then use that in the car class to calculate the current passed into the battery subclasses
#will need power system to provide the resistance value first
class Electronics:
    
    def __init__(self, power):
        self.power = power

    """
    Run the electrical system for a certain amount of time. This assumes the fluctuations in power usage are negligible
    
    :param time: time to run in seconds
    :returns: power used in watts """
    def run(self, time):
        return self.power * time