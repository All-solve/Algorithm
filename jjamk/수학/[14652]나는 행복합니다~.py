a, b, c = map(int, input().split())
n = 0
m = 0
for i in range(a):
    if (b*i <= c and b*(i+1) >= c):
        n = i
for j in range(b):
    if ((b*n)+j == c):
        m = j
print(n, m)
