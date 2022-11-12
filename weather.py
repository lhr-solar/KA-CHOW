import math
import pysolar
import requests
import csv
import codecs
import os.path

class Weather:
    #this is the api key for website https://www.visualcrossing.com/weather-api
    #limited to 1000 free / day
    API_KEY = "UBJES729Z5FC7YCXGZK3CNMYG"
    outputfilename = "weather_data/weather.csv"
    csv_data = []
    
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
    
    def pull_weather_data(self):
        #get weather data from API from visual crossing and stores it into a csv file
        #return weather data
        if(len(self.csv_data) == 0):
            if os.path.isfile(self.outputfilename):
                with open(self.outputfilename, 'r', newline='') as csvfile2:
                    reader = csv.reader(csvfile2)
                    next(reader)
                    self.csv_data = list(reader)
            else:
                with open(self.outputfilename, 'w', newline='') as csvfile:
                    wet = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' + str(self.latitude) + ',' + str(self.longitude) +'?unitGroup=metric&include=hours&key=' + self.API_KEY +'&contentType=csv').text
                    csvfile.write(wet)
                    csvfile.close()
                    
                    #inprove later
                    with open(self.outputfilename, 'r', newline='') as csvfile2:
                        reader = csv.reader(csvfile2)
                        next(reader)
                        self.csv_data = list(reader)
        curTime = self.time[:-5] + "00:00"
        for row in self.csv_data:
            if(row[1] == curTime):
                return row[17]

if __name__ == "__main__":
    a = Weather(40.7128, -74.0060, "2022-11-12T11:10:00")
    a.pull_weather_data()