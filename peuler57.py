#peuler57.py

import fractions
from time import *

s = 1000
n = 3
d = 2
c = 0
t = time()
for i in range(1,s):
    nt = n- d + 2*d
    n, d = d, nt
    n = n + d
    if len(str(n)) > len(str(d)):
        c += 1
##        print len(str(n)), len(str(d)), 
##        print n,d
print time() - t
