m = int(input())
n = int(input())
a = []

for i in range(m, n+1):
    for j in range(2, i+1):
        if ((i == 1) or (i != j and i % j == 0)):
            break
        elif (i == j):
            a.append(i)
if (len(a) == 0):
    print(-1)
else:
    print(sum(a))
    print(min(a))
