import requests
import json


class GetWeather:
    def __get_complete_url(city):
        # API key
        api_key = "611454210432c7064822cbcbe7dc14d7"

        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # complete_url variable to store complete url address
        return base_url + "appid=" + api_key + "&q=" + city

    def get_info(city):

        complete_url = GetWeather.__get_complete_url(city)

        # get method of requests module return response object
        response = requests.get(complete_url)

        # json method of response object. Convert json format data into
        # python format data
        x = response.json()

        if x["cod"] != "404":  # If the website does not give a 404 error
            # The website returns all the information in one big list, which
            # contains many smaller lists
            # I extract all the  wanted information from the list and return it
            # as a list

            # Extracts the "description" information from the "weather" list
            weather_list = x["weather"]
            weather_index_0 = weather_list[0]
            description = weather_index_0["description"]

            # Extracts the "temperature" and "feels_like"
            # information from the "main" list
            main_list = x["main"]
            temperature_k = main_list["temp"]
            feels_like_k = main_list["feels_like"]
            # Converts temperature from Kelvin to Fahrenheit
            temperature_f = round(1.8 * (temperature_k - 273) + 32)
            feels_like_f = round(1.8 * (feels_like_k - 273) + 32)

            # Extracts the "speed" information from the "wind" list
            wind_list = x["wind"]
            wind_speed_m = wind_list["speed"]
            # Converts wind speed from m/s to mph
            wind_speed_mi = round(wind_speed_m * 2.23693629)
            # Returns only the information we want
            print(x)
            return  description,  temperature_f,  feels_like_f,\
                    wind_speed_mi
        else: 
            return "City Not Found"

# What you'll have to write in the main program
city_name = input("Enter city name : ")

info_we_want = GetWeather.get_info(city_name) # Get the information

print(info_we_want)

