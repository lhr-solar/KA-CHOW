"""
model of the low-voltage electrical system
"""

class Electronics:
    
    def __init__(self, power):
        self.power = power

    """
    Run the electrical system for a certain amount of time. This assumes the fluctuations in power usage are negligible
    
    :param time: time to run in seconds
    :returns: power used in watts """
    def run(self, time):
        return self.power * time