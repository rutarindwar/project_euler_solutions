####### projecteuler21
######
def d(n):
    s = []
    for i in range(1, n/2 + 1):
        if n%i == 0:
            s.append(i)

    return sum(s)
######tl = []
######for i in range(1, 10001):
######    div = d(i)
######    if (i == d(div)):
######        tl.append(i)
######
######from math import *
######
######l = []
######for n in range(1, 101):
######    for r in range(1, n+1):
######        c = factorial(n)/(factorial(r)*factorial(n-r))
######        if c >= 1000000:
######            print c
######            l.append(c)
