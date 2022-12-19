x = []
y = []

max = 0
for i in range(4):
    out, In = map(int, input().split())
    x.append(out)
    y.append(In)
tmp = y[0]
for j in range(1, 4):
    if (max < tmp):
        max = tmp
    tmp += y[j]-x[j]
print(max)
