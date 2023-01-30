import sys

t = int(input())

for i in range(t):
    arr = []
    n, idx = map(int, input().split())
    arr = list(map(int, input().split()))
    s = [0 for i in range(n)]
    s[idx] = 1
    cnt = 0
    while True:
        if max(arr) == arr[0]:
            cnt += 1
            if s[0] == 1:
                print(cnt)
                break
            else:
                del arr[0]
                del s[0]
        else:
            arr.append(arr[0])
            del arr[0]
            s.append(s[0])
            del s[0]
