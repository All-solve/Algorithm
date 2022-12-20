for i in range(3):
    a = list(map(int, input().split()))
    res = sum(a)
    if (res == 0):
        print("D")
    elif (res == 1):
        print("C")
    elif (res == 2):
        print("B")
    elif (res == 3):
        print("A")
    else:
        print("E")
