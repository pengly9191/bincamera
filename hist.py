"""
Created on 2016.09.06
hist image
flit r/g/b
hist
merge rgb
"""
import cv2
from numpy import *
import Image
import os
from common import splitfn

if __name__ == '__main__':

    img = cv2.imread('/home/ply/pic.jpg')
    (B, G, R) = cv2.split(img)

    equ_B = cv2.equalizeHist(B)
    equ_G = cv2.equalizeHist(G)
    equ_R = cv2.equalizeHist(R)

    equ = cv2.merge([equ_B, equ_G, equ_R])

    cv2.imwrite("/home/ply/equ.jpg",equ)




