from time import *

fafile = open('anumber.txt', 'r')
fbfile = open('bnumber.txt', 'r')
fkfile = open('knumber.txt', 'r')


a = int(fafile.read())
b = int(fbfile.read())
k = int(fkfile.read())

fb = str(b)[:9]
bb = str(b)[-9:]

lbb = list(bb)
lbb.sort()
tail = ''.join(lbb)

lfb = list(fb)
lfb.sort()
head = ''.join(lfb)


print head, tail

t0  = time()
while not ((tail == '123456789') and (head == '123456789')):
    a, b = b, a+b
    k += 1
    fb = str(b)[:9]
    lfb = list(fb)
    lfb.sort()
    head = ''.join(lfb)

    bb = str(b)[-9:]
    lbb = list(bb)
    lbb.sort()
    tail = ''.join(lbb)
    if k % 10000 == 0:
        print k, len(str(b)), time() - t0
