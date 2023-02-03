import sys

while True:
    n = input()
    arr = []
    flag = 0
    if n == '.':
        break
    else:
        for i in n:
            if i == "(":
                arr.append(i)
            elif i == "[":
                arr.append(i)
            elif i == ")":
                if arr != [] and arr.pop() == "(":
                    pass
                else:
                    print("no")
                    flag = 1
                    break

            elif i == "]":
                if arr != [] and arr.pop() == "[":
                    pass
                else:
                    print("no")
                    flag = 1
                    break
    if flag == 0 and arr == []:
        print("yes")
    elif flag == 0:
        print("no")
