a = []
for i in range(9):
    x = int(input())
    a.append(x)
ma = max(a)
print(ma)
print(a.index(ma)+1)
