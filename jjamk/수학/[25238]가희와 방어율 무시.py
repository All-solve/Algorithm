a, b = map(float, input().split())

if (a-a*(b*0.01) >= 100):
    print(0)
else:
    print(1)
