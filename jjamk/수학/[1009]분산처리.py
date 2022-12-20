import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    a = a % 10
    if (a == 0):
        print(10)
    elif (a == 1 or a == 5 or a == 6):
        print(a)
    elif (a == 4 or a == 9):
        if (b % 2 != 0):
            print(a)
        else:
            print((a*a) % 10)
    else:
        if (b % 4 == 1):
            print(a)
        elif (b % 4 == 2):
            print((a*a) % 10)
        elif (b % 4 == 3):
            print((a*a*a) % 10)
        else:
            print((a*a*a*a) % 10)
