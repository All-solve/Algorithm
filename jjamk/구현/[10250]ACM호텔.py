import sys

n = int(input())

idx = 0
while idx < n:
    h, w, num = map(int, input().split())
    cnt = 0
    for i in range(1, w+1):
        y = i
        for j in range(1, h+1):
            x = j
            cnt += 1
            if cnt == num:
                break
        if cnt == num:
            break
    if y < 10:
        print(x, 0, y, sep='')
    else:
        print(x, y, sep='')
    idx += 1
