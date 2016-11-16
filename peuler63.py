# project euler 63

for i in range(1, 999999999+1):
    r = i ** (1.0/len(str(i)))
    if abs(r - int(r)) <= 0.0000000001:
        print i, '....', int(r)
