import requests
from twilio.rest import Client

account_sid = 'ACb5236e0d8592647779059ccc50e61ef7'
auth_token = '002e79aea069350fb14ee0937883cb5d'
client = Client(account_sid, auth_token)
API_KEY = '16b30ea26d10adea8608512999d8323e'
ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
parameters = {
    'lat': 39.7294,
    'lon': -104.8319,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}

response = requests.get(url=ENDPOINT, params=parameters)
response.raise_for_status()

data = response.json()
print(data['list'])
indexes: int = 12

will_rain = False

for index in range(0, indexes):
    condition_code = data['hourly'][index]['weather'][index]['id']
    if condition_code < 700:
        will_rain = True

#or
"""
data_slice = data['hourly'][:12]
for hour_data in data_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
        
"""

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☔",
        from_="+15205026724",
        to='+18474014291'
    )

    print(message.status)