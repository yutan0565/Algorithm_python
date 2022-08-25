import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
q = deque()

for _ in range(n):
    order = list(sys.stdin.readline().rstrip().split())
    if order[0] == "push_front":
        number= int(order[1])
        q.insert(0, number)
    if order[0] == "push_back":
        number = int(order[1])
        q.append(number)

    elif order[0] == "pop_front":
        if len(q) == 0:
            print(-1)
        else:
            pop_number = q.popleft()
            print(pop_number)
    elif order[0] == "pop_back":
        if len(q) == 0:
            print(-1)
        else:
            pop_number = q.pop()
            print(pop_number)
    elif order[0] == "size":
        print(len(q))
    elif order[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif order[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
