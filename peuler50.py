#peuler50.py
from time import *

tic = time()
fname = 'primesunderx.txt'
f = open(fname, 'r')
d = f.readlines()
d = [eval(i[:-1]) if '\n' in i else eval(i) for i in d]


def isprime(x, l):
    ind = 0

    while (l[ind] <= x):
        if (l[ind] == x):
            return 1
        ind += 1

    return 0



i = 0
j = 0
umax = 500000

totsum = 1
totlen = 1
totstart = 0

lastindp1 = 50000

for i in range(lastindp1):
    if (d[i] >= umax):
        break
    
    j = i+1
    length = 1
    p = 0
    lkeep = 1
    while (sum(d[i:j+1]) <= umax):
        length += 1
##        print '..', sum(d[i:j+1]), length
        if (isprime(sum(d[i:j+1]), d)):
            p = sum(d[i:j+1])
##            print '.......', sum(d[i:j+1]), length
            lkeep = length
        j += 1
    
    if (lkeep > totlen):
        totlen = lkeep
        totsum = p
        totstart = d[i]
        print "%d leads to a sum %d in %d terms"%(d[i], p, lkeep)    


print "longest prime: %d (avec %d terms from %d..)"%(totsum, totlen, totstart)








print time() - tic
