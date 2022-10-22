import battery_module
# model of the battery pack

class BatteryPack:

    """
    Constructor
    """
    def __init__(self, modules):
        self.modules = modules
        self.current = 0

    """
    run the battery at a specific current for a specific time
    TODO: should we be specifying power instead of current?
    """
    def run(self, current):
        # TODO: implement this
        pass
