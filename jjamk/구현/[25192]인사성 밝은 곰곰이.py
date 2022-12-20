import sys

n = int(sys.stdin.readline().rstrip())
save = 0
arr = set()

for i in range(n):
    m = sys.stdin.readline().rstrip()
    if (m != "ENTER"):
        arr.add(m)
    else:
        save += len(arr)
        arr.clear()


print(len(arr)+save)
