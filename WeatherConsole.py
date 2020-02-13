# put mock images in separate file
clear_day =  '''\033[0;33m
      \__/
    __/  \__
      \__/
      /  \ \033[0m'''

clear_night = '''\033[1;37m
      .   +
    +   .   . \033[0;33m(\033[1;37m 
      .   +   .
     +  .  .\033[0m'''

light_cloud_night = '''\033[1;37m
      .   + 
    +  .-.  . \033[0;33m(\033[1;37m 
     .(   )  .
    (__)___) \033[0m'''

light_cloud_day = '''\033[0;33m
          \__/\033[1;37m
       .-.\033[0;33m/  \\__\033[1;37m
     .(   ).\033[0;33m_/\033[1;37m
    (___(___)\033[0;33m\\\033[1;37m
    \033[0m'''

cloudy = '''\033[0;37m
       .--.
     .(    )-.
    (__(__.___)
    \033[0m'''

light_rain = '''\033[0;37m
       .--.
     .(    )-.
    (__(__.___)\033[0;36m
      ‘  ‘  ‘
     ‘  ‘  ‘\033[0m'''

showers = '''\033[0;37m
       .--.
     .(    )-.
    (__(__.___)\033[0;36m
    ‘  ‘  ‘  ‘
   ‘  ‘  ‘  ‘\033[0m'''

heavy_rain = '''\033[1;30m
       .--.
     .(    )-.
    (__(__.___)\033[0;36m
     ‘ ‘ ‘ ‘ ‘ 
    ‘ ‘ ‘ ‘ ‘\033[0m'''

hail = '''\033[1;30m
       .--.
     .(    )-.
    (__(__.___)\033[1;37m
     | | | | |
     . . . . .\033[0m'''

thunderstorm = '''\033[1;30m
       .--.
     .(    )-.
    (__(__.___)\033[0;36m
     ‘ ‘ \033[0;33m/_\033[0;36m‘ ‘ 
    ‘ ‘ ‘\033[0;33m /\033[0;36m‘ ‘\033[0m'''

sleet = '''\033[1;30m
       .--.
     .(    )-.
    (__(__.___)\033[1;37m
   . ‘ . ‘ . ‘
    . ‘ . ‘ .\033[0m'''

snow = '''\033[1;30m
       .--.
     .(    )-.
    (__(__.___)\033[1;37m
     * * * * * 
    * * * * * *\033[0m'''

heavy_cloud = '''\033[1;30m
   .--.       
 .(    )-.    .-.
(__(__.___) .(   ).
           (__(____)\033[0m'''

all_weather = [
    clear_day, 
    light_cloud_day, 
    clear_night, 
    light_cloud_night, 
    heavy_cloud, 
    light_rain, 
    showers, 
    heavy_rain, 
    thunderstorm, 
    hail,
    sleet,
    snow
]

import requests
import json

# create a formatted string of the Python JSON object
def format_json_response(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def convert_to_fahrenheit(temp):
    return round(temp * 9/5 + 32)

def format_display_time(time):
    minute = get_minute(time)

    hour = int(get_hour(time))
    if hour > 12: 
        am_pm = 'PM'
        hour -= 12
    elif hour == 12:
        am_pm = 'PM'
    else:
        am_pm = 'AM'
        if hour == 0: hour = 12

    return str(hour) + ':' + minute + ' ' + am_pm

def calc_sum_of_minutes(time):
    minutes_in_hours = int(get_hour(time)) * 60
    minutes = int(get_minute(time))

    return minutes_in_hours + minutes

def check_if_daylight(time, sun_rise, sun_set):
    time = calc_sum_of_minutes(time)
    sun_rise = calc_sum_of_minutes(sun_rise)
    sun_set = calc_sum_of_minutes(sun_set)

    if sun_rise < time and time < sun_set:
        return True
    else:
        return False

def get_minute(time):
    return time[14:16]

def get_hour(time):
    return time[11:13]

def get_year(time):
    return time[0:4]

def get_month(time):
    return time[5:7]

def get_date(time):
    return time[8:10]


def format_display_date(time):
    return get_month(time) + '/' + get_date(time) + '/' + get_year(time)

def display_ascii_image(time, sun_rise, sun_set, weather_abbr):
    is_daylight = check_if_daylight(time, sun_rise, sun_set)

    if weather_abbr == 'c' : 
        if is_daylight: ascii_image = clear_day
        else: ascii_image = clear_night
    elif weather_abbr == 'lc' : 
        if is_daylight: ascii_image = light_cloud_day
        else: ascii_image = light_cloud_night
    elif weather_abbr == 'hc' : ascii_image = heavy_cloud
    elif weather_abbr == 'lr' : ascii_image = light_rain
    elif weather_abbr == 's' : ascii_image = showers
    elif weather_abbr == 'hr' : ascii_image = heavy_rain
    elif weather_abbr == 't' : ascii_image = thunderstorm
    elif weather_abbr == 'h' : ascii_image = hail
    elif weather_abbr == 'sl' : ascii_image = sleet
    elif weather_abbr == 'sn' : ascii_image = snow
    else: ascii_image = '**no image**'

    return ascii_image

def line():
    return '________________________________________________\n'

def set_forcast_data():

    data = response.json()['consolidated_weather']

    forcast_data = {}

    for forcast_day in range(0,len(data)):

        forcast_data.update({
            "day" + str(forcast_day) : {
                'temp': str(convert_to_fahrenheit(data[forcast_day]['the_temp'])),
                'weather_abbr': data[forcast_day]['weather_state_abbr'],
                'weather_name': data[forcast_day]['weather_state_name'],
                'applicable_date': data[forcast_day]['applicable_date']+'T12:00',
                'max_temp': str(convert_to_fahrenheit(data[forcast_day]['max_temp'])),
                'min_temp': str(convert_to_fahrenheit(data[forcast_day]['min_temp']))
            },
        })

    return forcast_data

def display_forcasted_weather(): 

    display_output = ''

    data = set_forcast_data()

    for key, value in data.items():
        forcast_day = value

        x_abbr = forcast_day['weather_abbr']
        x_date = forcast_day['applicable_date']
        x_min_temp = forcast_day['min_temp']
        x_max_temp = forcast_day['max_temp']

        display_this_ascii_image = display_ascii_image(
            x_date, 
            sun_rise, 
            sun_set, 
            x_abbr
        )

        display_output += \
            line() + \
            format_display_date(x_date) + '\n' + \
            display_this_ascii_image + '\n\n' + \
            'High: ' + x_max_temp + '\n' + \
            'Low: ' + x_min_temp + '\n'

    display_output += line()
    return display_output
        
def display_current_weather():
        
    current_weather = \
        line() + '\n' + \
        '\t' + format_display_date(time) + \
        '\t' + format_display_time(time) + '\n' + \
        line() + \
        'Current weather conditions for: ' + city_title + '\n' + \
        display_ascii_image(time, sun_rise, sun_set, weather_abbr) + '\n\n' + \
        str(convert_to_fahrenheit(temp)) + '°F\n' + \
        line() + '\n' + \
        'Sun Rise: ' + format_display_time(sun_rise) + '\n' + \
        'Sun Set: ' + format_display_time(sun_set) + '\n'

    return current_weather

site = 'https://www.metaweather.com/'

city = input('Enter a city name: ')
# city = 'seattle'

response = requests.get(site + '/api/location/search/?query='+ city)

status_code = response.status_code

# DEBUGING::
    # format_json_response(response.json())
if not response.json() == []:    

    woeid = str(response.json()[0]['woeid'])
    response = requests.get(site + '/api/location/'+ woeid) 

    city_title = response.json()['title']

    # current time, sunrise & sunset times: 
    #       format: '2020-02-01T08:06:05.513467-08:00'
    time = response.json()['time'] 
    sun_rise = response.json()['sun_rise']
    sun_set = response.json()['sun_set']

    # json object holding data for the current day
    data = response.json()['consolidated_weather'][0] # 0 is current day

    temp = data['the_temp']
    weather_abbr = data['weather_state_abbr']
    weather_name = data['weather_state_name']
    applicable_date = data['applicable_date']
    max_temp = data['max_temp']
    min_temp = data['min_temp']

    print(
        display_current_weather() + \
        display_forcasted_weather()
    )

else:
    print('city not found')
