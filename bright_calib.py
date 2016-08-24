from util import *
import Image




PATH_IN = '/home/ply/image/20160818/'


if __name__ == '__main__':

  #  img = cv2.imread(PATH_IN + "left-dst0.jpg")
    img = cv2.imread(PATH_IN + "right-dst0.jpg")

    limg =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    limg = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)

    cv2.imwrite(PATH_IN + "dst0.jpg", limg)
    h,w = limg.shape[:2]
    print h,w

    ysum = 0
    limg = np.array(limg)
    yavg = np.mean(limg)
    print yavg
    for i in range(h):
        for j in range(w):
                y,_,_ = limg[i][j]
                ysum = ysum + y

    yavg = ysum/(w*h)
    print yavg

    for i in range(h):
        for j in range(w):
            limg[i][j] = limg[i][j]
    cv2.imwrite(PATH_IN+"dst.jpg",limg)

    img = cv2.imread(PATH_IN + "right-dst0.jpg", 0)
    img = np.array(img)
    mean = np.mean(img)
    img = img - mean
    img = img * 1.5 + mean * 0.7
#    img = img / 255.
    cv2.imwrite(PATH_IN + "dst.jpg", img)















