import requests
import json

url = 'http://fyndox.herokuapp.com/api/selectFeeds'
urlupdate = 'http://fyndox.herokuapp.com/api/updateFeed'


fr = requests.get(url)
feeds = fr.json()
d = {
  "feedId": '',
  "bizId": '',
  "expiryDate": '',
  "dateOfPost": '',
  "shopName" : '',
  "shopArea" : ''
}

def updatefeedtime():

    x = input('Enter starting feed -')
    y = input('Enter ending feed -')

    for i in range(len(feeds)):
        if int(feeds[i]['feedId']) >= int(x) and int(feeds[i]['feedId']) <= int(y):
            for keys in d:
                d[keys] = ''
                d[keys] = feeds[i][keys]
            if int(feeds[i]['feedId']) <= 2411:
                d['dateOfPost'] = '1480073400'
            else:
                d['dateOfPost'] = '1480159800'
                
            r = requests.post(urlupdate, data = json.dumps(d), headers = {'Content-type': 'application/json'})
            
            if r.status_code == 200:
                    print('updated - ' + str(feeds[i]['feedId']))
            else:
                    print('Not update -' + str(feeds[i]['feedId']))
                    print(r.reason)
