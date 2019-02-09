#
# Python script to get City name as user input and show weather details
#
# Vignesh Narasimhulu
#

import requests
import json

#define the base url and the api-key to access weather data
baseurl='http://api.openweathermap.org/data/2.5/weather?q='
#original api key masked from public code
apikey='xxxx'

try:
   city=str(input("Find your City: "))
   #city='Singapore'
except ValueError:
    print ("Sorry. Please provide a valid input, thanks!")

r=requests.get(baseurl + city+"&APPID="+apikey)
#check RC
rc=r.status_code

#if success
if (rc == 200):
    #access the json data
    rj=r.json()
    #print(rj)
    temp=rj['main']['temp']
    ctemp=int(temp)-273.15
    humidity=rj['main']['humidity']
    wdesc=rj['weather'][0]['description']
    #round-off to 2 decimal places
    print ("City Name: " +city)
    print ("Current Temperature in Celsius: " + f"{ctemp:.2f}")
    print ("Humidity: " + str(humidity) + "%")
    print ("Weather Condition: " + str(wdesc))

#handle city not found
elif (rc == 404):
    print ("Sorry. City not found!")
else:
    print ("Sorry, unable to retrieve the data at the moment!")
