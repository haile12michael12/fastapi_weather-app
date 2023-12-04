import requests
def getTemp():
r=requests.get("https://api.weather.gov/gridpoints/TOP/31,80/forecast").json()
day_temp= r["properties"]["period"]{0}
return {
   "temperature":day_temp["temperature"]
 "wind_speed":day_temp["windspeed"]
 "short_forcast":day_temp["shortforcast"]
 "icon":day_temp["icon"]
}
print(getTemp())
