
from util import *
from PIL import Image
import ImageDraw
from glob import glob
from common import splitfn

# PATH_IN = global_path+'/jpgPic'
# PATH_OUT = global_path+ '/originline'
PATH_IN = global_path+'/calib'
PATH_OUT = global_path+ '/dst'


if __name__== '__main__':

    img_mask = PATH_IN+'/*.jpg'

    img_names = glob(img_mask)
    print img_names
    for fn in img_names:
        print fn
        img = Image.open(fn)
        draw = ImageDraw.Draw(img)
        w,h = img.size
        for y in range(0,h,50):
            draw.line(((0,y),(w,y)),(255,255,0))


        draw.line(((w/2, 0), (w/2, h)), "red")
        draw.line(((w / 4, 0), (w / 4, h)) ,"red")
        draw.line(((w *3/ 4, 0), (w *3/ 4, h)), "red")

        path, name, ext = splitfn(fn)
        img.save(PATH_OUT+'/%s.jpg'%(name))







