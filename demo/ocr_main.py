#-*- coding: UTF-8 -*-
import sys
import optparse
import time
import apiutil
import base64
import json
import os
import base64, hashlib, json, cv2, random, string, time
from frame import getPicFrameMain

from config import APP_ID, API_KEY, ratio

app_key = API_KEY
app_id = APP_ID
 
def Recognise(img_path):
    with open(img_path, 'rb') as bin_data:
        image_data = bin_data.read()
    nonce = ''.join(random.sample(string.digits + string.ascii_letters, 32))
    stamp = int(time.time())
    ai_obj = apiutil.AiPlat(app_id, app_key)
    rsp = ai_obj.getOcrGeneralocr(image_data)
    # print rsp
    if rsp and rsp['ret'] == 0:
        datas = rsp['data']['item_list']
        return datas
    else:
        # 重试
        return None

def RecogniseAll():
    # outputDir, concatOutputDir = getPicFrameMain()
    outputDir = '/Users/chenxinyi/Documents/learn/py_aiplat_demo/video/第一部里面隐藏的那些彩蛋你找到了吗'
    concatOutputDir = '/Users/chenxinyi/Documents/learn/py_aiplat_demo/video/第一部里面隐藏的那些彩蛋你找到了吗/concat'
    
    start = int(time.time())
    print('-------------------------------')
    print('Running Start: ' + str(start))
    print('-------------------------------')
    output = open(outputDir + '/' + str(start) + '.txt', 'a')
    imgDir = sorted(os.listdir(concatOutputDir))
    positionData = []
    allWords = []

    for img_name in imgDir:
        img_path = concatOutputDir + '/' + img_name
        recognise_dic = Recognise(img_path)
        time.sleep(1)

        if recognise_dic is None:
            # 重试逻辑
            continue

        for item in recognise_dic:
              word = item['itemstring'].encode('utf8').strip()
              if word != '' and word not in allWords:
                  print('-------- KEYWORD %s --------'%(word))
                  allWords.append(word)
                  output.write('\n'+word)
                  output.flush()

    end = time.time()
    print('-------------------------------')
    print('Running time: ' + str(end - start))
    print('-------------------------------')
    output.close()

if __name__ == '__main__':
    RecogniseAll()
