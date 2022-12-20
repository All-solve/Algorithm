n = int(input())
f = int(input())
i = 0
while (((n//100) * 100 + i) % f != 0):
    i += 1
if (i < 10):
    print("0"+str(i))
else:
    print(i)
