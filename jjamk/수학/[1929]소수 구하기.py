import sys
import math

m, n = map(int, input().split())

for i in range(m, n+1):
    flag = 0
    if i == 1:
        continue
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i)
