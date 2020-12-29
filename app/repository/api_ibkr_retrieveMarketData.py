print("Hello world")

from connect import connect
import requests
import json

headers = { 'content-type': 'application/json;charset=utf-8' }

def getConId():
    # create a formatted string of the Python JSON object
    endpoint="https://localhost:8080/v1/api/iserver/marketdata/history"

    query0 = "SELECT conid from vol.conid"
    conids = connect(query0, "fetch")

    for x in conids:
      payload = { 'conids': x[0] }
      print(payload)
    #   r = requests.get(endpoint, headers=headers, params=payload, verify=False).json()

    #     data = ({key: r[0][key] for key in r[0].keys() & { 'conid','symbol' }})
    #     data['companyname']=r[0]['companyName']
    #     data['opt']=[r[0]['opt']]
    #     formatted = json.dumps(data)
    #     query = "INSERT INTO vol.conid SELECT * from json_populate_record(NULL::vol.conid,'{}') \
    #      ON CONFLICT (conid) DO UPDATE SET(opt) = \
    #           (SELECT opt FROM json_populate_record (NULL::vol.conid,'{}'))".format(formatted,formatted)

    #     results = connect(query,"insert")
    #     print(results, '', x)


if __name__ == "__main__":
    getConId()