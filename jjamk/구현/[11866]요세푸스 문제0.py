import sys
from collections import deque

n, m = map(int, input().split())
res = deque([])

for i in range(1, n+1):
    res.append(i)
print("<", end='')
while res:
    for i in range(m - 1):
        res.append(res[0])
        res.popleft()
    print(res.popleft(), end='')
    if res:
        print(', ', end='')
print(">")
