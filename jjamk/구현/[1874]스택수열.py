import sys

n = int(input())
arr = []
res = []
flag = 0
cur = 1
for i in range(n):
    num = int(input())
    # 입력한 수 만날때까지 푸시
    while cur <= num:
        arr.append(cur)
        res.append("+")
        cur += 1
    if arr[-1] == num:
        arr.pop()
        res.append("-")
    else:
        print("NO")
        flag = 1
        break
if flag == 0:
    for i in res:
        print(i)
