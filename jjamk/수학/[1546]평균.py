n = int(input())
sum = 0
a = list(map(int, input().split()))
for i in a:
    tmp = i/max(a)*100
    sum += tmp
print(sum/n)
