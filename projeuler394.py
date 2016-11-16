#proj euler prob 394

from random import *


def cut(n, p):
    k = n * p
    count = 0
##    print n
    while n >= k :
        i, j = random()* n, random() * n
        n = min(i,j)
##        print n, (i, j)
        count += 1
##    print count
    return count


t = 10000000
n = 10**8
p = 1/2.0
lt = 0
for i in range(t):
    g = cut(n, p)
    lt += g
    if i%(t/40.0) == 0:
        print i



print "--------------"
print "%2.10f"%(lt/float(t))
