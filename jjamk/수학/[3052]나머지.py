a = []
for _ in range(10):
    x = int(input())
    a.append(x % 42)
s1 = set(a)
lis = list(s1)

print(len(lis))
