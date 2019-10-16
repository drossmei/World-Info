import requests

class weatherLocation:
    
    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude
        r = requests.get(f"https://api.darksky.net/forecast/2a9db1ecd7b5c3c1c7574c1f198d1983/{latitude},{longitude}")
        self._weatherMap = r.json()

    def getLatitude(self) -> int:
        ''' get the latitude of a city '''
        return self._latitude

    def getLongitude(self) -> int:
        ''' get the longitude of the city '''
        return self._longitude

    def getLatitudeAndLongitude(self) -> list:
        ''' get a list containing the latitude and longitude of the city '''
        return [self._latitude, self._longitude]

    def getTemperature(self) -> float:
        return self._weatherMap['currently']['temperature']

    def getHumidity(self) -> float:
        return self._weatherMap['currently']['humidity']

    def getPrecipitationProbability(self) -> float:
        return self._weatherMap['currently']['precipProbability']

    def getPrecipitationType(self)->str:
        ''' rain, snow, etc. '''
        try:
            return self._weatherMap['currently']['precipType']
        except:
            return 'rain'

    def getUV(self) -> str:
        return self._weatherMap['currently']['uvIndex']

    def getGeneral(self) -> str:
        ''' returns the general state of weather (e.g. "clear") '''
        return self._weatherMap['currently']['summary']

    def getVisibility(self) -> str:
        return self._weatherMap['currently']['visibility']


    def __repr__(self):
        return f"WeatherCity({self._latitude}, {self._longitude})"

    def __str__(self):
        return "The weather is {general} at {temp} degrees with a {precip}% chance of {precipType}.".format(general=self.getGeneral().lower(), temp=self.getTemperature(), precip=self.getPrecipitationProbability() * 100, precipType=self.getPrecipitationType())

