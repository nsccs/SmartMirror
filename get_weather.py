# Python program to find current  
# weather details of any city 
# using openweathermap api 
  
# import required modules
import requests, json 
  
# Enter your API key here 
api_key = "611454210432c7064822cbcbe7dc14d7"
  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name 
city_name = input("Enter city name : ") 
  
# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  
# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
x = response.json() 
  
# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 
  
    # store the value of "main" 
    # key in variable y 
    y = x["main"] 
  
    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature_k = y["temp"] 
  
    # store the value corresponding 
    # to the "pressure" key of y 
    current_pressure = y["pressure"] 
  
    # store the value corresponding 
    # to the "humidity" key of y 
    current_humidiy = y["humidity"] 
  
    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 
  
    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of z 
    weather_description = z[0]["description"] 
  
    # converts temperature from Kelvin to Fahrenheit
    current_temperature_f = 1.8 * (current_temperature_k - 273) + 32
    
    # print following values 
    print("\nTemperature: " + format(current_temperature_f, '.0f') + " F")
    # print("Atmospheric pressure: " + str(current_pressure) + " hPa")
    print("Humidity: " + str(current_humidiy) + "%")
    print("Description: " + str(weather_description))
    print(x)
else: 
    print(" City Not Found ") 



'''
What we want to be returned:
 1. Temp
 2. Feels Like
 3. Description:
 4. Wind Speed
 5. Sun Set Time
'''