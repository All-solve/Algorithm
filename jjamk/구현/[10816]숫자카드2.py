import sys

n = int(sys.stdin.readline().rstrip())
arr1 = sorted(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))

count = {}
for card in arr1:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in arr2:
    res = count.get(target)
    if res == None:
        print(0, end=' ')
    else:
        print(res, end=' ')
