from util import *

from common import splitfn
import numpy as np
import sys
import getopt
from glob import glob

PATH_IN ='/home/ply/image/20160818/zoomPic'
PATH_OUT = '/home/ply/image/20160818/left_right_Pic'

if __name__ == '__main__':

    args, img_mask = getopt.getopt(sys.argv[1:], '', ['save=', 'debug=', 'square_size='])
    args = dict(args)

    img_mask = PATH_IN+'/*.jpg'
    img_names = glob(img_mask)


    for fn in img_names:

        img = cv2.imread(fn, 1)
        h, w = img.shape[:2]
        leftimg = np.zeros([h , w /2 ])
        rightimg = np.zeros([h , w /2])
        leftimg = img[:,0:w/2]
        rightimg = img[:,w/2:w]
        path, name, ext = splitfn(fn)
        cv2.imwrite(PATH_OUT+'/left-%s.jpg'% name ,leftimg)
        cv2.imwrite(PATH_OUT+'/right-%s.jpg'% name , rightimg)

