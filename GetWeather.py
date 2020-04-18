
from datetime import datetime
import requests

"""
    :author Luan Ta
    Query the weather from a JSON file of a third party site
    Source: https://www.metaweather.com    
"""

detailed_weather = requests.get('https://www.metaweather.com/api/location/2490383/').json()  # Current Weather
current_weather = detailed_weather['consolidated_weather'][0]


def get_weather():
    return '\nThe Weather right now: ' + current_weather['weather_state_name'] + '\nTemperature: ' \
        + format(celsius_to_fahrenheit(current_weather['the_temp']), '.0F') + ' F\nWind Speed: ' \
        + format(current_weather['wind_speed'], '.2F') + '\nHumidity: ' + str(current_weather['humidity'])


def celsius_to_fahrenheit(degree):
    return degree * 9 / 5 + 32


def get_weather_img():
    sun_rise_hour = int(detailed_weather['sun_rise'][11:13])
    sun_set_hour = int(detailed_weather['sun_set'][11:13])
    status = current_weather['weather_state_abbr']
    if status == 'c' or status == 'lc':
        if sun_rise_hour < datetime.now().hour < sun_set_hour:
            return 'img/' + status + 'd.png'
        return 'img/' + status + 'n.png'
    return 'img/' + status + '.png'


