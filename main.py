from util import *
from zoom import *
import os


if __name__=="__main__":

    execfile('mkdir.py')
    if not os.path.exists(global_path+"/zoomPic"):
        os.makedirs(global_path+"/zoomPic")
    if not os.path.exists(global_path + "/left_right_Pic"):
        os.makedirs(global_path + "/left_right_Pic")
    if not os.path.exists(global_path + "/calib"):
        os.makedirs(global_path + "/calib")

    print "picture resize:"
    # resize picture to (2*w,h)  then resize to (2*w,h)/2
    execfile('zoom.py')


    print "cut to get left and right picture:"
    execfile('cutpic.py')


    print "process picture get x_mean and y_mean and move picture:"
    execfile('yoffset.py')

