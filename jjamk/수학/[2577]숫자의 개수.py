a = 1
for i in range(3):
    a *= int(input())
b = str(a)
for j in range(10):
    tmp = 0
    for k in range(len(b)):
        if (b[k] == str(j)):
            tmp += 1
    print(tmp)
