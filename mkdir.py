from util import *
from zoom import *
import os



if __name__=="__main__":

    if not os.path.exists(global_path):
        os.mkdir(global_path)
        os.makedirs(global_path + "/jpgPic")
        os.makedirs(global_path + "/zoomPic")
        os.makedirs(global_path + "/left_right_Pic")
        os.makedirs(global_path + "/calib")


    if os.path.exists(global_path):
        img_mask = PATH_IN_ALL + '*.jpg'
        img_names = glob(img_mask)
        num = 0
        for fn in img_names:
            img = cv2.imread(fn)
            cv2.imwrite(global_path + "/jpgPic/pic-%s.jpg" % num, img)
            num = num+1

    print 'mkdir and get origin pic success!!!'