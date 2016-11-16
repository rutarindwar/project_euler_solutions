#peuler267
from random import *

c = 1.0;
f = 0.10
hs = 0;
for i in range(1000):
    flip = random();
    bet = f*c;
    if flip > 0.5: # head, win.
        c = c+ 2*bet
        hs += 1
    else:
        c = c - bet
    #print "capital %.10f"%c
    if (c > 1000000) :
        print "It took %i flips to get a milli"%(i+1)
        
    if c == 0:
        print "Busted"
        break
    if (c > 10**9) & (c > 10**6):
        print "It took %i flips to get a billion"%(i+1)

print "capital %.10f"%c
print "# heads= %i"%hs
