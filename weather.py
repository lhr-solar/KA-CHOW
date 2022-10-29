

class Weather:
    
    def __init__(self, latitude, longitude, time):
        self.latitude = latitude
        self.longitude = longitude
        self.time = time
        
    def set_time(self, time):
        self.time = time
        
    def get_angle_to_sun(self):
        #get weather data from API
        #return weather data
        pass
        
    #returns the intensity of the sun in W/m^2
    def get_intensity(self):
        #get weather data from API
        #return weather data
        pass