# peuler 407
# l = range(5+1);max([i for i in l if ((i**2)-i)%6 == 0 ])
from time import *
at = time()
l = [6]
k = [max([j for j in range(i+1) if ((j**2)-j)%i == 0 ]) for i in l]

print time() - at
print sum(k)


####k = [0] * len(l)
####
####for i in range(1, len(l)):
####    if (i**2 - i) % i == 0:
####        k[i] = max(k[i-1], i)
####    else:
####        k[i] = k[i-1]
####
####print time() - at
####print sum(k)
