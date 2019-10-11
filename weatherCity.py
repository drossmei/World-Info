import weather

class weatherCity:
    
    def __init__(self, city : str, cities : dict):
        self.city = city
        self.cities = cities


    def getLat(self) -> int:
        ''' get the latitude of a city '''
        return self.cities[self.city][0]


    def getLon(self) -> int:
        ''' get the longitude of the city '''
        return self.cities[self.city][1]


    def getLatLon(self) -> list:
        ''' get a list containing the latitude and longitude of the city '''
        return self.cities[city]


    def checkValidCity(self) -> bool:
        if (self.city in self.cities):
            return True
        return False

    def getTemperature(self) -> str:
        return weather.getWeather(self.getLat(), self.getLon()).temperature

    def getHumidity(self) -> str:
        return weather.getWeather(self.getLat(), self.getLon()).humidity

    def getPrecipitation(self) -> str:
        return weather.getWeather(self.getLat(), self.getLon()).precip_probability

    def getTime(self) -> str:
        return weather.getWeather(self.getLat(), self.getLon()).time

    def getUV(self) -> str:
        return weather.getWeather(self.getLat(), self.getLon()).uv_index

    def getGeneral(self) -> str:
        ''' returns the general state of weather (e.g. "clear") '''
        return weather.getWeather(self.getLat(), self.getLon()).summary

    def getVisibility(self) -> str:
        return weather.getWeather(self.getLat(), self.getLon()).visibility


    def __repr__(self):
        return f"WeatherCity({self.city}, {self.cities})"


    def __str__(self):
        return "{city} is {general} at {temp} degrees fahrenheit with a {precip}% chance of rain.".format(city=self.city, general=self.getGeneral().lower(), temp=self.getTemperature(), precip=self.getPrecipitation() * 100)


    def test(self) -> None:
            print(self.city, "is", self.getGeneral(), "at", self.getTemperature(), "with", self.getPrecipitation() * 100, "chance of rain")
