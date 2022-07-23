import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json", verify=False)
response.raise_for_status()

data = response.json()
print(data)

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position: tuple = (longitude, latitude)