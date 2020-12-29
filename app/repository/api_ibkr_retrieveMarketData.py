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
        print(payload)
        r = requests.get(endpoint, headers=headers, params=payload, verify=False).json()

        data = ({key: r[0][key] for key in r[0].keys() & { 'conid','symbol' }})
        data['opt']=[r[0]['opt']]
        formatted = json.dumps(data)
        query = "INSERT INTO vol.stocks SELECT * from json_populate_record(NULL::vol.stocks,'{}') ON CONFLICT (stockCode) DO UPDATE SET(opt) = \
          (SELECT opt FROM json_populate_record (NULL::vol.stocks,'{}'))".format(formatted,formatted)

    #     results = connect(query,"insert")
    #     print(results, '', x)


if __name__ == "__main__":
    getConId()