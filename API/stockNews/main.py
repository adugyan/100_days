import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
account_sid = 'ACb5236e0d8592647779059ccc50e61ef7'
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
ALPHA_KEY = os.environ.get('ALPHA_KEY')
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
stock_params = {
    'function': 'OVERVIEW',
    'symbol': STOCK,
    'apikey': ALPHA_KEY
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

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()

stock_data = stock_response.json()
print(stock_data)

news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()

news_data = news_response.json()
print(news_data)
#top_3 = news_data[:4]

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

client = Client(account_sid, AUTH_TOKEN, http_client=proxy_client)
message = client.messages \
    .create(
    body="",
    from_="+15205026724",
    to='+18474014291'
)

print(message.status)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

