#-*- coding: UTF-8 -*-
import sys, base64, time, os
from frame import getPicFrameMain
from txyun_sdk import requestOrc

from config import ratio
 
def Recognise(img_path):
    with open(img_path, 'rb') as file:
        base64_data = base64.b64encode(file.read())
    params = '{\"ImageBase64\":\"'+base64_data.decode('utf8')+'\"}'
    # print(params)
    rsp = requestOrc(params)
    # print rsp
    if rsp and rsp['TextDetections']:
        datas = rsp['TextDetections']
        return datas
    else:
        # 重试
        return None

def RecogniseAll():
    outputDir, concatOutputDir = getPicFrameMain()
    # outputDir = '/Users/chenxinyi/Documents/demo/learn/txyun_video_ocr/video/224157804-1-32'
    # concatOutputDir = '/Users/chenxinyi/Documents/demo/learn/txyun_video_ocr/video/224157804-1-32/concat'
    
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
              word = item['DetectedText'].encode('utf8').strip()
              word = word.decode('utf8')
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
