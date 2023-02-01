import sys

n = int(input())
arr = []
cnt = {}

for i in range(n):
    m = input()
    m_i = int(m)
    arr.append(m_i)
    if m_i in cnt.keys():
        cnt[m_i] += 1
    else:
        cnt.setdefault(m_i, 1)

print(round(sum(arr)/n))

arr.sort()
print(arr[n//2])

cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
# print(cnt)
res = []
leng = 0
for i in range(len(cnt)):
    if cnt[i][1] == cnt[0][1]:
        res.append(cnt[i][0])
        leng += 1
    else:
        continue
res.sort()
# print(res)
if leng == 1:
    print(res[0])
else:
    print(res[1])

print(arr[-1] - arr[0])
