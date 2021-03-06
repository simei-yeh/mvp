print("Hello world")

import os
import sys
sys.path.append(os.path.realpath('.'))
from database.connect import insert, fetch
import requests
import json
from database.stored_proc import add_stocks

headers = { 'content-type': 'application/json;charset=utf-8' }

timeOpts = [{'bar': '1d', 'period': '9m'}, {'bar': '1w', 'period': '140w'}, {'bar': '30min', 'period': '2w'}, {'bar':'15min','period':'1w'}, {'bar':'5min','period':'1d'}]

def getConId():
    # create a formatted string of the Python JSON object
    endpoint="https://localhost:8080/v1/api/iserver/marketdata/history"

    query0 = "SELECT conid from vol.conid"
    conids = fetch(query0)

    for x in conids:
      for y in timeOpts:
        payload = dict({ 'conid': x[0] }, **y)
        try:
          r = requests.get(endpoint, headers=headers, params=payload, verify=False).json()
          # print(x,y, r)
          stockData = ({key.lower() : r[key] for key in r.keys() & { 'timePeriod','symbol','barLength','volumeFactor','priceFactor','data' }})
          stockData['stockcode'] = '{}-{}-{}'.format(r['symbol'],r['timePeriod'],payload['bar'])
          stockData['bar'] = '{}'.format(payload['bar'])
        except Exception as exc:
          print ('could not receive stock data ', exc)
          print ('first catch', x, y)
          pass

        formatted = [json.dumps(stockData)]

        # print(formatted)
        try:
          add_stocks(formatted)
        except Exception as exc:
          print('could not insert ', exc)
          print('second catch ', x, y)
          pass


if __name__ == "__main__":
    getConId()