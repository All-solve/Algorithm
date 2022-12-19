date = int(input())
count = 0
a = list(map(int, input().split()))
for i in a:
    if (date == i):
        count += 1
print(count)
