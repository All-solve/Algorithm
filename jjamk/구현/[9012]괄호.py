import sys

n = int(input())
for i in range(n):
    list = input()
    flag = 0
    stack = []
    for j in list:
        if j == "(":
            # print(j)
            stack.append(j)
        elif j == ")":
            try:
                stack.pop()
            except:
                flag = 1
    if stack == [] and flag == 0:
        print("YES")
        print(stack)
    elif flag == 1 or stack:
        print("NO")
        print(stack)
