# model of the motor
import dynamics

#incline of the pedal is given
#the current the motor would draw = percentage of the pedal incline * max current allowed (50 Amps)
class Motor:
    def __init__(self, speed,slope):#pedal Incline in percent
        #self.pedalIncline = pedalIncline
        #self.current = self.pedalIncline * 50
        self.slope = slope
        self.speed = speed
        self.torque = 0
        self.current = 0
        
    def currentMotor(self):
        wheel_radius = .5
        dynam = dynamics(1000, 0.4, 0.7, .2, self.speed, 1)
        self.torque = wheel_radius * dynam.total_propelling_force(self.slope)
        self.current = (29/34)*self.torque + 1
        return self.current
        
    #def pedalIncline