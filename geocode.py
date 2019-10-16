import json
import requests
from LocationError import LocationError

class Location:

    def __init__(self, city : str):
        ''' Initializes the city to get the latitude/longitude of a given city '''
        self._city = city
        r = requests.get(f"https://geocode.xyz/{city}?json=1")
        self._mapData = r.json()
        if ('error' in self._mapData):
            raise LocationError # raises an error if city is not valid

    def getLatitude(self)->float:
        return self._mapData['latt']

    def getLongitude(self)->float:
        return self._mapData['longt']

    def getLatitudeAndLongitude(self)->list:
        return [self._mapData['latt'], self._mapData['longt']]

    def getDict(self)->dict:
        return self._mapData

    def __str__(self):
        return f'City of {self._city}'

    def __repr__(self):
        return f'Location({self._city})'

l = Location('Irvine')

