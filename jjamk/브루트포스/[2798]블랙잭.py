import sys

n, m = map(int, input().split())
arr = []
max = 0
arr = list(map(int, input().split()))

for i in range(n-2):
    for y in range(i+1, n-1):
        for j in range(y+1, n):
            k = arr[i] + arr[y] + arr[j]
            if k <= m:
                if max < k:
                    max = k
print(max)
