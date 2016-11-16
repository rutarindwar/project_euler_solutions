# peuler112.py


def t(n):
    s = str(n)
    a = ''.join(sorted(s))

    if (a != s) and (a != s[::-1]):
        return 1
    else:
        return 0


c = 0
end = 2000000

for i in range(100,end):
    if t(i):
        c += 1

    p = c*1.0/(end)
    if (abs(p - 0.99) <= 10**(-10)):
        print i, "%2.7f"%p
#        exit(0)

print i, p
