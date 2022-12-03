import dynamics

class Motor:
    def __init__(self, speed,slope):#pedal Incline in percent
        #self.pedalIncline = pedalIncline
        #self.pedalIncline = self.current / 50
        self.slope = slope
        self.speed = speed
        self.torque = 0
        self.current = 0
        
    #current provided by motor calculated by force from Dynamics
    def currentMotor(self):
        #parameters need to be verified
        wheel_radius = .3 #m 
        mass = 1000 #kg
        rolling_friction = .4
        static_friction = .7
        drag_coefficient = .2
        frontal_area = 1 #m^2
        dynam = dynamics(mass, rolling_friction, static_friction, drag_coefficient, self.speed, frontal_area)
        self.torque = wheel_radius * dynam.total_propelling_force(self.slope)
        self.current = (29/34)*self.torque + 1 #equation from torque-current curve on motor data sheet
        return self.current

#the current the motor would draw = percentage of the pedal incline * max current allowed (50 Amps)
#pedal incline can be output to driver if needed