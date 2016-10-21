
# -*- coding: utf-8 -*-
"""
Created on 2016.09.06
input yuv420p data
imshow y value as pic
imshow to rgb pic
"""

from numpy import *
import Image
import os
from common import splitfn

screenLevels = 255.0


def yuv_import(filename, dims, numfrm, startfrm):
    fp = open(filename, 'rb')
    blk_size = prod(dims) * 3 / 2
    fp.seek(blk_size * startfrm, 0)
    Y = []
    U = []
    V = []
    # print dims[0]
    # print dims[1]
    d00 = dims[0] // 2
    d01 = dims[1] // 2

    Yt = zeros((dims[0], dims[1]), uint8, 'C')
    Ut = zeros((d00, d01), uint8, 'C')
    Vt = zeros((d00, d01), uint8, 'C')
    print (dims[0], dims[1])
    print (d00, d01)


    if 1:
        for i in range(numfrm):
            for m in range(dims[0]):
                for n in range(dims[1]):
                    if (m < 80):
                        Yt[m, n] = ord(fp.read(1))
  #                      Yt[m, n] = 0
                    else:
                        Yt[m, n] = ord(fp.read(1))
   #                     Yt[m, n] = 255
            for m in range(d00):
                for n in range(d01):
                    if (m <40):
                        Ut[m, n] = ord(fp.read(1))
    #                    Ut[m, n] = 128
                    else:
                        Ut[m, n] = ord(fp.read(1))
      #                  Ut[m, n] = 128
            for m in range(d00):
                for n in range(d01):
                    if (m <40):
                        Vt[m, n] = ord(fp.read(1))
       #                 Vt[m, n] = 128
                    else:
                        Vt[m, n] = ord(fp.read(1))
       #                 Vt[m, n] = 128
    else:
        for i in range(numfrm):
            for m in range(dims[0]):
                for n in range(dims[1]):
                    if (m < 80):
                        Yt[m, n] = ord(fp.read(1))
                        Yt[m, n] = 255
                    else:
                        Yt[m, n] = ord(fp.read(1))
                        Yt[m, n] = 255
            for m in range(d00):
                for n in range(d01):
                    if (m < 40):
                        Ut[m, n] = ord(fp.read(1))
                        Ut[m, n] = 128
                    else:
                        Ut[m, n] = ord(fp.read(1))
                        Ut[m, n] = 128
            for m in range(d00):
                for n in range(d01):
                    if (m < 40):
                        Vt[m, n] = ord(fp.read(1))
                        Vt[m, n] = 128
                    else:
                        Vt[m, n] = ord(fp.read(1))
                        Vt[m, n] = 128


    # convert yuv
    # Y = Y + [Yt]
    # U = U + [Ut]
    # V = V + [Vt]
    #


    # w = dims[0]
    # h = dims[1]
    # Y0 = Y[0]
    # print len(Y0)
    # for i in range(40):
    #     Y0[i] = 0
    # Y[0] = Y0


    # Y0 = Y[0]
    # print Y0.shape
    # for i in xrange(45):
    #         print "i:",i,Y0[i]
    fp.close()
 #   return (Y, U, V)
    return(Yt,Ut, Vt)

def yuv_move(Y, U, V):


    return Y,U,V

def yuv_crop(Yt,Ut, Vt,crop_value):


    Y = []
    U = []
    V = []
    Y = Y + [Yt]
    U = U + [Ut]
    V = V + [Vt]
    #
    # Y0 = Y[0]
    # print len(Y0)
    # for i in range(40):
    #     Y0[i] = 0
    # Y[0] = Y0
    #
    return Y, U, V


def yuv2rgb(Y, U, V, width, height):
    U = repeat(U, 2, 0)
    U = repeat(U, 2, 1)
    V = repeat(V, 2, 0)
    V = repeat(V, 2, 1)
    r = zeros(wh, float, 'C')
    g = zeros(wh, float, 'C')
    b = zeros(wh, float, 'C')
    rr = zeros(wh, float, 'C')
    gg = zeros(wh, float, 'C')
    bb = zeros(wh, float, 'C')
    rr = Y + 1.14 * (V - 128.0)
    gg = Y - 0.395 * (U - 128.0) - 0.581 * (V - 128.0)
    bb = Y + 2.032 * (U - 128.0)

    for i in xrange(width):
        for j in xrange(height):
            if rr[i,j]>255:
                rr[i,j] = 255
            if rr[i,j] <0:
                rr[i,j] =0
            if gg[i,j] > 255:
                gg[i,j] = 255
            if gg[i,j] < 0:
                gg[i,j] = 0
            if bb[i,j] > 255:
                bb[i,j] = 255
            if bb[i,j] < 0:
                bb[i,j] = 0


    rr1 = rr.astype(uint8)
    gg1 = gg.astype(uint8)
    bb1 = bb.astype(uint8)

    # print 'rr1:'
    # print rr1[0:3, 0:30]

    return rr1, gg1, bb1


if __name__ == '__main__':

    if 1:
        w = 800
        h = 600
        if 1:
            path = '/home/ply/data/20160902/yuv.yuv'
        else:
            path = '/home/ply/data/20160902/yuvpros.yuv'
    else:
       w = 720
       h = 540
       if 0:
           path = '/home/ply/data/20160902/yuvorigin5.yuv'
       else:
           path = '/home/ply/data/20160902/yuvpros5.yuv'
    wh = (w, h)

 #   data = yuv_import('/home/ply/yuvhalf.yuv', wh, 1, 0)
    Yt, Ut, Vt = yuv_import(path, wh, 1, 0)
    crop_value = 80
    data = yuv_crop(Yt, Ut, Vt , crop_value)

    YY = data[0][0]


    print YY.shape

    im = Image.fromstring('L', wh, YY.tostring())

    path, name, ext = splitfn(path)

    im.save('%s/%s.jpg'%(path,name))
    whu = (w / 2, h / 2)
    UU = data[1][0]
    im = Image.fromstring('L', whu, UU.tostring())
    im.save('%s/%s_u.jpg'%(path,name))
    VV = data[2][0]
    im = Image.fromstring('L', whu, VV.tostring())
    im.save('%s/%s_v.jpg'%(path,name))

    R_ = data[0][0]
    G_ = data[1][0]
    B_ = data[2][0]
    RGB = yuv2rgb(R_, G_, B_, w, h)
    im_r = Image.fromstring('L', wh, RGB[0].tostring())
    im_g = Image.fromstring('L', wh, RGB[1].tostring())
    im_b = Image.fromstring('L', wh, RGB[2].tostring())
#    im_r.show()
    # for m in range(2):
    #     print m, ': ', R_[m, :]
    co = Image.merge('RGB', (im_r, im_g, im_b))
#    print R_
    co.save('%s/%s_result.jpg'%(path,name))