import numpy as np
import cv2
from matplotlib import pyplot as plt


ply_header = '''ply
format ascii 1.0
element vertex %(vert_num)d
property float x
property float y
property float z
end_header
'''

def write_ply(fn, verts):
    verts = verts.reshape(-1, 3)

    verts = np.hstack([verts])
    with open(fn, 'w') as f:
        f.write(ply_header % dict(vert_num=len(verts)))
        np.savetxt(f, verts, '%f %f %f %d %d %d')

if __name__ == '__main__':

    imgL = cv2.imread('/home/ply/image/20161019/left_right_Pic/left-pic-6.jpg')  # downscale images for faster processing
    imgR = cv2.imread('/home/ply/image/20161019/left_right_Pic/right-pic-6.jpg')


    # disparity range is tuned for 'aloe' image pair
    window_size = 5
    min_disp = 30
    num_disp = 112 - min_disp
    stereo = cv2.StereoSGBM_create(minDisparity=min_disp,
           numDisparities= 16*8,
           blockSize= 2,
           P1=8 * 3 * window_size ** 2,
           P2=32 * 3 * window_size ** 2,
           disp12MaxDiff=-1,
           uniquenessRatio=10,
           speckleWindowSize=100,
           speckleRange=32

    )


    print 'computing disparity...'
    disp = stereo.compute(imgL, imgR).astype(np.float32)/16.0

    print disp.shape[:2]
    print disp



    cv2.imwrite("/home/ply/disp.jpg",disp)

    h, w = imgL.shape[:2]
    f = 0.8 * w  # guess for focal length

    cx = 2049
    cy = 1573
    f = 3415
    Tx = 30
    dcx = -40

    Q1 = np.float32([[1, 0, 0, -0.5 * w],
                    [0, 1, 0, -0.5 * h],  # turn points 180 deg around x-axis,
                    [0, 0, 0, f],  # so that y-axis looks up
                    [0, 0, -1, 0]])


    Q = np.float32([[1, 0, 0, -cx],
                    [0, 1, 0, -cy],  # turn points 180 deg around x-axis,
                    [0, 0, 0, f],  # so that y-axis looks up
                    [0, 0, -1/Tx, dcx/Tx]])
    print Q
    points = cv2.reprojectImageTo3D(disp, Q)

    mask = disp > disp.min()
    out_points = points[mask]

    verts = out_points.reshape(-1, 3)

    verts = np.hstack([verts])

    print verts


