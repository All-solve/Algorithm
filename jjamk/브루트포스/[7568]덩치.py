import sys

n = int(input())
res = [[0]*2 for i in range(n)]
arr = []
for i in range(n):
    x, y = map(int, input().split())
    res[i][0] = x
    res[i][1] = y
for i in range(n):
    cnt = 1
    for j in range(n):
        if res[i][0] < res[j][0] and res[i][1] < res[j][1]:
            cnt += 1
    arr.append(cnt)
for i in arr:
    print(i, end=' ')
