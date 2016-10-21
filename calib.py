# !/usr/bin/env python


import numpy as np
import cv2
from matplotlib import pyplot as plt
from util import *
# local modules
from common import splitfn
import yaml

# built-in modules
import os

USAGE = '''
USAGE: calib.py [--save <filename>] [--debug <output path>] [--square_size] [<image mask>]
'''

PATH_IN = global_path+'/left_right_Pic'
PATH_OUT = global_path+'/calib'


if __name__ == '__main__':
    import sys
    import getopt
    from glob import glob

    args, img_mask = getopt.getopt(sys.argv[1:], '', ['save=', 'debug=', 'square_size='])
    args = dict(args)
    try:
        img_mask = img_mask[0]
    except:
        img_mask = PATH_IN+'/right*.jpg'

    img_mask_left = PATH_IN+'/left*.jpg'
    img_mask_right = PATH_IN + '/right*.jpg'

    if len(img_mask):


        img_names = glob(img_mask)
        print img_names

        debug_dir = 0
        square_size = float(args.get('--square_size', 20.0))
        print square_size

        pattern_size = (11, 8)
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
                # path, name, ext = splitfn(fn)
                # cv2.imwrite("/home/ply/%s.jpg"%(name),vis)
            if not found:
                print 'chessboard not found'
                continue

            img_points.append(corners.reshape(-1, 2))
            obj_points.append(pattern_points)

    #    print "img_points:",img_points
    #    print "obj_points",obj_points


        rms, camera_matrix, dist_coefs, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, (w, h), None, None)
        print "RMS:", rms
        print "camera matrix:\n", camera_matrix
        print "distortion coefficients: ", dist_coefs.ravel()

        # if camera_matrix is scale ,must  z = 1.0
        camera_matrix = camera_matrix
        camera_matrix[2, 2] = 1


        for fn in img_names:
            img = cv2.imread(fn, 0)
            h, w = img.shape[:2]
            newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (w, h), 1, (w, h))
            print 'newcameramtx ',newcameramtx
            print "roi",roi
            mapx, mapy = cv2.initUndistortRectifyMap(camera_matrix, dist_coefs, None, None, (w, h), 5)
    #        dst = cv2.remap(img, mapx, mapy, cv2.INTER_CUBIC)
            dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

            #print("------------------use undistort function-------------------")
            #   dst = cv2.undistort(img, camera_matrix, dist_coefs, None, newcameramtx)
            # x, y, w, h = roi
            # dst1 = dst[y:y + h, x:x + w]
            #print("-------------------use remap way-----------------------")
            #mapx, mapy = cv2.initUndistortRectifyMap(camera_matrix, dist_coefs, None, newcameramtx, (w, h), 5)
            # dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)


            path, name, ext = splitfn(fn)
            cv2.imwrite(PATH_OUT+'/%s.jpg' % (name), dst)
            # plt.imshow(dst,cmap='gray')
            # plt.show()








