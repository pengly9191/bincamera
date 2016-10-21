##################################
####  reaize different size pic ##
##################################

from util import *
from glob import glob
from common import splitfn


PATH_IN = global_path+'/jpgPic'
PATH_OUT = global_path+'/zoomPic'

# PATH_IN = '/home/ply/stereo/data/in1/'
# PATH_OUT = '/home/ply/stereo/data/in/'

if __name__ == '__main__':

    img_mask = PATH_IN+'/*.jpg'
    print img_mask
    img_names = glob(img_mask)

    for fn in img_names:

        img = cv2.imread(fn)

        h,w = img.shape[:2]
        print h,w

    #    dst1 = cv2.resize(img,(w*2,h))
        dst = cv2.pyrDown(img)

        # dst = cv2.resize(img,(w/2,h/2))

        path, name, ext = splitfn(fn)
        cv2.imwrite(PATH_OUT+"/%s.jpg" % (name), dst)

    print 'resize pic success!!!!'




