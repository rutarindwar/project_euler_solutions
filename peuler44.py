# peuler44.py

s = 10**4
l = [0] * s
for i in range(s):
    n = i+1
    l[i] = n * (3*n - 1)/2


##and (abs(l[i] - l[j]) in l)
for i in range(s/2):
    for j in range(s/2):
        if (i != j):
            if ((l[i] + l[j] in l) and (abs(l[i] - l[j]) in l)):
                print l[i], l[j], abs(l[i] - l[j])
