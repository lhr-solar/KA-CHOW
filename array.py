import requests

#model for a solar cell array
class Array:
    def __init__(self):
        self.num_c60 = 300
        self.num_e60 = 90

    def get_power(self):
        solarcell_c60 = SolarCell(solarcell_c60, 153.328, 0.225, 25, -0.00342) #unsure of the temperature_coefficients
        solarcell_e60 = SolarCell(solarcell_e60, 153.328, 0.237, 25, -0.00363)
        return solarcell_c60.get_power_gen(1000) * self.num_c60 + solarcell_e60.get_power_gen(1000) * self.num_e60
    
    
    
#model for a solar cell in a solar panel
class SolarCell:
    #@param area is in cm^2, efficiency is a percentage, temperature is in Celsius
    #@param temperature coefficient is in %/C, negative value for how much it decreases
    #self.area is in m^2
    def __init__(self, area, efficiency, temperature, temperature_coefficient):
        self.area = area / 10000
        self.efficiency = efficiency
        self.temperature = temperature
        self.temperature_coefficient = temperature_coefficient
        
        self.standard_temp = 25 #standard test condition temperature
        self.standard_intensity = 1000 #standard test condition intensity

    def get_area(self):
        return self.area

    def get_efficiency(self):
        return self.efficiency

    def update_temperature(self, temperature):
        self.temperature = temperature
       
    #light_intensity is in W/m^2
    def get_power_gen(self, light_intensity):
        temperature_loss = (self.temperature - self.standard_temp) * self.temperature_coefficient
        return self.area * self.efficiency * light_intensity * (1 - temperature_loss)