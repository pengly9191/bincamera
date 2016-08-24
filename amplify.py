import cv2
from  matplotlib import pyplot as plt
import Image
import numpy as np

def plot_image(image):
    if len(image.shape) == 2:
        image = cv2.merge((image, image, image))
    f, axarr = plt.subplots(1, 1, figsize=(10, 15))
    axarr.axis('off')
    axarr.imshow(image)
    axarr.plot()


if __name__ == '__main__':

    src = cv2.imread('/home/ply/stereo/data/merge/merged_0.jpg')

    cv2.imwrite('/home/ply/mer.jpg',src)

    # im = Image.open('/home/ply/image/20160721/merge/merged_0.jpg')
    # box = (0,0,1024,1536)
    # dst = im.crop(box)
    h,w = src.shape[:2]
    img1 = src[:, 0:w/2]
    img2 = src[:, w/2:w]


    ret, img1 = cv2.threshold(img1, 1, 255, cv2.THRESH_BINARY)
    ret, img2 = cv2.threshold(img2, 1, 255, cv2.THRESH_BINARY)

    img1 = cv2.medianBlur(img1,5)
    filename = '/home/ply/imgNew.jpg'
    cv2.imwrite(filename,img1)

    img1_row = np.sum(img1, axis=1)
    img1_col = np.sum(img1, axis=0)

    # imgNew = cv2.imread('/home/ply/imgNew.jpg',0)
    # h,w = imgNew.shape[:2]
    # imgNew = np.float32(imgNew)
    # dst = cv2.cornerHarris(imgNew, 2, 3, 0.04)
    # cv2.cornerHarris()
    # dst = cv2.dilate(dst, None)

    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 3, 3, 0.04)
    dst = cv2.dilate(dst, None)

    img[dst > 0.3 * dst.max()] = [0, 0, 255]
    s = dst > 0.3 * dst.max()
    p = np.where(s>0)
    print p
    cv2.imwrite('/home/ply/dst1.jpg', img)

    # Threshold for an optimal value, it may vary depending on the image.
    #
    # _, contours, hierarchy = cv2.findContours(imgNew,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # vis = np.zeros((h, w, 3), np.uint8)
    # cv2.drawContours(vis, contours, -1, (128, 255, 255),3, cv2.LINE_AA, hierarchy)
    # vis[dst > 0.01 * dst.max()] = [0, 255, 255]
    # cv2.imwrite("/home/ply/dst.jpg", vis)
    #
    # cv2.imwrite("/home/ply/imgNew1.jpg",vis)
    #
    # pentagram = contours[0]
    # print pentagram[:,]
    #
    # for i in range(h):
    #     idx = np.where(img1[i,:] > 10)[0]
    #
    # print img1[idx]
    # for y,k in range(9):
    #     for x in range(9):
    #         p[k][x] = (x*w/8,y*w/8)

    # outX0 = max(outX0, )
    # plt.subplot(2, 2, 3)
    # plt.imshow(dst)

    #  point coordinate ((0,74)(882,1079)  )

    roi = (0,74,882,1079-74)
    IMAGE_PATH = "/home/ply/stereo/data/merge/merged_0.jpg"
    src = cv2.imread(IMAGE_PATH)
    h, w = src.shape[:2]
    img1 = src[:, 0:w / 2]
    img2 = src[:, w / 2:w]
    IMAGE_PATH1 = "/home/ply/L.jpg"
    IMAGE_PATH2 = "/home/ply/R.jpg"
    cv2.imwrite(IMAGE_PATH1,img1)
    cv2.imwrite(IMAGE_PATH2, img2)
    img1 = Image.open(IMAGE_PATH1)
    img2 = Image.open(IMAGE_PATH2)

    dst1 = img1.crop(roi)
    dst2 = img2.crop(roi)
    size = (1024,1536)
    dst1 = dst1.resize(size, Image.ANTIALIAS)
    dst2 = dst2.resize(size, Image.ANTIALIAS)
    IMAGE_BAKUP1 = "/home/ply/dst1.jpg"
    IMAGE_BAKUP2 = "/home/ply/dst2.jpg"
    dst1.save(IMAGE_BAKUP1)
    dst2.save(IMAGE_BAKUP2)

    dst1 = cv2.imread(IMAGE_BAKUP1)
    dst2 = cv2.imread(IMAGE_BAKUP2)

    h,w = dst1.shape[:2]
    dst = np.zeros((h, w*2, 3), np.uint8)
    dst[:,0:w] = dst1
    dst[:, w:2*w] = dst2

    dst = cv2.resize(dst, (3328, 1872))
    cv2.imwrite("/home/ply/dst.jpg",dst)
