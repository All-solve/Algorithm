import sys

n, m = map(int, input().split())

a = b = c = 1
for i in range(2, n+1):
    a *= i
for j in range(2, m+1):
    b *= j
for k in range(2, n-m+1):
    c *= k

print(a//(b*c))
