f = open('primesunderx.txt')
l = f.readlines()
l = [ i.strip() for i in l]
l = [ i for i in l if i[-1] != '9']
outl = []
from time import *

def lf(x): return (sum([1 if x[i:] in l  else 0 for i in range(len(x))]) == (len(x)))

def rl(x): return (sum([1 if x[:i] in l  else 0 for i in range(len(x), 0, -1)]) == (len(x)))
a = time()

for x in l:
    if ((sum([1 if x[i:] in l  else 0 for i in range(len(x))]) == (len(x))) and \
       (sum([1 if x[:i] in l  else 0 for i in range(len(x), 0, -1)]) == (len(x)))):
        print x 
        outl.append(x)
    if l.index(x)%10000 == 0:
        print "===> ", x, ".....",l.index(x)
print time() -a 
outl2 = [eval(i) for i in outl]


