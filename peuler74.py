#peuler74
from math import *

fact = {i:factorial(i) for i in range(10)}

def p74(x):

    lst = [0] * 100
    lst[0] = x
    nxt = sum([fact[eval(i)] for i in str(x)])
    j = 1
    while nxt not in lst[:j]:
        lst[j] = nxt
        j += 1
        x = nxt
        nxt= sum([fact[eval(i)] for i in str(x)])
    return j


big = 1
####
####for num in range(69,500000):
####    if p74(num) >= big:
####        big = p74(num)
####        print "%d has a chain of length %d"%(num, big)
