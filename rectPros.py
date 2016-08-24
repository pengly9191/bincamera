import cv2
from  matplotlib import pyplot as plt
import Image
import numpy as np

if __name__ == '__main__':

    src = cv2.imread('/home/ply/stereo/data/merge/merged_0.jpg')
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    h, w = src.shape[:2]
    img1 = gray[:, 0:w / 2]
    img2 = gray[:, w / 2:w]

    IMAGE_PATH1 = "/home/ply/L.jpg"
    IMAGE_PATH2 = "/home/ply/R.jpg"
    ret, img1 = cv2.threshold(img1, 1, 255, cv2.THRESH_BINARY)
    ret, img2 = cv2.threshold(img2, 1, 255, cv2.THRESH_BINARY)
    cv2.imwrite(IMAGE_PATH1, img1)
    cv2.imwrite(IMAGE_PATH2, img2)


    dst = cv2.cornerHarris(img1, 3, 3, 0.04)
    dst = cv2.dilate(dst, None)


    img1[dst > 0.3 * dst.max()] = [0, 0, 255]
    s = dst > 0.3 * dst.max()
    p = np.where(s > 0)
    print p
    cv2.imwrite('/home/ply/dst1.jpg', dst)



    # roi = (20, 20, w/2-80, h - 20)
    # IMAGE_PATH = "/home/ply/stereo/data/merge/merged_0.jpg"
    # src = cv2.imread(IMAGE_PATH)
    # h, w = src.shape[:2]
    # img1 = src[:, 0:w / 2]
    # img2 = src[:, w / 2:w]
    #
    # cv2.imwrite(IMAGE_PATH1, img1)
    # cv2.imwrite(IMAGE_PATH2, img2)
    # img1 = Image.open(IMAGE_PATH1)
    # img2 = Image.open(IMAGE_PATH2)
    # dst1 = img1.crop(roi)
    # dst2 = img2.crop(roi)
    # size = (1024, 1536)
    # dst1 = dst1.resize(size, Image.ANTIALIAS)
    # dst2 = dst2.resize(size, Image.ANTIALIAS)
    # IMAGE_BAKUP1 = "/home/ply/dst1.jpg"
    # IMAGE_BAKUP2 = "/home/ply/dst2.jpg"
    # dst1.save(IMAGE_BAKUP1)
    # dst2.save(IMAGE_BAKUP2)
    #
    # dst1 = cv2.imread(IMAGE_BAKUP1)
    # dst2 = cv2.imread(IMAGE_BAKUP2)
    #
    # h, w = dst1.shape[:2]
    # dst = np.zeros((h, w * 2, 3), np.uint8)
    # dst[:, 0:w] = dst1
    # dst[:, w:2 * w] = dst2
    #
    # dst = cv2.resize(dst, (3328, 1872))
    # cv2.imwrite("/home/ply/dst.jpg", dst)



