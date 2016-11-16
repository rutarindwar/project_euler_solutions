#peuler102_2.py

from math import *

def ang(x1, y1, x2, y2):
    a = acos(((x1 * x2) + (y1 * y2))/(sqrt(x1**2 + y1**2) * sqrt(x2**2 + y2**2)))
    return a

f = open('triangles.txt', 'r')
d = f.readlines()
d = [i[:-1] for i in d]
d = [k.split(',') for k in d]

c= 0

for i in range(1000):
    x1, y1, x2, y2, x3, y3 = [eval(h) for h in d[i]]
    a1 = ang(x1, y1, x2, y2)
    a2 = ang(x1, y1, x3, y3)
    a3 = ang(x2, y2, x3, y3)
    s = a1 + a2 + a3

    if (s == 2*pi):
        c += 1
        print '%d contains the origins ...' % (i+1)
    
    
