import sys

n, m, b = map(int, input().split())
str = []
ans = int(1e9)
for i in range(n):
    s = list(map(int, input().split()))
    str += s

for i in range(257):  # 0부터 257까지
    max = 0
    min = 0
    for j in range(n*m):
        if str[j] < i:  # 원소가 더 크면 쌓기
            min += (i - str[j])
        else:
            max += (str[j] - i)  # 원소가 더 작으면 제거 후 보관
    invent = max + b
    if invent < min:  # 인벤토리 부족 시 못하므로 패스
        continue

    time = 2 * max + min

    if time <= ans:
        ans = time
        high = i
print(ans, high)
