# model of the motor
import dynamics

#incline of the pedal is given
#the current the motor would draw = percentage of the pedal incline * max current allowed (50 Amps)
class Motor:
    def __init__(self, mechLoss, dynam):#pedal Incline in percent
        self.pedalIncline = pedalIncline
        self.current = self.pedalIncline * 50
        self.mechLoss = mechLoss

    def currentMotor(self):
        return self.current

    def pedalIncline