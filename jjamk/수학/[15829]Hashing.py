import sys

n = int(input())
m = input()

sum = 0
for i in range(n):
    sum += (ord(m[i])-96) * (31**i)
print(sum % 1234567891)
