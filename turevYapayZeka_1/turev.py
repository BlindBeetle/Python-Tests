import math
import numpy as np

h = 0.001
w=5
b=4

data = np.array([[1,1],[2,2],[3,4],[4,6]])

def f(x,w,b):

    return (w*x+b)**2

def hata (w,x,b,y):

    return math.fabs(f(x,w,b)-y)

#w için türev
def turev_w(x,y,w,b):

    return((hata(x,(w+h),b,y) - hata(w,x,b,y)) / h)

#b için türev
def turev_b(x,y,w,b):

    return((hata(x,w,(b+h),y) - hata(w,x,b,y)) / h)

for i in data:

    x=i[0]
    y=i[1]

    hata_ = hata(x,w,b,y)
    turevw = turev_w(x,y,w,b)
    turevb = turev_b(x,y,w,b)

    print(f"x: {x}  y: {y}  w: {w}  b: {b}  hata: {hata_}  turev_w: {turevw}  turev_b: {turevb}")
