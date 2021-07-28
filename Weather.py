import requests
from datetime import datetime

api_key = 'bc2725039e03039b9e8c47281ad18a1f'
location = input("Enter the city name: ")

complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print(f"Weather Stats for - {location.upper()}  || {date_time}")
print("-------------------------------------------------------------")

print(f"Current temperature is: {temp_city :.2f} deg C")
print(f"Current weather desc  : {weather_desc}")
print(f"Current Humidity      : {hmdt} %")
print(f"Current wind speed    :{wind_spd} kmph")

print("====================================================")


# making a list so that i can print the info to a txt
txtlist = [temp_city, weather_desc, hmdt, wind_spd, date_time]
# using open() buit-in function to write to a text file
with open("textfile.txt", mode='w', encoding='utf-8') as f:
    # encoding = utf-8 for linux and cp1252 for win
    f.write("------------------------------------------------------------- \n ")
    f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    f.write("\n ------------------------------------------------------------- \n")
    f.write("Current temperature is: {:.2f} deg C\n".format(txtlist[0]))

    f.write("{},{} \n".format("Current weather desc  :", txtlist[1]))
    f.write("{},{},{} \n".format("Current Humidity      :", txtlist[2], "%"))
    f.write("{},{},{} \n".format(
        "Current wind speed    :", txtlist[3], "kmph"))
    f.write("====================================================")
