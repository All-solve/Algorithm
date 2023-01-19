import sys

n, m = map(int, input().split())
arr = []
max = 0
for i in range(n):
    arr.append(int(input()))

for i in range(n-1):
    for j in range(i+2):
        k = arr[i] + arr[i+1] + arr[j]
        if k <= m:
            if max < k:
                max = k
