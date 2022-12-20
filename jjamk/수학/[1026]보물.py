n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0
for i in range(n):
    sum += min(a)*max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))
print(sum)
