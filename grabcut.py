from util import *
import numpy as np
import cv2
import sys

PATH_IN = global_path+'/left_right_Pic'
PATH_OUT = global_path+'/grabcut'

if __name__ == '__main__':

    img = cv2.imread(path+"/left-pic-0.jpg")
    img2 = img.copy()  # a copy of original image
    mask = np.zeros(img.shape[:2], dtype=np.uint8)  # mask initialized to PR_BG
    output = np.zeros(img.shape, np.uint8)  # output image to be shown
    w,h = img2.shape[:2]
    rect = (593,287,800,600)
    #rect = (data['args'][0], data['args'][1], data['args'][2], data['args'][3])
    bgdmodel = np.zeros((1, 65), np.float64)
    fgdmodel = np.zeros((1, 65), np.float64)
    cv2.grabCut(img2, mask, rect, bgdmodel, fgdmodel, 1, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    dst = img * mask2[:, :, np.newaxis]
    img += 255 * (1 - cv2.cvtColor(mask2, cv2.COLOR_GRAY2BGR))

    cv2.imwrite(PATH_OUT+"/left-pic-5.jpg",dst)