import cozmo
import requests
import json

api_key = '6ef4dbea48b1168603b72af9189c2d6c'
lat = "42.1429"
lon = "77.0547"
url = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(url)
data = json.loads(response.text)
print(data)