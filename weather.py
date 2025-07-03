import requests
import math
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv()
api_key = os.getenv("OpenWeather_apiKey")


def get_coordinates(city_name):
    geocoding_api = "https://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": city_name,
        "limit": 1,
        "appid": api_key
    }
    r = requests.get(geocoding_api, params=params)

    data = r.json()
# if not empty list
    if data:
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        return lat, lon
    else:
        return None

def geo_reverse(lat, lon):
    geo_reverse_api = 'http://api.openweathermap.org/geo/1.0/reverse'
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key
    }
    response = requests.get(geo_reverse_api, params=params)
    return response.json()

def get_weather(lat, lon):
# Send request to OpenWeather API
    weather_api = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        'exclude': "minutely,hourly,daily,alerts",
        'units' : "imperial"
    }
    response = requests.get(weather_api, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data ['main']['feels_like']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']

        return weather, temp, feels_like, temp_min, temp_max
    else:
        print("Weather data unavailable.", response.status_code)
        return None

def main():
# Ask the user for a city name
    city = geo_reverse(40.7127281, -74.0060152)
    print(city)
    city_name = input("Enter a city name: ")
    coords = get_coordinates(city_name)
    if coords == None:
        print("Sorry, city not found.")
    else:
        lat, lon = get_coordinates(city_name)
        print(f"The coordinates for {city_name} are: ({lat}, {lon})")
 # Call get_weather and display_weather 
        weather, temp, feels_like, temp_min, temp_max = get_weather(lat, lon)
        print(f"Weather: {weather} \nTemperature: {temp}˚F \nFeels like {feels_like}˚F \nMin: {temp_min}˚F \nMax: {temp_max}˚F")



if __name__ == "__main__":
    main()