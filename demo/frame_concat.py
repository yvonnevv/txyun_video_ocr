#encoding:utf-8  

# 图片拼接
import cv2
import os
from config import ratio, concat_num
import time

def concatFrames(outputDir):
    frameOutputDir = outputDir + '/frames'
    concatOutputDir = outputDir + '/concat'

    if not os.path.exists(concatOutputDir):
        os.mkdir(concatOutputDir)

    imgDir = sorted(os.listdir(frameOutputDir))
    concat_imgs = []
    index = 0
    for img_name in imgDir:
        index += 1
        img_path = frameOutputDir + '/' + img_name
        im = cv2.imread(img_path)
        height, width = im.shape[:2]
        crop_im = im[int((1 - ratio) * height):height, 0:width]
        c_index = index//concat_num
        if len(concat_imgs) < c_index + 1:
            print 'c_index', c_index
            concat_imgs.append([])

        concat_imgs[c_index].append(crop_im)
    
    name_idx = 0
    for item in concat_imgs:
        # 垂直拼接
        name_idx += 1
        new_im = cv2.vconcat(item)
        new_im_resize = cv2.resize(new_im, (new_im.shape[1],new_im.shape[0]), interpolation=cv2.INTER_AREA)
        cv2.imwrite(concatOutputDir + '/' + str(name_idx).zfill(10) + '.jpg', new_im_resize)

    return concatOutputDir

# if __name__ == '__main__':
#     outputDir = '/Users/chenxinyi/Documents/learn/py_aiplat_demo/video/【文曰小强】纪念我们永远的魔法世界《哈利·波特与魔法石》'
#     concatFrames(outputDir)