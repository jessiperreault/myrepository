print("Welcome to OpenWeather database.")
print()

#create an import function to retrieve data
import json, requests

#create variable for base url, the id, and create input for city name
baseurl = "https://api.openweathermap.org/data/2.5/weather"
appid = "2a9f0837f538e74956072959e47e3868"
city = input("Please Enter a city: ")


#create string that makes up url formula made of previous variables
url = f"{baseurl}?q={city}&APPID={appid}"
print(url)
print()

#pull that data from json by creating a response variable that makes a request to json database
response = requests.get(url)
unformated_data = response.json()
print(unformated_data)

#give the user the current temp and max temp of that area for the day by pulling variables from the unformated data that represent that data
#need to figure out way to display error message if "city not found"
temp = unformated_data["main"]["temp"]
print(f"The current temperature is: {temp}")
temp_max = unformated_data["main"]["temp_max"]
print(f"The maximum temperature is: {temp_max}")
humidity = unformated_data["main"]["humidity"]
print(f"The atmospheric humidity percentage is: {humidity}%")
feels_like = unformated_data["main"]["feels_like"]
print(f"It feels like: {feels_like}")

#create try/except block that checks if the input city is valid, if not, the program will prompt valid city input
#while True:
  #print()
  #if False:
  #error msg


again = 'yes'

while again == 'yes':

  print('Would you like to enter another city? (yes or no)')
  
  again = input()

  if again == 'no':
    print('Thank you.')

    #testing
