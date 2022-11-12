# model of the motor

#incline of the pedal is given
#the current the motor would draw = percentage of the pedal incline * max current allowed (50 Amps)
class Motor:
    def __init__(self, pedalIncline):#pedal Incline in percent
        self.pedalIncline = pedalIncline

    def currentMotor(self):
        return self.pedalIncline * 50