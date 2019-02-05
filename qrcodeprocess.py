#!/usr/bin/python3
import json
import sys
from databaseprolib import databaseProcess
from geolite2 import geolite2 as geo# geolite2 is the lib to get location of ip address

print ("Content-Type: text/html\n\n")
# connect to the database get
try:
    aclog.log("conncet to the database.")
    dbp = databaseProcess('user','password','host','database name')
    #dbp.connect()
except Exception as err:
    errorlog.log('Database error : {}'.format(err))
    print('<h1 style="color:red">Error : {}</h1>'.format(err))
    print('\n')
    sys.exit()

#get data from client by json
data=sys.stdin.read()

params=json.loads(data) #type = kind of command

ctype = params['type']
jpurl = params['p1']#for ctype 'access' jpurl = ip
enurl = params['p2']#for ctype 'access' enurl = country
produceid = params['p3']
version = params['p4']
modeid = params['p5']
submodeid = params['p6']
menuid = params['p7']
mac=params['p8']
if(ctype=='update'):
    try:
        res=dbp.insertQrUrl(jpurl,enurl,produceid,version,modeid,submodeid,menuid)
        print(res)
    except Exception as err:
        errorlog.log('error in update qrcode table : {}'.format(err))
        print(err)
elif(ctype=='access'):
    try:
       re=geo.reader()
       _c=re.get(jpurl)#get ip address info
       enurl=_c['country']['iso_code']#take the iso_code of country
       res=dbp.accessQrUrl(produceid,version,modeid,submodeid,menuid,jpurl,enurl,mac)
       print(res)
    except Exception as err:
        errorlog.log('error in access  qrcode table : {}'.format(err))
        print(err)
print ("\n")
