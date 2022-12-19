a = []
sum = 0
for i in range(10):
    n = int(input())
    a.append(n)

for u in a:
    sum += u
    if sum >= 100:
        if 100 - (sum - u) >= sum - 100:
            print(sum)
            break
        else:
            print(sum-u)
            break

if (sum < 100):
    print(sum)
