# peuler43
from time import *

st = time()
f = open('primes1.txt','r')
d = f.readlines()
d = [i.strip() for i in d if i != '\n' ]
d = [i.split() for i in d]
d = [i for j in d for i in j]
print len(d)
d = [i for i in d if '0' not in i]
print len(d)

lst = 0
for p in d:
    s = ''.join([str(i) for i in range(1,len(p)+1)])
    
    if s == ''.join(sorted(list(p))):
        lst = p

print lst
print time() - st

    
