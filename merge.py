from util import *


if __name__ == '__main__':
    img_mask = '/home/ply/stereo/data/out'
    for fn in xrange(2):
        print fn
        img_mask_B = "%s/Blue-canvas-%d.jpg"%(img_mask,fn)
        img_mask_G = "%s/Green-canvas-%d.jpg" % (img_mask,fn)
        img_mask_R = "%s/Red-canvas-%d.jpg" % (img_mask,fn)
        print img_mask_B,img_mask_G,img_mask_R
        B = cv2.imread(img_mask_B,0)
        G = cv2.imread(img_mask_G,0)
        R = cv2.imread(img_mask_R,0)
        merged = cv2.merge([R, G, B])

   #     merged1 =cv2.pyrUp(merged,2)
        merged2 = cv2.resize(merged,(3328,1872))
        cv2.imwrite("/home/ply/stereo/data/merge/merged_%d.jpg" % (fn), merged2)
