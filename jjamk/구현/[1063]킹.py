king, stone, n = map(str, input().split())

m = []
for i in range(int(n)):
    tmp = input()
    m.append(tmp)

arr1 = ["A", "B", "C", "D", "E", "F", "G", "H"]
arr2 = ["1", "2", "3", "4", "5", "6", "7", "8"]

location_k = []
location_s = []
for i in arr1:
    if king[0:1] == i:
        location_k.append(arr1.index(i))
    if stone[0:1] == i:
        location_s.append(arr1.index(i))
for j in arr2:
    if king[1:2] == j:
        location_k.append(arr2.index(j))
    if stone[1:2] == j:
        location_s.append(arr2.index(j))

for i in m:
    if (i == "R" and location_k[0] < 7):
        if ((location_k[0]+1) == location_s[0] and location_k[1] == location_s[1]
                and location_s[0] < 7):
            location_s[0] += 1
        elif (location_k[0]+1) == location_s[0] and location_k[1] == location_s[1]:
            continue
        location_k[0] += 1
    if (i == "L" and location_k[0] > 0):
        if ((location_k[0]-1) == location_s[0] and location_k[1] == location_s[1]
                and location_s[0] > 0):
            location_s[0] -= 1
        elif ((location_k[0]-1) == location_s[0] and location_k[1] == location_s[1]):
            continue
        location_k[0] -= 1
    if (i == "B" and location_k[1] > 0):
        if (location_k[0] == location_s[0] and (location_k[1]-1) == location_s[1]
                and location_s[1] > 0):
            location_s[1] -= 1
        elif (location_k[0] == location_s[0] and (location_k[1]-1) == location_s[1]):
            continue
        location_k[1] -= 1
    if (i == "T" and location_k[1] < 7):
        if (location_k[0] == location_s[0] and (location_k[1]+1) == location_s[1]
                and location_s[1] < 7):
            location_s[1] += 1
        elif (location_k[0] == location_s[0] and (location_k[1]+1) == location_s[1]):
            continue
        location_k[1] += 1
    if (i == "RT" and location_k[0] < 7 and location_k[1] < 7):
        if ((location_k[0]+1) == location_s[0] and (location_k[1]+1) == location_s[1]
                and location_s[0] < 7 and location_s[1] < 7):
            location_s[0] += 1
            location_s[1] += 1
        elif ((location_k[0]+1) == location_s[0] and (location_k[1]+1) == location_s[1]):
            continue
        location_k[0] += 1
        location_k[1] += 1
    if (i == "LT" and location_k[0] > 0 and location_k[1] < 7):
        if ((location_k[0]-1) == location_s[0] and (location_k[1]+1) == location_s[1]
                and location_s[0] > 0 and location_s[1] < 7):
            location_s[0] -= 1
            location_s[1] += 1
        elif (location_k[0]-1) == location_s[0] and (location_k[1]+1) == location_s[1]:
            continue
        location_k[0] -= 1
        location_k[1] += 1
    if (i == "RB" and location_k[0] < 7 and location_k[1] > 0):
        if ((location_k[0]+1) == location_s[0] and (location_k[1]-1) == location_s[1]
                and location_s[0] < 7 and location_s[1] > 0):
            location_s[0] += 1
            location_s[1] -= 1
        elif ((location_k[0]+1) == location_s[0] and (location_k[1]-1) == location_s[1]):
            continue
        location_k[0] += 1
        location_k[1] -= 1
    if (i == "LB" and location_k[0] > 0 and location_k[1] > 0):
        if ((location_k[0]-1) == location_s[0] and (location_k[1]-1) == location_s[1]
                and location_s[0] > 0 and location_s[1] > 0):
            location_s[0] -= 1
            location_s[1] -= 1
        elif ((location_k[0]-1) == location_s[0] and (location_k[1]-1) == location_s[1]):
            continue
        location_k[0] -= 1
        location_k[1] -= 1
print(arr1[location_k[0]]+arr2[location_k[1]])
print(arr1[location_s[0]] + arr2[location_s[1]])
