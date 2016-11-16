#project euler prob 39
from time import *
t1 = time()
mac = 1
l = []
for p in range(1, 1001):
##    if p%100 == 0 : print p
    count = 0
    for c in range(1, p/2):
        for a in range(1, c):
            b = p - c - a
            if c <= (a+b) and (c**2 == (a**2 + b**2)) and ( a<= b<= c):
                print a, b,c
                count += 1
    l.append(count)
##    if count !=0 : print p, ' has ', count , ' solutions.'
    if count > mac: mac = count

print l.index(max(l)) + 1

t2 = time()
print t2- t1              
