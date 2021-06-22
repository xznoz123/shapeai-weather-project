import requests
#import os
from datetime import datetime

api_key = '25ef887cff1b37ceb08709200d12c7df'#adding my api key
location = input("city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
#getting information of wheather from the link
api_data = api_link.json()

# using some variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("*-------------------------------------------------------------*")
print ("Weather Stats for - () & ()".format(location.upper(), date_time))
print ("*-------------------------------------------------------------*")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

g=open("project.txt","a")
g.write("**on upper slide we have previous data of weather**")
g.write ("\n-------------------------------------------------------------\n")
g.write ("Weather Stats for - ""location"+"= "+location.upper()+"\t|| date and time"+"= "+date_time)
g.write("\n-------------------------------------------------------------\n")
g.write('Current temperature is: {:.2f} deg C\n'.format(temp_city))
g.write("Current weather desc:"+weather_desc)
g.write('\nCurrent Humidity: {:.0f} %\n'.format(hmdt))
g.write("Current wind speed : {:} kmph\n".format(wind_spd))
g=open("project.txt","r")
print(g.read())
g.close()