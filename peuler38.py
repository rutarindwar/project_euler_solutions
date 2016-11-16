# peuler38.py

s =10
n = 5


for k in range (2, s+1):
    p = ''
    for m in range(1, n+1):
        p += str(k*m)
        if len(p) >= 9:
            if ''.join(sorted(list(p))) == '123456789':
                print k, p, '****'
            break
        print k, m, p
##    print 'k= %d'%k
