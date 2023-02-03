import sys

n, m = map(int, input().split())

arr = list(map(int, input().split()))
start = 0
end = max(arr)
while start <= end:
    middle = (start + end) // 2
    s = 0
    for i in range(n):
        if middle < arr[i]:
            s += arr[i] - middle
    if s >= m:
        start = middle + 1
    else:
        end = middle - 1
print(end)
