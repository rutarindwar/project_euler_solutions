# project euler #49

import itertools
from time import *

def unique(lst):
    ul = []
    for i in lst:
        if i not in ul:
            ul.append(i)
    return ul


f = open('primesunderx.txt','r')
ps = f.readlines()
d = [int(i.strip()) for i in ps]
lst = [p for p in d if ((p>=1000) and (p<=10000))]

f = lambda x: [int(''.join(k)) for k in list(itertools.permutations(str(x)))]

mx = 0
tic = time()
cands = range(1000,10000)
for n in cands:
    np = f(n)
    pp = [1 if j in lst else 0 for j in np]
    keep = [np[j] for j in range(len(pp)) if pp[j] == 1]
    ps = list(itertools.combinations(keep,3))
    ts = [sorted(i) for i in ps]

    dif = [[k[2]-k[1], k[1]-k[0]] for k in ts]

    for pot in dif:
        if (pot[0] == pot[1]) and (sum(pot) != 0):
            print pot, ts[dif.index(pot)]
            break
    for i in np:
        if i in cands:
            cands.remove(i)
    #print "There are %i cands left."%len(cands)

print time() - tic
    
####    for tpl in ts:
####        if (tpl[2] - tpl[1]) == (tpl[1] - tpl[0]):
####            out = tpl
####            print tpl, 'are a sequence with difference ',(tpl[2] - tpl[1])
####    
