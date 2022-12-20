N, M = map(int, input().split())
arr = []
res = []

for i in range(N):
    arr.append(input())

for a in range(N-7):
    for b in range(M-7):
        init_W = 0
        init_B = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if arr[i][j] != 'W':
                        init_W += 1
                    if arr[i][j] != 'B':
                        init_B += 1
                else:
                    if arr[i][j] != 'B':
                        init_W += 1
                    if arr[i][j] != 'W':
                        init_B += 1
        res.append(min(init_W, init_B))

print(min(res))
