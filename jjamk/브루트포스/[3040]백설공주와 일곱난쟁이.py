a = []
sum = 0
r_i = 0
r_j = 0
for i in range(9):
    n = int(input())
    a.append(n)
    sum += n

sum -= 100
for i in range(9):
    for j in range(i+1, 9):
        if (a[i] + a[j] == sum):
            r_i = i
            r_j = j
            break
        
for i in range(len(a)):
    if (i != r_i and i != r_j):
        print(a[i])
