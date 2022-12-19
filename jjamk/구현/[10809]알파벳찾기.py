a = input()
count = 0
res = []
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in alpha:
    count = 0
    for j in a:
        if (j == i):
            tmp = a.index(i)
            res.append(tmp)
            break
        else:
            count += 1
    if (count == len(a)):
        res.append(-1)

real = []
for k in res:
    real.append(str(k))
print(' '.join(real))
