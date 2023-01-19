import sys

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))
for i in b:
    try:
        a.index(i)
    except:
        print(0)
    else:
        print(1)
