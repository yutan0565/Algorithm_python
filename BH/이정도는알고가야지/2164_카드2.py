import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
q = deque(range(1, n + 1))
while True:
    if len(q) == 1:
        break
    del_number = q.popleft()
    add_number = q.popleft()
    q.append(add_number)

print(q[0])
