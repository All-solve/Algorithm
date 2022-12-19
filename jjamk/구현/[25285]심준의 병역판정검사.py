n = int(input())

for i in range(n):
    a, b = map(float, input().split())
    if (a < 140.1):
        print(6)
    elif (a >= 140.1 and a < 146):
        print(5)
    elif (a >= 146 and a < 159):
        print(4)
    elif (a >= 159 and a < 161):
        if (b/((a*0.01))**2 >= 16 and b/((a*0.01))**2 < 35):
            print(3)
        elif (b/((a*0.01))**2 < 16 or b/((a*0.01))**2 >= 35):
            print(4)
    elif(a >= 161 and a < 204):
        if (b/((a*0.01))**2 >= 20 and b/((a*0.01))**2 < 25):
            print(1)
        elif ((b/((a*0.01))**2 >= 18.5 and b/((a*0.01))**2 < 20) or (b/((a*0.01))**2 >= 25 and b/((a*0.01))**2 < 30)):
            print(2)
        elif ((b/((a*0.01))**2 >= 16 and b/((a*0.01))**2 < 18.5) or (b/((a*0.01))**2 >= 30 and b/((a*0.01))**2 < 35)):
            print(3)
        elif (b/((a*0.01))**2 >= 35 or b/((a*0.01))**2 < 16):
            print(4)
    elif (a >= 204):
        print(4)
