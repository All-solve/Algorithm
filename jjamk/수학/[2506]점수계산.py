n = int(input())
a = list(map(int, input().split()))
score = 0
flag = 0
for i in a:
    if (i == 1):
        score += 1+flag
        flag += 1
    else:
        flag = 0
print(score)
