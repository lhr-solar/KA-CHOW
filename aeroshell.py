# model of the aeroshell
class Aeroshell:
    
     def __init__(self, velocity, referenceArea, mediumDensity, dragCoefficient, distance):
        self.velocity = velocity 
        self.referenceArea = referenceArea
        self.mediumDensity = mediumDensity#a given constant
        self.dragCoefficient = dragCoefficient
        self.distance = distance

     def dragForce(self):
        return self.velocity * self.referenceArea * self.mediumDensity * self.dragCoefficient
    
    #distance is given 
     def energyLostv1(self):#distance is an input
        return self.dragForce() - self.distance
    #distance has to be calculated
     def energyLostv2(self, time, dragForce):
        return dragForce(self) - (time*self.velocity)
