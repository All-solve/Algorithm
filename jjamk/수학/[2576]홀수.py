a = []
for _ in range(7):
    n = int(input())
    if (n % 2 != 0):
        a.append(n)
if (len(a) == 0):
    print(-1)
else:
    print(sum(a))
    print(min(a))
