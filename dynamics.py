# model of the dynamics system
# TODO: might be good to break this up, depending on how complex it gets

"""
This class is meant to model the dynamics systems and energy losses
The system will take in paramaters such as the car's mass, the velocity it's going at,
& the friction coefficient of the car as preliminary constants. 
It will then calculate the total amount of energy lost as a result of the dynamics systems
"""
import math


class Dynamics:

    #constant for gravity
    GRAVITY = 9.81


    def __init__(self, mass, tire_frictk, velocity, theta):
        #the weight of the car
        self.weight = mass

        # the friction coefficients of the tire
        self.tire_frictk = tire_frictk
        
        # the velocity of the car
        self.velocity = velocity

        #the angle of incidence for the road. MEANT TO BE DEGREES
        self.theta = theta


    #this method will update the 
    def update_speed(self, velocity):
        self.velocity = velocity

    #this method returns the normal force of the car (weight * gravity * math.cos(degrees))
    def normal_force(self):
        return self.mass * self.GRAVITY * math.cos(math.radians(self.theta))

    #this method calculates the total amount of energy lost to friction
    def frictionLoss(self, time):
        return  self.normal_force(self) * self.tire_frictk * self.velocity * time

    #this method calculates & returns the total amount of enregy lost as a result of the dynamics system
    def dynamicsLoss(self, time):
        return self.frictionLoss(self, time)
