import requests

def getCapitalCity(country):
    parameters: dict = {
        'name': country
    }
    response = requests.get(url='https://jsonmock.hackerrank.com/api/countries', params=parameters)
    response.raise_for_status()  # checks for error codes

    data = response.json()
    country_data = data['data']
    print(data)

cap_city = getCapitalCity('Afghanistan')

print(cap_city)