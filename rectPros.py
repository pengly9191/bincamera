"""
Created on 2016.09.06

"""
import cv2
from  matplotlib import pyplot as plt
import Image
import numpy as np
from glob import glob
from common import splitfn


PATH_IN = "/home/ply/stereo/data/out"
PATH_OUT = "/home/ply/stereo/data/rectout"
if __name__ == '__main__':

    img_mask = PATH_IN + '/*.jpg'
    img_names = glob(img_mask)

    for fn in img_names:
        src = cv2.imread(fn)
     #   gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        h0, w0 = src.shape[:2]

        src[0:60, :] = 0
        src[h0-100:h0,:] = 0
        src[:,w0/2-200:w0/2+20]= 0
        src[:, w0-50:w0] = 0

        # img1 = src[:, 0:w0 / 2]
        # img2 = src[:, w0 / 2:w0]

        # IMAGE_PATH1 = "/home/ply/L.jpg"
        # IMAGE_PATH2 = "/home/ply/R.jpg"
        # ret, img1 = cv2.threshold(img1, 1, 255, cv2.THRESH_BINARY)
        # ret, img2 = cv2.threshold(img2, 1, 255, cv2.THRESH_BINARY)

        # img1 = img1[100:h0, 100:w0/2 - 250]
        # cv2.imwrite(IMAGE_PATH1, img1)
        # img2 = img2[100:h0, 100:w0/2 - 250]
        # cv2.imwrite(IMAGE_PATH2, img2)

        # h,w = img1.shape[:2]
        # dst = np.zeros((h, 2*w, 3), np.uint8)
        # dst[0:h,0:w]= img1
        # dst[0:h, w:2*w ] = img2
        # dst = dst[0:h-20,:]
#        dst = cv2.resize(dst,(w0,h0))




        path, name, ext = splitfn(fn)
        cv2.imwrite(PATH_OUT+'/%s.jpg'%(name),src)


