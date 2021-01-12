print("Hello world")


import tokens
import requests
import json

token = tokens.ALPHAVANTAGE

ticker_list= ['GME', 'STIC', 'NIO', 'PLTR', 'TSLA', 'BABA', 'AAPL', 'DKNG', 'MT',
'IPOC', 'FCEL', 'PENN', 'NKLA', 'ARK', 'QS', 'GILD', 'PSTH', 'MVIS', 'TLRY','MARA','CRSR','ETSY','CHWY','MRNA','FVRR']

timeSeries = ['TIME_SERIES_DAILY','TIME_SERIES_WEEKLY','TIME_SERIES_MONTHLY']


interval = ['1min', '5min', '15min','30min','60min']

endpoint = 'https://www.alphavantage.co/query'


def retrieveData():
    # create a formatted string of the Python JSON object
    payload = {'function': 'TIME_SERIES_DAILY', 'symbol': 'TSLA', 'apikey': token }
    response = requests.get(endpoint, params=payload)
    text = json.dumps(response.json(), sort_keys=True, indent=2)
    print(text)


if __name__ == "__main__":
    retrieveData()