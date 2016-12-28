import json
import copy
import sys
sys.path.append('/Library/Python/2.7/site-packages')
import requests
import datetime

resp = requests.get('http://fyndox.herokuapp.com/api/selectFeeds')
data = resp.json()

#js = open('biz.json','r', encoding = 'utf-8')
#data = json.load(js) # deserializing json format into lists
print('The total number of feeds is - ' + str(len(data)))


# setting date correctly
# setting initial list of category
cats=[]
for i in range(len(data)):
    datee = data[i]['dateOfPost']
    data[i]['dateOfPost'] = str(int(data[i]['dateOfPost'])/1000)[0:10]
    
    data[i]['dateOfPost'] = data[i]['dateOfPost'].split('-')
    for i in range(500,550):
        print(data[i]['dateOfPost'])
    cats.append(str(data[i]['sourceDevice']))
print('Dates have been set as year, month, day.')
cats = list(set(cats))
print('Categories identified & copied.')


# setting initial dictionary for feeds counter by category
fbc = dict()
for i in range(len(cats)):
    fbc[cats[i]] = 0
fbcd = copy.deepcopy(fbc)
fbcda = copy.deepcopy(fbc)
print('Initial feeds dictionary set & copied.')


# getting feeds by date & area
def getfeedsbydate():   
    day = input('Please enter date - ')
    month = input('Please enter month - ')
    dm = ['2016',str(month),str(day)]
    ct2 = 0
    ct3 = 0
    arealist = []
    feedst = []
    x=0   
    for i in range(len(data)):
        if 'Chennai'.lower() in str(data[i]['shopArea']).lower():
            if data[i]['dateOfPost'] == dm:
                ct2 = ct2+1
                arlt=[]
                feedst.append(data[i])
                areaf = str(data[i]['shopArea'])           
                arlt = areaf.split(', ')
                if int(len(arlt))>2:
                    for j in range(len(arlt)):
                        if str(arlt[j].lower()) == 'Chennai'.lower():
                            x=j
                    arealist.append(arlt[x-1])
    arealist = list(set(arealist))
    print('\nThe total number of feeds for the day is - ' + str(ct2))
    print('The list of areas for the period ' + str(dm) + ' is below - ')
    print(arealist)
    print('\n')
    
    for i in range(len(arealist)):
        ct3 = 0
        for keys in fbcda:
            fbcda[keys]=0
        for j in range(len(feedst)):
            areaf = str(feedst[j]['shopArea'])
            if str(arealist[i]).lower() in areaf.lower():
                fbcda[str(feedst[j]['sourceDevice'])] = fbcda[str(feedst[j]['sourceDevice'])]+1
                ct3 = ct3+1               
        print('Feeds for ' + str(arealist[i]) +' on ' + str(dm) + ' is - ' + str(ct3) +'\n')
        sl2 = sorted(fbcda,key=fbcda.__getitem__,reverse = True)
        for key in sl2:
            print(key + " - " + str(fbcda[key]))
        print('\n\n')
    getuserinput()
        

# getting feeds by DATE RANGE & area -
def setdaterange():   
    day1 = input('Please enter starting date - ')
    month1 = input('Please enter starting month - ')
    day2 = input('Please enter ending date - ')
    month2 = input('Please enter ending month -')
    dm1 = ['2016',str(month1),str(day1)]
    dm2 = ['2016',str(month2),str(day2)]
    feedst=[]
    for i in range(len(data)):
        if 'Chennai'.lower() in str(data[i]['shopArea']).lower():
            if int(data[i]['dateOfPost'][1]) >= int(dm1[1]) and int(data[i]['dateOfPost'][1]) <= int(dm2[1]):
                if dm1[1] == dm2[1]:
                    if int(data[i]['dateOfPost'][2]) >= int(dm1[2]) and int(data[i]['dateOfPost'][2]) <= int(dm2[2]):
                               feedst.append(data[i])                                              
                else:
                       if int(data[i]['dateOfPost'][1]) == int(dm1[1]):
                           if int(data[i]['dateOfPost'][2]) >= int(dm1[2]):
                               feedst.append(data[i])                           
                       elif int(data[i]['dateOfPost'][1]) == int(dm2[1]):
                           if int(data[i]['dateOfPost'][2]) <= int(dm2[2]):
                               feedst.append(data[i])
                       else:
                           feedst.append(data[i])
                      
    getfeedsbyrange(feedst,dm1,dm2)

def getfeedsbyrange(f,x,y):
    feedst = f
    dm1 = x
    dm2 = y
    arlt=[]
    arealist = []
    for i in range(len(feedst)):
        areaf = str(feedst[i]['shopArea'])           
        arlt = areaf.split(', ')
        if int(len(arlt))>2:
            for j in range(len(arlt)):
                if str(arlt[j].lower()) == 'Chennai'.lower():
                    x=j
            arealist.append(arlt[x-1])
    arealist = list(set(arealist))
    print('\nThe total number of feeds for the period ' + str(dm1) + ' to '+ str(dm2) +' is - ' + str(len(feedst)))
    print('The list of areas for the period is below - ')
    print(arealist)
    print('\n')
    for i in range(len(arealist)):
        ct3 = 0
        for keys in fbcda:
            fbcda[keys]=0
        for j in range(len(feedst)):
            areaf = str(feedst[j]['shopArea'])
            if str(arealist[i]).lower() in areaf.lower():
                fbcda[str(feedst[j]['sourceDevice'])] = fbcda[str(feedst[j]['sourceDevice'])]+1
                ct3 = ct3+1
        print('Feeds for ' + str(arealist[i]) +' for the period '+ str(dm1) +' to '+ str(dm2) +' - ' + str(ct3) +'\n')
        sl2 = sorted(fbcda,key=fbcda.__getitem__,reverse = True)
        for key in sl2:
            print(key + " - " + str(fbcda[key]))
        print('\n\n')

    getuserinput()


#getting user input
def getuserinput():
    userinput = input('Press 1 for reports on a day\nPress 2 for reports for a period\nPress 3 for exit\n')
    if str(userinput) == '1':
        getfeedsbydate()
    elif str(userinput) == '2':
        setdaterange()
    else:
        exit()

# setting total feeds by category counter
ct1 = 0
for i in range(len(data)):
    ct1 = ct1+1
    fbc[str(data[i]['sourceDevice'])] = fbc[str(data[i]['sourceDevice'])]+1
print('Total feeds dictionary values done - ' + str(ct1) + '\n')
sl1 = sorted(fbc,key=fbc.__getitem__,reverse = True)
for key in sl1:
    print(key + " - " + str(fbc[key]))
print('\n\n')
getuserinput()
