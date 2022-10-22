"""
Model of a single battery module
"""

class BatteryModule:

    # TODO: will probably need more helper methods

    """
    constructor
    """
    def __init__(self, voltage, temperature, capacity, resistance):
        self.voltage = voltage
        self.temperature = temperature
        self.current = 0
        self.capacity = capacity
        self.resistance = resistance

    """
    run the battery module with a certain current for a certain time 
    """
    def run(current, time):
        # TODO
        pass