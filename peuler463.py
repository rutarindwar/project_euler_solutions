# peuler463.py

from matplotlib import pyplot as plt

def f(i):
    if i==1:
        return 1
    elif i==3:
        return 3
    elif i%2 == 0:
        return f(i/2)
    elif (i-1)%4 == 0:
        return 2*f(2*((i-1)/4)+ 1) - f((i-1)/4)
    elif (i-3)%4 == 0:
        return 3*f(2*((i-3)/4) + 1) - 2*f((i-3)/4)


def s(n):
    return sum([f(j) for j in range(1, n+1)])

def s2(n):
    c = 0
    for i in range(1,n+1):
        c += f(i)
    return c

k = 2000
x = range(600,k+1)
y = [s(j) for j in range(600, k+1)]

plt.plot(x, y, '.')
plt.show()
