print("Hello world")


import config
import requests
import json

token = config.ALPHAVANTAGE

endpoint = 'https://www.alphavantage.co/query'
payload = {'function': 'TIME_SERIES_INTRADAY', 'symbol': 'TSLA', 'interval': '60min', 'apikey': token }


response = requests.get(endpoint, params=payload)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=2)
    print(text)

jprint(response.json())