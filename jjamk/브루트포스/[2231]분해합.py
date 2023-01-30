import sys

t = int(input())
res = 0
for i in range(1, t+1):
    arr = list(map(int, str(i)))
    if i + sum(arr) == t:
        print(i)
        break
if i == t:
    print(0)
