import weather

class weatherCity:
    
    def __init__(self, city : str, cities : dict):
        self.city = city
        self.cities = cities


    def getLat(self):
        return self.cities[self.city][0]


    def getLon(self):
        return self.cities[self.city][1]


    def getLatLon(self) -> list:
        return self.cities[city]


    def checkValidCity(self) -> bool:
        if (self.city in self.cities):
            return True
        return False

    def getTemperature(self):
        return weather.getWeather(self.getLat(), self.getLon()).temperature

    def getHumidity(self):
        return weather.getWeather(self.getLat(), self.getLon()).humidity

    def getPrecipitation(self):
        return weather.getWeather(self.getLat(), self.getLon()).precip_probability

    def getTime(self):
        return weather.getWeather(self.getLat(), self.getLon()).time

    def getUV(self):
        return weather.getWeather(self.getLat(), self.getLon()).uv_index

    def getGeneral(self):
        return weather.getWeather(self.getLat(), self.getLon()).summary

    def getVisibility(self):
        return weather.getWeather(self.getLat(), self.getLon()).visibility


    def test(self) -> None:
            print(self.city, "is", self.getGeneral(), "at", self.getTemperature(), "with", self.getPrecipitation() * 100, "chance of rain")
