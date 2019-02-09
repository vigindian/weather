#
# Python script to get input and show weather
#
# Vignesh Narasimhulu
#

import requests
import json

#define the base url and the api-key to access weather data
baseurl='http://api.openweathermap.org/data/2.5/weather?q='
apikey='c5df5a566d55d3251922e9d9e057d763'

city='Singapore'

r=requests.get(baseurl + city+"&APPID="+apikey)
#check RC
rc=r.status_code

#if success
if (rc == 200):
    #access the json data
    rj=r.json()
    #print(rj)
    lon=rj['coord']['lon']
    print (lon)
