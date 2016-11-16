#peuler127

from fractions import gcd

def prodlist(lst):
    p = 1
    for k in lst:
        p *= k
    return p



def getPrimes(n):
    d = 2
    p = []
    while d*d <= n:
        k = 0    
        while n%d ==0:
            n = n/d
            if not k:
                p.append(d)
                k = 1
        d+= 1
    if n != 1:
        p.append(n)
    return p
    

def istriplet(a, b, c):
    cond1 = (sum([gcd(a, b), gcd(a,c), gcd(b, c)]) == 3)
    cond2 = a<b
    cond3 = (a+b == c)
    cond4 = prodlist(getPrimes(a*b*c)) < c
##    print cond1, cond2, cond3, cond4
    
    if (cond1 and cond2 and cond3 and cond4):
##        print 'it is a triplet'
        return 1
    else:
        return 0


count = 0
sumc = 0
for c in range(3, 5000):
    for b in range(2,c):
        a = c - b
        if a < b:
            if istriplet(a, b, c):
                print '%10d \t %10d \t %10d'%(a,b,c)
                count += 1
                sumc += c
print count
print sumc




