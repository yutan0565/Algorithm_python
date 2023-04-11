from collections import deque
import sys

def bfs():
    q = deque()
    q.append(n)
    visited[n] = 0

    while q:
        a = q.popleft()
        if a == k:
            return visited[a]
        for nx in [a-1, a+1, 2*a]:
            if 0<=nx<100001:
                if visited[nx] == -1:
                    if nx == 2*a:
                        visited[nx] = visited[a]
                        q.appendleft(nx)
                    else:
                        visited[nx] = visited[a] + 1
                        q.append(nx)

n,k = map(int ,sys.stdin.readline().rstrip().split())

visited = [-1] * (100000 + 1)

result = bfs()
print(result)