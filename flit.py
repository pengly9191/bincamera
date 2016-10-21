from util import *

from glob import glob
from common import splitfn

PATH_IN = global_path
PATH_OUT = global_path+'/flit'

if __name__ == '__main__':

    img_mask = PATH_IN +'/*.jpg'
    img_names = glob(img_mask)
    for fn in img_names:
        print 'processing %s...' % fn
        img = cv2.imread(fn, 1)
        (B, G, R) = cv2.split(img)
        path, name, ext = splitfn(fn)
        cv2.imwrite(PATH_OUT+"/Red-%s.jpg" %(name), R)
        cv2.imwrite(PATH_OUT+"/Green-%s.jpg"%(name), G)
        cv2.imwrite(PATH_OUT+"/Blue-%s.jpg"%(name), B)
