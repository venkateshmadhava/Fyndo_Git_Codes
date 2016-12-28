import json
import copy
import sys
sys.path.append('/Library/Python/2.7/site-packages')
import requests

urlbiz = 'http://fyndox.herokuapp.com/api/selectBizInfos'
bizresp = requests.get(urlbiz)
biz = bizresp.json()

feedresp = requests.get('http://fyndox.herokuapp.com/api/selectFeeds')
feeds = feedresp.json()

urlupdate = 'http://fyndox.herokuapp.com/api/updateBizInfo'

bizdic = {1460: ' ',1459: ' ',1458: ' ',1457: ' ',1456: ' ',1455: ' ',1454: ' ',1453: ' ',1452: ' ',1451: ' ',1450: ' ',1449: ' ',1448: ' ',1447: ' ',1446: ' ',1445: ' ',1444: ' ',1443: ' ',1442: ' ',1391: ' ',1390: ' ',1389: ' ',1388: ' ',1387: ' ',1386: ' ',1385: ' ',1384: ' ',1383: ' ',1382: ' ',1381: ' ',1380: ' ',1379: ' ',1378: ' ',1377: ' ',1376: ' ',1375: ' ',1374: ' ',1373: ' ',1372: ' ',1371: ' ',1370: ' ',1369: ' ',1368: ' ',1367: ' ',1366: ' ',1365: ' ',1364: ' ',1363: ' ',1362: ' ',1361: ' ',1360: ' ',1359: ' ',1358: ' ',1357: ' ',1356: ' ',1355: ' ',1354: ' ',1353: ' ',1352: ' ',1351: ' ',1350: ' ',1349: ' ',1348: ' ',1347: ' ',1346: ' ',1345: ' ',1344: ' ',1343: ' ',1342: ' ',1341: ' ',1340: ' ',1339: ' ',1338: ' ',1337: ' ',1336: ' ',1335: ' ',1334: ' ',1333: ' ',1332: ' ',1331: ' ',1330: ' ',1329: ' ',1328: ' ',1327: ' ',1326: ' ',1325: ' ',1324: ' ',1323: ' ',1322: ' ',1321: ' ',1320: ' ',1319: ' ',1318: ' ',1317: ' ',1316: ' ',1315: ' ',1314: ' ',1313: ' ',1312: ' ',1311: ' ',1310: ' ',1309: ' ',1308: ' ',1307: ' ',1306: ' ',1305: ' ',1304: ' ',1303: ' ',1302: ' ',1301: ' ',1300: ' ',1299: ' ',1298: ' ',1297: ' ',1296: ' ',1295: ' ',1294: ' ',1293: ' ',1292: ' ',1291: ' ',1290: ' ',1289: ' ',1288: ' ',1287: ' ',1286: ' ',1285: ' ',1284: ' ',1283: ' ',1282: ' ',1281: ' ',1280: ' ',1279: ' ',1278: ' ',1277: ' ',1276: ' ',1275: ' ',1274: ' ',1273: ' ',1272: ' ',1271: ' ',1270: ' ',1269: ' ',1268: ' ',1267: ' ',1266: ' ',1265: ' ',1264: ' ',1263: ' ',1262: ' ',1261: ' ',1260: ' ',1259: ' ',1258: ' ',1257: ' ',1256: ' ',1255: ' ',1254: ' ',1253: ' ',1252: ' ',1251: ' ',1250: ' ',1249: ' ',1248: ' ',1247: ' ',1246: ' ',1245: ' ',1244: ' ',1243: ' ',1242: ' ',1241: ' ',1240: ' ',1236: ' ',1235: ' ',1234: ' ',1233: ' ',1232: ' ',1231: ' ',1075: ' ',1239: ' ',1238: ' ',1237: ' '}
print('The len of bizdic is - ' + str(len(bizdic)))

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

def updatecat():
    t = 0
    errbiz = []
    for i in range(len(feeds)):
        if feeds[i]['bizId'] in bizdic.keys():
            bizdic[feeds[i]['bizId']] = feeds[i]['textContent']

    for i in range(len(biz)):
        up = {}
        if biz[i]['bizId'] in bizdic.keys():
            
            up['bizId'] = biz[i]['bizId']
            up['bizName'] = biz[i]['bizName']
            up['bizDesc'] = biz[i]['bizDesc']
            up['bizType'] = biz[i]['bizType']
            up['bizMobile'] = biz[i]['bizMobile']
            up['bizCategory'] = bizdic[biz[i]['bizId']]
            up['userRelation'] = biz[i]['userRelation']
            up['bizProfile'] = biz[i]['bizProfile']
            up['gpsLatitude'] = biz[i]['gpsLatitude']
            up['gpsLongitude'] = biz[i]['gpsLongitude']
            up['fyndoUserId'] = biz[i]['fyndoUserId']
            up['bizArea'] = biz[i]['bizArea']
            bup = requests.post(urlupdate, data = json.dumps(up), headers = {'Content-type': 'application/json'})
            if bup.status_code == 200:
                print('Biz updated - ' + str(biz[i]['bizId']))
                t = t +1
            else:
                errbiz.append(biz[i]['bizId'])
    print('Total biz on dict - ' + str(len(bizdic)) + '. Total biz updated - ' + str(t))

    if len(errbiz) >=1:
        print('Few biz were not updated - \n')
        for j in range(len(errbiz)):
            print(str(biz[i]['bizId']))
            

        

    
