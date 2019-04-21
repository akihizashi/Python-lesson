from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
geolocator = Nominatim(user_agent="get_weather")

class Location:

    def __init__(self, location, latitude, longitude):
        self.location = location
        self.latitude = latitude
        self.longitude = longitude

    def getLocationName(self):
        try:
            location = geolocator.geocode(self)
            return location
        except GeocoderTimedOut:
            return 'Sorry, Tinker can\'t get your location' 

    def getLocationByCoordinate(self):
        try:
            location = geolocator.geocode(self)
            latitude = location.latitude
            longitude = location.longitude
            return {"latitude": latitude, "longitude": longitude}
        except GeocoderTimedOut:
            return 'Sorry, Tinker can\'t get your location'
# location = Location
# print(location.getLocationName('kawasaki'))
# print(location.getLocationByCoordinate('kawasaki'))