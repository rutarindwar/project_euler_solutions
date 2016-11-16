# peuler80.py
# calculating sqrt by hand to 100th digit

from math import *
from time import *

x = 2
def sum100digits(x):
    m = int(sqrt(x))
    r = x - m*m
    s = 100
    count = 0
    ans = m

    for i in range(s-1):
        r = r * 100
        n = 0

        while ((ans*2)*10 + n) * n <= r:
            tmp = ((ans*2)*10 + n) * n
            n += 1
        n -= 1
        ans = (ans*10) + n
        count += n
        r = r - tmp

    return count + m

t = time()
res = 0
for num in range(1,100):
    if (sqrt(num) != int(sqrt(num))):
        p = sum100digits(num)
##        print "%d : %d"%(num, p)
        res += p
print res
print time() - t
