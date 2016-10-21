import cv2

filename = '/home/ply/data/20160902/yuv.yuv'
if __name__ == '__main__':

    fd = open(filename, 'rb')
    img = fd.read();
    vis = cv2.cvtColor(img, cv2.CV_BayerBG2BGR)
    cv2.imwrite('/home/ply/dest.jpg',vis)