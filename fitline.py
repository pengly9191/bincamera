import numpy as np


if __name__=='__main__':


    X=[ 1 ,2  ,3 ,4 ,5 ,6]
    Y=[ 2.5 ,3.51 ,4.45 ,5.52 ,6.47 ,7.51]
    z1 = np.polyfit(X, Y, 1)
    p1 = np.poly1d(z1)
    print z1
    print p1