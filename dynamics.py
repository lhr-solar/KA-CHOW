# model of the dynamics system
# TODO: might be good to break this up, depending on how complex it gets

class Dynamics:
    def __init__(self, velocity, acceleration, air_mass_density):
        # Calculating the required vehicle propelling force
        self.gravity = 9.81
        self.mass = 1000 # kg
        self.rolling_res_coefficient = 0.01
        self.aerodynamic_drag_coefficient = 0.5
    
    def calculate_rolling_resistance(self):
        return self.rolling_res_coefficient * self.mass * self.gravity
    
    def calculate_aerodynamic_drag(self):
        return 0.5 * self.aerodynamic_drag_coefficient * self.air_mass_density * self.velocity**2
    
    def calculate_accel_force(self):
        return self.mass * self.acceleration
    
    def calculate_propelling_force(self): # Minimum force required to keep the vehicle moving
        return self.calculate_accel_force() + self.calculate_rolling_resistance() + self.calculate_aerodynamic_drag()


        
