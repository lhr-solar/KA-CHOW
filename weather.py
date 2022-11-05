import math
import pysolar

class Weather:
    
    def __init__(self, latitude, longitude, time):
        self.latitude = latitude
        self.longitude = longitude
        self.time = time
        
    def set_time(self, time):
        self.time = time
        
    #returns the intensity of the sun in W/m^2
    def get_intensity(self):
        #get weather data from API
        #return weather data
        altitude_deg = pysolar.solar.get_altitude(self.latitude,self.longitude,self.time)
        return pysolar.radiation.get_radiation_direct(self.time,altitude_deg)