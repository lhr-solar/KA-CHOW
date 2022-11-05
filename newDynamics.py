# new car dynamics class

import math

class newDynamics:
    
    def __init__(self, mass, dragCoefficient, frontalArea, rollingResistance, bearingResistance, wheelRadius, velocity):
        self.mass = mass;
        self.dragCoefficient = dragCoefficient;
        self.frontalArea = frontalArea;
        self.rollingResistance = rollingResistance;
        self.bearingResistance = bearingResistance;
        self.whellRadius = wheelRadius;
        self.velocity = velocity;
        self.targetSpeed = 0;

    def setVelocity(self, velocity):
        self.velocity = velocity

    def setTargetSpeed(self, targetSpeed):
        self.targetSpeed = targetSpeed

    def getVelocity(self):
        return self.velocity

    def calculateForce(self, velocity, gradient, airDensity):
        # calculate the force required to maintain the target speed
        force = self.mass * (self.targetSpeed - velocity) / self.timeStep
        # calculate the force required to overcome the rolling resistance
        force += self.mass * self.GRAVITY * self.rollingResistance
        # calculate the force required to overcome the aerodynamic drag
        force += 0.5 * self.dragCoefficient * airDensity * velocity * velocity * self.frontalArea
        # calculate the force required to overcome the gradient
        force += self.mass * self.GRAVITY * math.sin(math.radians(gradient))
        return force
    
    def calculateDrag(self, velocity, gradient, airDensity):
        # calculate the aerodynamic drag and the drag due to the gradient
        drag = 0.5 * self.dragCoefficient * airDensity * velocity * velocity * self.frontalArea
        drag += self.mass * self.GRAVITY * math.sin(math.radians(gradient))
        return drag

    def calculateTorque(self):
        # calculate the torque required to overcome the rolling resistance
        torque = self.mass * self.GRAVITY * self.rollingResistance * self.radius
        # calculate the torque required to overcome the aerodynamic drag
        torque += 0.5 * self.dragCoefficient * self.airDensity * self.velocity * self.velocity * self.frontalArea * self.radius
        # calculate the torque required to overcome the gradient
        torque += self.mass * self.GRAVITY * math.sin(math.radians(self.gradient)) * self.radius
        return torque


    