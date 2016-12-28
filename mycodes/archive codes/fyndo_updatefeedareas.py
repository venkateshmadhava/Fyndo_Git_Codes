import json
import copy
import sys
sys.path.append('/Library/Python/2.7/site-packages')
import requests


urlbiz = 'http://fyndo.herokuapp.com/api/selectBizInfos'
bizresp = requests.get(urlbiz)
biz = bizresp.json()

urlfeed = 'http://fyndox.herokuapp.com/api/selectFeeds'
feedresp = requests.get(urlfeed)
feeds = feedresp.json()

urlupdate = 'http://fyndox.herokuapp.com/api/updateFeed'

bizdic = {}

def updatefeedarea():
    x = input('Enter starting feed id -')
    y = input('Enter ending feed id - ')
    x = int(x)
    y = int(y)
    bizdic = {}
    for i in range(len(biz)):
        l = []
        l.append(biz[i]['bizName'])
        l.append(biz[i]['bizArea'])
        bizdic[biz[i]['bizId']] = l

    for i in range(len(feeds)):
        d={}
        d['feedId'] = feeds[i]['feedId']
        d['bizId'] = biz[j]['bizId']
        d['expiryDate'] = feeds[i]['expiryDate']
        d['dateOfPost'] = feeds[i]['dateOfPost']
        
        
        
    
