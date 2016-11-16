# proj euler 59
d = open('cipher1.txt', 'r')
t = d.read()
t = t.split(',')
t = [eval(i) for i in t]
al = 'abcdefghijklmnopqrstuvwxyz'
mal = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

m = t[:3]
cout = open('predata.txt', 'w')
for i in range(97, 123):
    for j in range(97, 123):
        for k in range(97, 123):
            key = [i, j, k]
            if (chr(m[0]^i) in (al+mal)): 
                s = [m[0]^i, m[1]^j, m[2]^k]
                print "found a winner"
                cout.write(''.join([str(i), str(j), str(k)])+' '+''.join([chr(l) for l in s])+'\n')
    print i


print ''.join([str(i), str(j), str(k)])
d2 = open('predata.txt', 'r')
w = d2.readlines()

w = [u[:-1] for u in w]
w = [y.split(' ') for y in w]
print len(w)
