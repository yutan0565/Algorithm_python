import sys
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    graph[n] = 0
    count = 0
    while q:
        a = q.popleft()
        if a == k:
            count += 1
        for nx in [ 2*a, a +1, a-1]:
            if 0 <= nx < 100001:
                if graph[nx] == -1 or graph[nx] == graph[a] + 1:
                    q.append(nx)
                    graph[nx] = graph[a] + 1

    return graph[k] , count

n, k = map(int, sys.stdin.readline().rstrip().split())

graph = [-1 for _ in range(100000+1)]
ti, c = bfs()

print(ti)
print(c)

