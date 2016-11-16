#proj euler 45
from time import *
a = time()
for i in range(285, 100000):
    t = i*(i+1)/2

    if ((1+ (1 + (24*t))**(0.5))%6 == 0) and ((1+ (1 + (8*t))**(0.5))%4 == 0) :
        print i, t

print time() -a
