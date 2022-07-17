import sys
from collections import deque

def bfs(x, y):
    q = deque()
    count = 1
    q.append([x,count])
    while q:
        a,count = q.popleft()
        if a == y:
            return count

        count += 1
        if a*2 <= y:
            q.append([a*2,count])
        if a*10 + 1 <= y:
            q.append([a*10 + 1,count])
    return -1


x, y = map(int, sys.stdin.readline().rstrip().split())

print(bfs(x,y))
