import requests, json

class GetWeather:

    def get_info_list(city):
        # API key
        api_key = "611454210432c7064822cbcbe7dc14d7"
  
        # base_url variable to store url 
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
          
        # complete_url variable to store complete url address 
        complete_url = base_url + "appid=" + api_key + "&q=" + city 
          
        # get method of requests module return response object 
        response = requests.get(complete_url) 

        # json method of response object. Convert json format data into 
        # python format data 
        return response.json()

        

    def get_description(x):
        # Extracts the "description" information from the "weather" list
        weather_list = x["weather"]
        weather_index_0 = weather_list[0]
        return weather_index_0["description"]

    def get_temp(x):
        # Extracts the "temperature" information from the "main" list
        main_list = x["main"]
        temperature = main_list["temp"]
        # Converts temperature from Kelvin to Fahrenheit
        return round(1.8 * (temperature - 273) + 32)

    def get_feels_like(x):
        # Extracts the "feels like" information from the "main" list
        main_list = x["main"]
        feels_like = main_list["feels_like"]
        return round(1.8 * (feels_like - 273) + 32)

    def get_wind(x):
        # Extracts the "speed" information from the "wind" list
        wind_list = x["wind"]
        wind_speed = wind_list["speed"]
        # Converts wind speed from m/s to mph
        return round(wind_speed * 2.23693629)

    def get_sunrise(x):
        # Extracts the "sunrise" information from the "sys" list
        sys_list = x["sys"]
        sunrise = sys_list["sunrise"]
        # Convert the information from seconds to hours and minutes
        seconds_in_day = (sunrise - 28800) % 86400
        hours = seconds_in_day // 3600
        minutes = seconds_in_day // 60 % 60
        return hours, minutes
    
    def get_sunset(x):
        # Extracts the "sunrise" information from the "sys" list
        sys_list = x["sys"]
        sunset = sys_list["sunset"]
        # Convert the information from seconds to hours and minutes
        seconds_in_day = (sunset - 28800) % 86400
        hours = seconds_in_day // 3600 - 12
        minutes = seconds_in_day // 60 % 60
        return hours, minutes

# What you'll have to write in the main program
city_name = input("Enter city name: ")

info_list = GetWeather.get_info_list(city_name)
# Adds items to a list to check if program is working
show = []
show.append(GetWeather.get_description(info_list))
show.append(GetWeather.get_temp(info_list))
show.append(GetWeather.get_feels_like(info_list))
show.append(GetWeather.get_wind(info_list))
show.append(GetWeather.get_sunrise(info_list))
show.append(GetWeather.get_sunset(info_list))

print(show)

