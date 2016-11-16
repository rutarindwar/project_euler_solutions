# prob 14
from time import *

a = time()
n = 1000000
l = [0] *(n+1)
for i in range(1, n+1):
    j = i
    k = 0
    while ( i != 1):
        if (i%2  == 0):
            i = i/2
        else:
            i = 3*i + 1
        k += 1
    l[j] = k

    if j%100000 == 0:
        print j, " >>>>> " , k
    
l.index(max(l))
print time() - a
