# -*- coding: utf-8 -*-
import requests
import json
import hashlib
#import time


data = '''
{
    "APP_HEAD" : {
    },
    "BODY" : {
        "CHANNEL_CODE":"01"
    },
    "LOCAL_HEAD" : { },
     "SYS_HEAD": {
        "DEST_BRANCH_NO": "1",
        "SERVICE_CODE": "MbsdPays",
        "MESSAGE_TYPE": "1400",
        "USER_ID": "MBU001",
        "TRAN_TIMESTAMP": "142810111",
        "AUTH_FLAG": "N",
        "PROGRAM_ID": "MT",
        "SEQ_NO": "CGY11124342223323433",
        "SOURCE_TYPE": "01",
        "TRAN_MODE": "ONLINE",
        "USER_LANG": "AMERICAN/ENGLISH",
        "MESSAGE_CODE": "172208",
        "TRAN_DATE": "20181220",
        "SOURCE_BRANCH_NO": "1",
        "LOG_ID": "GATE-f6457241-19ea-4652-8bbb-50278d5dd48e",
        "BRANCH_ID": "999"
    }
}
'''

print("BODY REQUEST: \n"+data)

response = requests.post("http://smart-payment-dev1.bankbkemobile.co.id/HttpServer", data = data)
print(response.json())
print(response.text)
tx = response.text
js = response.json()
du = json.dumps(js,sort_keys=True,indent=4, separators=(', ', ': '))
jl = json.loads(tx)
print(du)
print(jl)