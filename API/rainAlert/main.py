import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os


account_sid = 'ACb5236e0d8592647779059ccc50e61ef7'
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
API_KEY = os.environ.get('OWM_API_KEY')
ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
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
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, AUTH_TOKEN, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☔",
        from_="+15205026724",
        to='+18474014291'
    )

    print(message.status)