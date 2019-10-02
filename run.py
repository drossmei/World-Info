from weatherCity import weatherCity
import json

# json holds the latitude and longitudes of supported cities
input_file = open('cityLoc.json')
cities = json.load(input_file)
input_file.close()

# Temporary input for text version of program
def inputCity() -> str:
    city = input("Enter a city: ")
    return city

city = inputCity()

wc = weatherCity(city, cities)

wc.test()