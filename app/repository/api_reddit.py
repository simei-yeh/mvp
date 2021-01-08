print("Hello world")

from connect import fetch
from flask_socketio import SocketIO
import random
import tokens
import requests
import json
import threading

user = tokens.REDDITUSER
endpoint_list = ['hot','new','rising','top']
headers = { 'User-Agent' : user }
payload = {'g': 'GLOBAL', 'count': '100', 'limit': '100'}


substring_list = ['takeoff', 'moon', u"\U0001f48e", u"\U0001F680", "\ud83d\ude80",u"\uE11D", u"\uE04C", 'gang', 'calls', 'thank you','diamond hand','tendies', 'yolo', 'bought', 'short squeeze', 'squeeze', 'tendy', 'tendie', 'thanks', 'home run', 'gain','bulls','gang']

ticker_list= ['GME', 'STIC', 'NIO', 'PLTR', 'TSLA', 'BABA', 'AAPL', 'DKNG', 'MT',
'IPOC', 'FCEL', 'PENN', 'NKLA', 'QS', 'GILD', 'PSTH', 'MVIS', 'TLRY','MARA','CRSR','ETSY','CHWY','MRNA','FVRR']

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
                    'corsair': 'CRSR',
                    'tilray': 'TLRY'}

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()
        print('done with interval request')


def scrapeReddit():
    count = 0

    for x in endpoint_list:
        endpoint = 'https://www.reddit.com/r/wallstreetbets/{}.json'.format(x)
        r = requests.get(endpoint, headers=headers, params=payload).json()

        for x in r['data']['children']:
            s = x['data']
            temp = '{}{}'.format(s['title'], s['selftext'])


            if any( y.lower() in temp for y in substring_list ):
              #  (any( a.upper() in temp for a in ticker_list) or any (a.lower() in temp for a in ticker_alias.keys()))
              for a in [x for x in ticker_list if x in temp] + [val for key,val in ticker_alias.items() if key in temp]:
                count += 1
                formatData = {key: s[key] for key in s.keys() & {'ups', 'upvote_ratio','score','num_comments','created','name' }}
                data = dict({'ticker': a, 'rankcode': '{}-{}'.format(a,s['name']), 'weighted_score': round(s['ups']*s['upvote_ratio']+0.75*s['num_comments'],3)}, **formatData)
                queryObj=json.dumps(data)

                query = "INSERT INTO vol.wsb SELECT * FROM json_populate_record (NULL::vol.wsb,'{}') \
                  ON CONFLICT (rankcode) DO UPDATE SET(score,ups,upvote_ratio,num_comments,weighted_score) = (SELECT score,ups,upvote_ratio,num_comments,weighted_score FROM json_populate_record (NULL::vol.wsb,'{}'))".format(queryObj, queryObj)

                results = fetch(query,"insert")
                # print(results)
    print(count)

if __name__ == "__main__":
    scrapeReddit()