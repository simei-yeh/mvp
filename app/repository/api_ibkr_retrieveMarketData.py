print("Hello world")

from connect import connect
import requests
import json

headers = { 'content-type': 'application/json;charset=utf-8' }

timeOpts = [{'bar': '1d', 'period': '1y'}, {'bar': '1w', 'period': '5y'}, {'bar': '30min', 'period': '1m'}, {'bar':'15min','period':'1w'}]

def getConId():
    # create a formatted string of the Python JSON object
    endpoint="https://localhost:8080/v1/api/iserver/marketdata/history"

    query0 = "SELECT conid from vol.conid"
    conids = connect(query0, "fetch")

    for x in conids:
      for y in timeOpts:
        payload = dict({ 'conid': x[0] }, **y)
        try:
          r = requests.get(endpoint, headers=headers, params=payload, verify=False).json()
          # print(x,y, r)
          stockData = ({key.lower() : r[key] for key in r.keys() & { 'timePeriod','symbol','barLength','volumeFactor','priceFactor','data' }})
          stockData['stockcode'] = '{}-{}-{}'.format(r['symbol'],r['timePeriod'],payload['bar'])
        except Exception as exc:
          print ('could not receive stock data ', exc)
          print ('first catch', x, y)
          pass


        formatted = json.dumps(stockData)
        query = "INSERT INTO vol.stocks SELECT * from json_populate_record(NULL::vol.stocks,'{}') ON CONFLICT (stockcode) DO UPDATE SET(data) = \
          (SELECT data FROM json_populate_record (NULL::vol.stocks,'{}'))".format(formatted,formatted)

        try:
          results = connect(query,"insert")
        except Exception as exc:
          print('could not insert ', exc)
          print('second catch ', x, y)
          pass


if __name__ == "__main__":
    getConId()