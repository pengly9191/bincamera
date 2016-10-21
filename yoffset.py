from util import *
import numpy as np
import cv2
from matplotlib import pyplot as plt

# local modules
from common import splitfn

USAGE = '''
USAGE: calib.py [--save <filename>] [--debug <output path>] [--square_size] [<image mask>]
'''

PATH_IN = global_path+'/left_right_Pic'
PATH_OUT = global_path+'/calib'



pattern_w = 11
pattern_h = 8

def getcorners(img_names):
    debug_dir = 1
    square_size = float(args.get('--square_size', 20.0))
    pattern_size = (pattern_w, pattern_h)
    pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
    pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
    pattern_points *= square_size

    obj_points = []
    img_points = []
    h, w = 0, 0
    for fn in img_names:
        img = cv2.imread(fn, 0)
        if img is None:
            print "Failed to load", fn
            continue
        h, w = img.shape[:2]
        found, corners = cv2.findChessboardCorners(img, pattern_size)
        if found:
            term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1)
            cv2.cornerSubPix(img, corners, (5, 5), (-1, -1), term)
        if debug_dir:
            vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            cv2.drawChessboardCorners(vis, pattern_size, corners, found)
            path, name, ext = splitfn(fn)
            cv2.imwrite("/home/ply/%s.jpg" % (name), vis)
        if not found:
            print 'chessboard not found'


        img_points.append(corners.reshape(-1, 2))
        obj_points.append(pattern_points)

    return found,img_points,obj_points

def fitline(x_value,y_value):
    for i in xrange(pattern_h):
        X = x_value[0+i:pattern_w+i]
        Y = y_value[0+i:pattern_w+i]
        # print 'x:',X
        # print 'y',Y
        z1 = np.polyfit(X, Y, 1)
        p1 = np.poly1d(z1)
        # print z1
 #       print p1



def mean_move_xy(x_leftvalue,x_rightvalue,y_leftvalue,y_rightvalue):
    x_diff = x_leftvalue - x_rightvalue
    y_diff = y_leftvalue - y_rightvalue
    # print 'x_diff:',x_diff
    # print 'y_diff:',y_diff
    x_min = min(x_diff)
    x_max = max(x_diff)
    y_min = min(y_diff)
    y_max = max(y_diff)

    x_mean = sum(x_diff) / len(x_diff)
    y_mean = sum(y_diff) / len(y_diff)

    # print "x_max :", x_max
    # print "x_min :", x_min
    # print "y_max :", y_max
    # print "y_min :", y_min
    print "x_mean :", x_mean
    print "y_mean :", y_mean
    return x_mean,y_mean




if __name__ == '__main__':
    import sys
    import getopt
    from glob import glob

    args, img_mask = getopt.getopt(sys.argv[1:], '', ['save=', 'debug=', 'square_size='])
    args = dict(args)
    try:
        img_mask = img_mask[0]
    except:
        img_mask = PATH_IN+'/*.jpg'

    img_name = glob(img_mask)

    size =  len(img_name)
    print size
    for i in range(size/2):

        obj_points = []
        img_points = []

        # img_names = [PATH_IN+'/left-pic-%s.jpg'%(i),
        #             PATH_IN+'/right-pic-%s.jpg'%(i)]

        img_names = [PATH_IN + '/left-pic-%s.jpg' % (i),
                     PATH_IN+'/right-pic-%s.jpg'%(i)]

        print img_names
        found,img_points,obj_points = getcorners(img_names)
        if not found:
            continue
        if found:
            leftvalue  = img_points[0]
            rightvalue = img_points[1]

            # print "1:",leftvalue
            # print "2:",rightvalue

            x_leftvalue = leftvalue[:,0]
            y_leftvalue = leftvalue[:,1]
            x_rightvalue = rightvalue[:, 0]
            y_rightvalue = rightvalue[:, 1]

            ######### fit line ################
            print 'fitline left:'
            fitline(x_leftvalue, y_leftvalue)
            print 'fitline right:'
            fitline(x_rightvalue, y_rightvalue)

            x_mean, y_mean = mean_move_xy(x_leftvalue, x_rightvalue, y_leftvalue, y_rightvalue)
'''

            path, name, ext = splitfn(img_names[1])
            src = cv2.imread(PATH_IN+'/%s.jpg'% (name))

            dst = src
            h,w = src.shape[:2]
            if y_mean < 0:
                # right pic up
                y_mean = int (abs(y_mean))
                dst[0:h-y_mean,:] = src[y_mean:h,:]
            if y_mean > 0:
                # right pic down
                y_mean = int (abs(y_mean))
                zerom = np.zeros((y_mean, w, 3), np.uint8)
                dst[0:y_mean,:]= zerom
                dst[ y_mean:h,:] = src[ 0:h -y_mean,:]

            img = np.zeros((h, w*2, 3), np.uint8)
            path, name, ext = splitfn(img_names[0])
            left_img = cv2.imread(PATH_IN+'/%s.jpg'% (name))
            left_img[0:y_mean, :] = zerom
            right_img = dst
            img[:,0:w] = left_img
            img[:,w:2*w] = right_img

            cv2.imwrite(PATH_OUT+'/pic_%s.jpg'% (i),img)

            img = np.zeros((h, w * 2, 3), np.uint8)

            x_off = int (abs(x_mean-20)/2 )

            if x_mean < 0:
                img[:,x_off:w+x_off] = left_img
                img[:,w-x_off:2*w-x_off] = right_img
                img[:,0:x_off] = 0
                img[:,w-x_off:w+x_off] = 0
                img[:, 2*w-x_off:2*w] = 0

            if x_mean > 0:

                img[:, 0:w - x_off] = left_img[:,x_off:w]
                img[:, w + x_off:2 * w ] = right_img[:,0:w-x_off]
                img[:, w - x_off:w + x_off] = 0



            dst1 = cv2.resize(img, (w*2, h*2))
            cv2.imwrite(PATH_OUT + '/dst_%s.jpg' % (i), dst1)




'''




