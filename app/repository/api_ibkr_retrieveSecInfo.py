print("Hello world")

from connect import connect
import requests
import json

headers = { 'content-type': 'application/json;charset=utf-8' }

ticker_list= ['GME', 'STIC', 'NIO', 'PLTR', 'TSLA', 'BABA', 'AAPL', 'DKNG', 'MT',
'IPOC', 'FCEL', 'PENN', 'NKLA','QS', 'GILD', 'PSTH', 'MVIS', 'TLRY','MARA','CRSR','ETSY','CHWY','MRNA','FVRR','AAPL','ADBE','ADI','ADP','ADSK','AEP','ALGN','ALXN','AMAT','AMD','AMGN','AMZN','ANSS','ASML','ATVI','AVGO','BIDU','BIIB','BKNG','CDNS','CDW','CERN','CHKP','CHTR','CMCSA','COST','CPRT','CSCO','CSX','CTAS','CTSH','DLTR','DOCU','DXCM','EA','EBAY','EXC','FAST','FB','FISV','FOX','FOXA','GILD','GOOG','GOOGL','IDXX','ILMN','INCY','INTC','INTU','ISRG','JD','KDP','KHC','KLAC','LRCX','LULU','MAR','MCHP','MDLZ','MELI','MNST','MRNA','MRVL','MSFT','MTCH','MU','MXIM','NFLX','NTES','NVDA','NXPI','OKTA','ORLY','PAYX','PCAR','PDD','PEP','PTON','PYPL','QCOM','REGN','ROST','SBUX','SGEN','SIRI','SNPS','SPLK','SWKS','TCOM','TEAM','TMUS','TSLA','TXN','VRSK','VRSN','VRTX','WBA','WDAY','XEL','XLNX','ZM']

def getConId():
    # create a formatted string of the Python JSON object
    endpoint="https://localhost:8080/v1/api/iserver/secdef/search"
    for x in ticker_list:
        print(x)
        payload = { 'symbol': x }
        r = requests.get(endpoint, headers=headers, params=payload, verify=False).json()

        data = ({key: r[0][key] for key in r[0].keys() & { 'conid','symbol' }})
        data['companyname']=r[0]['companyName']
        data['opt']=[r[0]['opt']]
        formatted = json.dumps(data)
        query = "INSERT INTO vol.conid SELECT * from json_populate_record(NULL::vol.conid,'{}') \
         ON CONFLICT (conid) DO UPDATE SET(opt) = \
              (SELECT opt FROM json_populate_record (NULL::vol.conid,'{}'))".format(formatted,formatted)

        results = connect(query,"insert")
        print(results, '', x)


if __name__ == "__main__":
    getConId()