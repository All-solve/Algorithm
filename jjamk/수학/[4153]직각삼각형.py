import sys

while True:
    n, m, k = map(int, input().split())
    if n == 0 and m == 0 and k == 0:
        break
    elif n == 0 or m == 0 or k == 0:
        print("wrong")
    list = [n, m, k]
    list.sort()
    if list[0]**2 + list[1]**2 == list[2]**2:
        print("right")
    else:
        print("wrong")
