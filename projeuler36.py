# project euler prob 36
l = []
for i in range(1, 1000000):
    b = list(bin(i))[2:]
    if (str(i) == str(i)[::-1]) and (b == b[::-1]):
        print i, ''.join(b)
        l.append(i)
