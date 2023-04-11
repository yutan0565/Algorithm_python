from collections import deque
import sys
"""
1. 범위 제대로 !!!
"""

def bfs(x, y):
    q = deque()
    q.append(x)
    visited[x] = 0

    while q:
        a = q.popleft()
        if a == k:
            return visited[a]
        for nx in [a-1, a+1, 2*a]:
            if 0<= nx <= 100000:
                if visited[nx] == -1:
                    q.append(nx)
                    visited[nx] = visited[a] + 1


n,k = map(int, sys.stdin.readline().rstrip().split())

visited = [-1] * (100000+1)

result =  bfs(n, k)
print(result)