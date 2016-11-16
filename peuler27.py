#peuler27.py

from time import *

f = open('outputfile.txt', 'r')

d = f.read().split(',')
d = [int(i) for i in d]

s = time()

dic = [0]*10**6
for a in range(1, 1000):
    for b in range(1, 1000):
        n = 0
        c = 0
        while (((n**2) + (a*n) + b) in d) and (c < 100):
            c += 1
            n += 1
        if c == 100: print 'waouh ...'
        dic.append((a,b, c))

        if (a*b) % 10000 == 0:
            print "%i is finished" % ((a*b)/10000)

print time() - s
