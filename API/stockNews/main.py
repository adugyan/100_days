import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

#TODO Add a better news API. This one is shite
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
account_sid = 'ACb5236e0d8592647779059ccc50e61ef7'
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
ALPHA_KEY = os.environ.get('ALPHA_KEY')
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': ALPHA_KEY,
    'outputsize': 'compact'
}

NEWS_KEY = os.environ.get('NEWS_KEY')
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
date = '2022-09-18'
news_params = {
    'q': COMPANY_NAME,
    'from': date,
    'sortBy': 'popularity',
    'language': 'en',
    'apikey': NEWS_KEY
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()

stock_data = stock_response.json()['Time Series (Daily)']
stock_list = [value for (key, value) in stock_data.items()]

yesterday_closing_price = float(stock_list[0]['4. close'])
ereyesterday_closing = float(stock_list[1]['4. close'])
percentage_decrease = (((yesterday_closing_price / ereyesterday_closing) / yesterday_closing_price) * 100)
percentage_increase = (((ereyesterday_closing / yesterday_closing_price) / yesterday_closing_price) * 100)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
formatted_article = None

news_data = news_response.json()['articles']
if percentage_decrease >= 5:
    for index in range(3):
        stock_change = f"{STOCK}: 🔻{percentage_decrease}%"
        title = f"{news_data[index]['title']}:"
        description = f"{news_data[index]['description']} \n"
        formatted_article = f"{stock_change} \n{title} \n{description}"

if percentage_increase >= 5:
    for index in range(3):
        stock_change = f"{STOCK}: 🔺{percentage_increase}%"
        title = f"{news_data[index]['title']}:"
        description = f"{news_data[index]['description']} \n"
        formatted_art = f"{stock_change} \n{title} \n{description}"


proxy_client = TwilioHttpClient()
#proxy_client.session.proxies = {'https': os.environ['https_proxy']}

client = Client(account_sid, AUTH_TOKEN, http_client=proxy_client)
message = client.messages \
    .create(
    body=formatted_article,
    from_="+15205026724",
    to='+18474014291'
)

print(message.sid)
