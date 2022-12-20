a = input().upper()
res = list(set(a))

count = []
for i in res:
    cnt = a.count(i)
    count.append(cnt)

if (count.count(max(count)) > 1):
    print("?")
else:
    index = count.index(max(count))
    print(res[index])
