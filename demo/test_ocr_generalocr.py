#-*- coding: UTF-8 -*-
import sys
# sys.path.append('../SDK')  
import optparse
import time
import apiutil
import base64
import json

from config import APP_ID
from config import API_KEY

app_key = API_KEY
app_id = APP_ID

if __name__ == '__main__':
    with open('/Users/chenxinyi/Documents/learn/py_aiplat_demo/data/generalocr.jpg', 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)

    print '----------------------SEND REQ----------------------'
    rsp = ai_obj.getOcrGeneralocr(image_data)

    if rsp['ret'] == 0:
        for i in rsp['data']['item_list']:
            print i['itemstring'] 
        print '----------------------API SUCC----------------------'
    else:
        print json.dumps(rsp, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
        print '----------------------API FAIL----------------------'
