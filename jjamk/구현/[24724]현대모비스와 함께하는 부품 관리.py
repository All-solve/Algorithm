import sys

t = int(sys.stdin.readline().rstrip())
for i in range(1, t+1):
    x = []
    y = []
    n = int(sys.stdin.readline().rstrip())
    a, b = map(int, sys.stdin.readline().rstrip().split())
    for j in range(n):
        x1, y1 = map(int, sys.stdin.readline().rstrip().split())
        x.append(x1)
        y.append(y1)
    print("Material Management", i)
    print("Classification ---- End!")
