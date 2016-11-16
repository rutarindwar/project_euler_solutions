
# project euler, problem 99

from time import *

def p92(n,flag):
    n0 = n
    nlst = [n]
    e = 0
    while 1:
        l = list(str(n))
        tmp = sum([eval(i)**2 for i in l])
        if (tmp in nlst) or (tmp == 89):
            e = tmp
            break
        else:
            nlst.append(tmp)
            n = tmp
    if flag:
        print nlst
    return [tmp, len(nlst),n0]

def p92_v2(n,old,flag):
    n0 = n
    nlst = [n]
    e = 0
    while 1:
        l = list(str(n))
        tmp = sum([eval(i)**2 for i in l])
        if (tmp in old) or (tmp == 1) or (tmp == 89):
            e = tmp
            break
        else:
            nlst.append(tmp)
            n = tmp
    if flag:
        print nlst
    return [e,len(nlst)]


end = 100000

t1 = time()
c = 0
lst1 = []
for i in range(2,end):
    tmp = p92_v2(i,lst1,0);
    if (tmp[0] == 89) or (tmp[0] in lst1):
        lst1.append(i)

print time() - t1



t2 = time()
c = 0
lst2 = []
for i in range(2,end):
    if p92(i,0)[0] == 89:
        lst2.append(i)

print time() - t2


######
######viz = []
######c89 = 0
######c1 = 0
######
######for n in range(47,48): 
######    lst = [n]
######    l = list(str(n))
######    tmp = sum([eval(i)**2 for i in l])
######    while (tmp not in lst) and (tmp not in viz):
######        lst.append(tmp)
######        l = list(str(tmp))
######        tmp = sum([eval(i)**2 for i in l])
######    
######    if tmp == 89:
######        c89 += 1
######    if tmp == 1:
######        c1 += 1
######    for i in lst:
######        if i not in viz:
######            viz.append(i)
