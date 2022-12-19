x,y = input().split()

x = int(x)
y = int(y)

from math import gcd

print(gcd(x,y))

def lcm(x,y):
    return x * y // gcd(x,y)

print(lcm(x, y))
