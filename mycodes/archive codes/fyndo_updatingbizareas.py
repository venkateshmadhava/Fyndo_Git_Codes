import json
import copy
import sys
sys.path.append('/Library/Python/2.7/site-packages')
import requests

urlbiz = 'http://fyndox.herokuapp.com/api/selectBizInfos'
bizresp = requests.get(urlbiz)
biz = bizresp.json()

urlupdate = 'http://fyndox.herokuapp.com/api/updateBizInfo'

apikey = 'AIzaSyA0q6Ho_hLDnwFfL2G9je5d016dq-j0nCo'

up = {
    "bizId": 0,
    "bizName": "",
    "bizDesc": "",
    "bizType": "",
    "bizArea": "",
    "bizMobile": "",
    "bizCategory": "",
    "userRelation" : "",
    "bizProfile" : "",
    "gpsLatitude": 0,
    "gpsLongitude": 0,
    "fyndoUserId" : ""
  }

def updatearea():
    x = input('Enter starting biz id - ')
    y = input('Enter ending biz id - ')
    h=1
    missedbiz=[]
    errorbiz = []
    for i in range(len(biz)):
        if int(biz[i]['bizId']) >= int(x) and int(biz[i]['bizId']) <= int(y):
            if biz[i]['gpsLatitude'] == 0 or biz[i]['gpsLongitude'] == 0 or biz[i]['gpsLatitude'] == "" or biz[i]['gpsLongitude'] == "":
                missedbiz.append(biz[i])
            else:
                mainarea = ""
                f = 0
                lat = biz[i]['gpsLatitude']
                long = biz[i]['gpsLongitude']
                urlapi = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+str(lat)+','+str(long)+'&key='+apikey
                r = requests.get(urlapi)
                add = r.json()
                #print(add)
                c = 0
                if len(add['results']) == 1:
                    c=0
                else:
                    c=1
                areab = str(add['results'][c]['formatted_address'])
                print('Address gathered is-' + areab)
                arlt = areab.split(', ')
                if int(len(arlt))>2:
                    for j in range(len(arlt)):
                        if str(arlt[j].lower()) == 'Chennai'.lower():
                            h=j
                            f = 1
                    if f == 0:
                        for j in range(len(arlt)):
                            if 'Tamil Nadu'.lower() in str(arlt[j].lower()):
                                h=j
                                f = 1
                if f == 1:
                    mainarea = str(arlt[h-1])
                    #print('The main area - ' + str(mainarea))
                    up['bizId'] = biz[i]['bizId']
                    up['bizName'] = biz[i]['bizName']
                    up['bizDesc'] = biz[i]['bizDesc']
                    up['bizType'] = biz[i]['bizType']
                    up['bizMobile'] = biz[i]['bizMobile']
                    up['bizCategory'] = biz[i]['bizCategory']
                    up['userRelation'] = biz[i]['userRelation']
                    up['bizProfile'] = biz[i]['bizProfile']
                    up['gpsLatitude'] = biz[i]['gpsLatitude']
                    up['gpsLongitude'] = biz[i]['gpsLongitude']
                    up['fyndoUserId'] = biz[i]['fyndoUserId']
                    up['bizArea'] = mainarea
                    bup = requests.post(urlupdate, data = json.dumps(up), headers = {'Content-type': 'application/json'})
                    if bup.status_code == 200:
                        print('Biz updated - ' + str(biz[i]['bizId']))
                    else:
                        errorbiz.append(biz[i])
                else:
                    mainarea = ""
                    errorbiz.append(biz[i])
                
               
    print('\n')
    print('Biz wth gps value zero or null - ')
    for i in range(len(missedbiz)):
        print(str(missedbiz[i]['bizId']) + ' - ' + str(missedbiz[i]['bizName']))

    print('\n')
    print('Biz wth gps value correct but cudnt update - ')
    for i in range(len(errorbiz)):
        print(str(errorbiz[i]['bizId']) + ' - ' + str(errorbiz[i]['bizName']))
            
            
    
