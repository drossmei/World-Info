from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import units, weather

API_KEY = '2a9db1ecd7b5c3c1c7574c1f198d1983'

darksky = DarkSky(API_KEY)

# i is a double with the temperature
# you can change temperature at the end to other weather conditions
def getWeather(latitude : float, longitude : float):
    return darksky.get_forecast(latitude, longitude).currently

# URL = "https://api.darksky.net/forecast/2a9db1ecd7b5c3c1c7574c1f198d1983/33.6839473,-117.7946942"