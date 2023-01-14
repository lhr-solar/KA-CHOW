import math
import pysolar
import csv
import codecs
import os.path
import json, requests, datetime


class Weather:
    # this is the api key for website https://www.visualcrossing.com/weather-api
    # limited to 1000 free / day
    API_KEY = "UBJES729Z5FC7YCXGZK3CNMYG"
    outputfilename = "weather_data/weather.csv"
    csv_data = []

    def __init__(self, latitude, longitude, time):
        self.latitude = latitude
        self.longitude = longitude
        self.time = time

        url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' + str(
            self.latitude) + ',' + str(self.longitude) + f'/{int(time)}/{int(time) + 60*60*24*7}' + '?unitGroup=metric&include=hours&key=' + self.API_KEY + '&contentType=json'
        data = json.loads(requests.get(url).text)

        self.data = data
        with open("weather_data/weather.json", "w") as outfile:
            json.dump(data, outfile)


    # returns the intensity of the sun in W/m^2
    @staticmethod
    def get_intensity(self):
        # get weather data from API
        # return weather data

        # altitude_deg = pysolar.solar.get_altitude(self.latitude,self.longitude,self.time)
        # return pysolar.radiation.get_radiation_direct(self.time,altitude_deg)

        return self.currWeatherRad

    def pull_weather_data(self, epochTime):
        for day in self.data["days"]:
            t = int(day["datetimeEpoch"]) + 86400 # a day in seconds
            if t > epochTime:
                for hour in day["hours"]:
                    light_intensity = float(hour["solarradiation"])
                    if int(hour["datetimeEpoch"]) > epochTime:
                        print(f'Light Intensity at {day["datetime"]} @ {hour["datetime"]}: {light_intensity}')
                        self.currWeatherRad = light_intensity
                        return light_intensity


if __name__ == "__main__":
    a = Weather(40.7128, -74.0060, "2022-11-12T11:10:00")
    a.pull_weather_data()
