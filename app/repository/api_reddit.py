print("Hello world")

from connect import connect
import tokens
import requests
import json
import re
import threading
import time

user = tokens.REDDITUSER
endpoint_list = ['hot','new','rising','top']
headers = { 'User-Agent' : user }
payload = {'g': 'GLOBAL', 'count': '100', 'limit': '100'}


substring_list = ['takeoff', 'moon', u"\U0001F680", u"\uE11D", u"\uE04C", 'gang', 'calls', 'thank you', 
'tendies', 'yolo', 'bought', 'short squeeze', 'squeeze', 'tendy', 'tendie', 'thanks', 'home run', 'gain']

ticker_list= ['GME', 'STIC', 'NIO', 'PLTR', 'TSLA', 'BABA', 'AAPL', 'DKNG', 'MT', 
'IPOC', 'FCEL', 'PENN', 'NKLA', 'ARK', 'QS', 'GILD', 'PSTH', 'MVIS', 'TLRY','MARA']

ticker_alias= {'game stop': 'GME', 
                    'gamestop': 'GME',
                    'palantir': 'PLTR', 
                    'tesla' : 'TSLA',
                    'alibaba': 'BABA', 
                    'draftkings': 'DKNG', 
                    'apple': 'AAPL',
                    'fuelcell energy': 'FCEL',
                    'nikola': 'NKLA',
                    'gilead': 'GILD',
                    'tilray': 'TLRY'}

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()
        print('done with interval request')


def scrapeReddit():
    matches = {}
    count = 0

    for x in endpoint_list:
        endpoint = 'https://www.reddit.com/r/wallstreetbets/{}.json'.format(x)
        r = requests.get(endpoint, headers=headers, params=payload).json()

        for x in r['data']['children']:
            s = x['data']
            temp = '{}{}'.format(s['title'], s['selftext'])

            if any( y.lower() in temp for y in substring_list ) and (any( a.upper() in temp for a in ticker_list) 
            or any (a.lower() in temp for a in ticker_alias.keys())):
                formatData = {key: s[key] for key in s.keys() 
                    & {'ups', 'upvote_ratio','score','num_comments','created','name' }}
                formatData['ticker'] =  [x for x in ticker_list if x in temp] + [val for key,val in ticker_alias.items() if key in temp]
                queryObj=json.dumps(formatData)

                query = "INSERT INTO vol.wsb SELECT * FROM json_populate_record (NULL::vol.wsb,'{}') \
                    ON CONFLICT (name) DO UPDATE SET(created,name,ticker,score,ups,upvote_ratio,num_comments)= \
                        (SELECT * FROM json_populate_record (NULL::vol.wsb,'{}'))".format(queryObj, queryObj)
                
                # created,name,ticker,score,ups,upvote_ratio,num_comments
               
                results = connect(query,"insert")    

if __name__ == "__main__":
    setInterval(scrapeReddit,300)