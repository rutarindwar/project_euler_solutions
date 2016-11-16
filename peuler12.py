# peuler12.py

from math import *
from time import *

def ld(n):
    t = int(ceil(n/2.0)) + 1
    lds = []
    for i in range(1, t):
        if n%i == 0:
            lds.append(i)
    lds.append(n)
    return lds


at = time()
for i in range(1000, 10000):
    s = (i*(i+1))/2.0
    
    if len(ld(s)) >= 500:
        print i, s, time() - at
        break

    if i%1000 == 0:
        print i, time() - at
