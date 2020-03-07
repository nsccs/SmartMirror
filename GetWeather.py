
from datetime import datetime
import requests
detailed_weather = requests.get('https://www.metaweather.com/api/location/2490383/').json()  # Current Weather
current_weather = detailed_weather['consolidated_weather'][0]


def get_weather():
    s = '[size=20][font=fonts/IndieFlower-Regular.ttf]Date: ' \
        + str(datetime.now().month).zfill(2) + '/' + str(datetime.now().day).zfill(2) \
        + '/' + str(datetime.now().year) + '[/font][/size]' + '\n' + get_time() \
        + '\nThe Weather right now: ' + current_weather['weather_state_name'] + '\nTemperature: ' \
        + format(celsius_to_fahrenheit(current_weather['the_temp']), '.0F') + ' F\nWind Speed: ' \
        + format(current_weather['wind_speed'], '.2F') + '\nHumidity: ' + str(current_weather['humidity'])
    return s


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


def get_time():
    return 'Time: ' + str(datetime.now().hour) + ':' + str(datetime.now().minute).zfill(2)
