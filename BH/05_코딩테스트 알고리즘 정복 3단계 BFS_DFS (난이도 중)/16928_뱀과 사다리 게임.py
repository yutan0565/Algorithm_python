import sys
from collections import deque
def bfs(graph, visited, up, down):
    q = deque()
    q.append(1)
    visited[1] = True

    count = 0
    dx = [1,2,3,4,5,6]

    while q:
        a = q.popleft()
        if a == 100:
            return graph[100]

        for i in range(6):
            nx = a + dx[i]
            if 0 < nx <=100:
                    if nx in up.keys():
                        nx = up[nx]
                    if nx in down.keys():
                        nx = down[nx]
                    if visited[nx] == False:
                        q.append(nx)
                        visited[nx] = True
                        graph[nx] = graph[a] + 1

graph = [ 0 ] * 101
visited = [True] + [ False] * 100

n,m = map(int, sys.stdin.readline().rstrip().split())

up = {}
down = {}

for i in range(n):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    up[a] = b
for i in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    down[a] = b

result = bfs(graph, visited, up, down)
print(result)
