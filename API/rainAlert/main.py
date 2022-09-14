import requests

API_KEY = '16b30ea26d10adea8608512999d8323e'
parameters = {
    'lat': 39.7294,
    'lon': -104.8319,
    'appid': API_KEY
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()

data = response.json()
print(data['list'])