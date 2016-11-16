# peuler 99.py

from math import *
from time import *

f = open('p099_base_exp.txt', 'r')
d = f.readlines()
d = [i.strip().split(',') for i in d]

tic = time()
mx = 0
ind = 0
for i in range(len(d)):
    base,xp = [int(k) for k in d[i]]

    if xp*log(base) > mx:
        mx = xp * log(base)
        ind = i
print ind
print time() - tic
