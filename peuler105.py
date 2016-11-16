# peuler 105

from numpy import *
from itertools import *

f = open('p105_sets.txt', 'r')
d = f.readlines()
d = [[eval(i) for i in k.split(',')] for k in d]

sz = len(d)

def list_powerset(lst):
    result = [[]]
    for x in lst:
        result.extend([subset + [x] for subset in result])
    return result[1:-1]


res = []

for i in range(100):
    print i
    
    ln = d[i]
    blst = list_powerset(ln)
    flag = 1
    for j in range(len(blst)):
        bi = blst[j]
        clst = list_powerset(setdiff1d(ln, bi))
        cond1 = 1
        cond2 = 1
        for ci in clst:
            if (sum(bi) == sum(ci)):
                cond1 = 0
                #print bi,ci, 'cond1'
                break
            
            if len(bi) > len(ci):
                if sum(bi) <= sum(ci):
                    cond2 = 0
                    #print bi,ci, 'cond2'
                    break
        if (cond1 == 0) or (cond2 == 0):
            flag = 0


    if flag != 0: # meaning it passed all conditions
        print ln
        res.append(ln)

    print '===================='

print sum(sum(res))
    

        
