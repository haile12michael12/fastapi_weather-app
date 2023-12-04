import requests

r=requests.get("https://api.weather.gov/gridpoints/TOP/31,80/forecast").json()
print(r)
