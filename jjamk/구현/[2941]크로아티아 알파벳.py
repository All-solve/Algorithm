n = input()
cro = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
cnt = 0
i = 0
flag = 0
while (i < len(n)):
    res = n[i:i+2]
    for c in cro:
        if (res == c):
            cnt += 1
            i += 1
            flag = 1
            break
        elif (n[i:i+3] == "dz="):
            cnt += 1
            i += 2
            flag = 1
            break
    if (flag == 0):
        cnt += 1
    flag = 0
    i += 1
print(cnt)
