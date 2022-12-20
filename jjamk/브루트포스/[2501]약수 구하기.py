n, k = map(int, input().split())
a = []
for i in range(1, n+1):
    if (n % i == 0):
        a.append(i)
if (len(a) < k):
    print(0)
else:
    a.sort()
    print(a[k-1])
