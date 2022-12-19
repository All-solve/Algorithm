a = list(map(int, input().split()))
tmp = 0
for i in range(7):
    if (a[i] - a[i+1] < 0):
        tmp += 1
    elif (a[i] - a[i+1] > 0):
        tmp -= 1
if (tmp == 7):
    print("ascending")
elif (tmp == -7):
    print("descending")
else:
    print("mixed")
