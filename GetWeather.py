import requests, json

class GetWeather:

    def __init__(self):

        city = "Seattle"
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
        self.x = response.json()

    def get_description(self):
        # Extracts the "description" information from the "weather" list
        weather_list = self.x["weather"]
        weather_index_0 = weather_list[0]
        return weather_index_0["description"]

    def get_temp(self):
        # Extracts the "temperature" information from the "main" list
        main_list = self.x["main"]
        temperature = main_list["temp"]
        # Converts temperature from Kelvin to Fahrenheit
        return str(round(1.8 * (temperature - 273) + 32)) + " F"

    def get_feels_like(self):
        # Extracts the "feels like" information from the "main" list
        main_list = self.x["main"]
        feels_like = main_list["feels_like"]
        return str(round(1.8 * (feels_like - 273) + 32)) + " F"

    def get_wind(self):
        # Extracts the "speed" information from the "wind" list
        wind_list = self.x["wind"]
        wind_speed = wind_list["speed"]
        # Converts wind speed from m/s to mph
        return str(round(wind_speed * 2.23693629)) + " mph"

    def get_sunrise(self):
        # Extracts the "sunrise" information from the "sys" list
        sys_list = self.x["sys"]
        sunrise = sys_list["sunrise"]
        # Convert the information from seconds to hours and minutes
        seconds_in_day = (sunrise - 28800) % 86400
        hours = seconds_in_day // 3600
        minutes = seconds_in_day // 60 % 60
        return str(hours) + ":" + str(minutes) + " AM"
    
    def get_sunset(self):
        # Extracts the "sunrise" information from the "sys" list
        sys_list = self.x["sys"]
        sunset = sys_list["sunset"]
        # Convert the information from seconds to hours and minutes
        seconds_in_day = (sunset - 28800) % 86400
        hours = seconds_in_day // 3600 - 12
        minutes = seconds_in_day // 60 % 60
        return str(hours) + ":" + str(minutes) + " PM"
    
    def get_icon(self):
        weather_list = self.x["weather"]
        identity = weather_list[0]["icon"]
        url = "http://openweathermap.org/img/w/" + identity + ".png"
        response = requests.get(url)
        imageLocation = '/home/pi/Desktop/SmartMirror/img/' + identity + '.png'
        with open(imageLocation, 'wb') as f:
            f.write(response.content)
        return imageLocation