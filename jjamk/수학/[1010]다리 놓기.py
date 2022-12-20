import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    x = 1
    y = 1
    a, b = map(int, sys.stdin.readline().rstrip().split())
    for j in range((b-a)+1, b+1):
        if (b-(b-a) == 1):
            x = b
            break
        x *= j
    for k in range(1, a+1):
        y *= k
    print(x//y)
