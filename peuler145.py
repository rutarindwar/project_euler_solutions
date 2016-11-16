# peuler145.py

from time import *
tic = time()
n = 1000000
c = 0
for i in range(1,n+1):
    s = int(str(i)[::-1]) + i
    if sum([1 if int(k)%2==0 else 0 for k in list(str(s))]) == 0:
        c += 1
print time() - tic
print c
