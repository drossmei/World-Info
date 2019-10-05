from weatherCity import weatherCity
import json

# json holds the latitude and longitudes of supported cities
input_file = open('cityLoc.json')
cities = json.load(input_file)
input_file.close()

# Temporary input for text version of program
def inputCity() -> str:
    return input("Enter a city: ")

def weatherInput() -> str:
    return input('Enter "Temperature," "Humidity," "Precipitation," "Time," or "UV": ')

city = inputCity()

wc = weatherCity(city, cities)
def printInputWeather():
    try:
        print(eval('wc.get' + weatherInput() + "()"))
    except:
        printInputWeather()

printInputWeather()