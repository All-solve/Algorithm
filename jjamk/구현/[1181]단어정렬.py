import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(input())

arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)
