import forecastio
import requests
import json
# from location import Location
import ast
from urllib.request import urlopen
import pandas

class Weather:
    
    def __init__(self):
        pass

    def getWeatherData(self, latitude, longitude):
    # def getWeatherData(self):
        # request_link = 'https://api.darksky.net/forecast/c0c04cd3ca1920f3864260b49e44a68e/' + coordinate
        # print(request_link)
        # exit()
        # coordinate = latitude + longitude
        #################load form darksky#######################
        url = 'https://api.darksky.net/forecast/c0c04cd3ca1920f3864260b49e44a68e/'+ str(latitude) + ',' + str(longitude)
        
        forecast = urlopen(url).read().decode('utf8')
        forecast_json = json.loads(forecast)
        # print(forecast_json)
        # exit()
        return forecast_json
        #########################################
        # print(forecast_json)
        # exit()
        # forecast = forecastio.load_forecast(api_key, latitude, longitude)
        # print(forecast)
        #################load from file########################
        # with open('dumdata.txt', 'r') as f:
        #     s = f.read()
        #     whip = ast.literal_eval(s)
        #     return whip
        #########################################
            # whip.json()
            # print(whip)
            # exit()
        #########################################
        #########################################
    
    def getWeatherDaily(self, data):
        result = data['daily']
        print(result)
    
    def getWeatherHourly(self, data):
        result = data['hourly']
        for hourly in result['data']:
            date_time = self.convertTime(hourly['time'])
            print(date_time, hourly['icon'])
            print('###############')

    def getWeatherCurrently(self, data):
        result = data['currently']
        # print(result)
        print('It seems ' + result['summary'])
        print('Temperature about ' + str(int((result['temperature'] - 32)/1.8)) + '℃ ')
        self.advice(result)
        # print(result)
    def advice(self, data):
        if data['icon'] in ['clear-day', 'clear-night']:
            print('Tinker think that you should go some where because today\'s weather is very fine')
        if data['icon'] in ['rain', 'snow', 'thunderstorm', 'tornando']:
            print('Stay home is better. But if you have to go out, be careful')

    def convertTime(self, data):
        date_time = pandas.to_datetime(data, unit='s')
        return date_time

        
    

# api_key = "c0c04cd3ca1920f3864260b49e44a68e"
# location = Location
# coordinate = location.getLocationByCoordinate('kawasaki')
# coordinate = '35.523142,139.708024'
# coordinate = str(coordinate['latitude']) + "," + str(coordinate['longitude'])
# print(coordinate)
# exit()  
# print(coordinate['latitude'])
# exit()
# latitude = 35.523142
# longitude = 139.708024
# coordinate = str(latitude) + ',' +str(longitude)
# url = 'https://api.darksky.net/forecast/c0c04cd3ca1920f3864260b49e44a68e/'+coordinate
# for line in urlopen(url):
#     print(line)
# # print(url_open)
# exit()
# print(coordinate)
# exit()
# print('https://api.darksky.net/forecast/c0c04cd3ca1920f3864260b49e44a68e/' + str(latitude) + ',' + str(longitude))
# weather = Weather()
# weather_data = weather.getWeatherData()
# weather.getWeatherHourly(weather_data)
# print(weather_data.daily())
# daily = weather.getWeatherDataCurrently(weather_data)
# geolocator = Nominatim(user_agent="get_weather")
# location = geolocator.geocode("kawasaki")
# print(location.latitude, location.longitude)

# lat = location.latitude
# lng = location.longitude

# forecast = forecastio.load_forecast(api_key, lat, lng)
# # current_weather = forecast.currently()
# by_hour = forecast.hourly()
# daily_weather = forecast.hourly()

# print(daily_weather.summary)
# print ("Hourly Summary: %s" % (by_hour.summary))