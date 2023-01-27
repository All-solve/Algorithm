import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
deque = deque([])
for i in range(n):
    inp = sys.stdin.readline().rstrip()
    try:
        a, b = inp.split(' ')
    except:
        a = inp
    if a == "push_back":
        b = int(b)
        deque.append(b)
        # print(b)
    elif a == "push_front":
        b = int(b)
        deque.appendleft(b)
    elif a == "pop_front":
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif a == "pop_back":
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif a == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif a == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)
    elif a == "empty":
        if deque:
            print(0)
        else:
            print(1)
    elif a == "size":
        print(len(deque))
