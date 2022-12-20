n = int(input())

arr1 = {1,3, 5, 7, 8, 10, 12}
arr2 = {4, 6, 9, 11}

for i in range(n):
    y, m = map(int, input().split())
    if (m == 1):
        print(y-1, 12, 31)
    elif (m == 3):
        if ((y % 100 != 0 and y % 4 == 0) or y % 400 == 0):
            print(y, m-1, 29)
        else:
            print(y, m-1, 28)
    elif (m-1 in arr1):
        print(y, m-1, 31)
    else:
        print(y, m-1, 30)
