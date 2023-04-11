from collections import deque
import sys

def bfs():
    q = deque()
    q.append(s)
    visited[s] = 0
    dx = [u,-d]

    while q:
        a = q.popleft()
        if a == g:
            return visited[a]
        for i in range(2):
            nx = a + dx[i]
            if 1<= nx < f+1:
                if visited[nx] == -1:
                    q.append(nx)
                    visited[nx] = visited[a] + 1
    return -1



f,s,g,u,d = map(int ,sys.stdin.readline().rstrip().split())

visited = [-1] *(f+1)
result = bfs()
if result == -1:
    print("use the stairs")
else:
    print(result)