import requests
import time

MY_LAT: int = 42.179560
MY_LONG: float = -87.930440
FLAG_FOR_UNIX_TIME = 0

parameters: dict = {
  "lat": MY_LAT,
  "lng": MY_LONG,
  "time": FLAG_FOR_UNIX_TIME
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(sunrise.split(':')[0], sunset.split(':')[0])

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
formatted_time = current_time.split(':')[0]
print(formatted_time)