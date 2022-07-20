import sys
from collections import deque


def bfs(graph, visited, n, cut, x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny >=0 and nx<n and ny<n:
                if visited[nx][ny] == False:
                    if graph[nx][ny] > cut:
                        q.append([nx, ny])
                        visited[nx][ny] = True

n = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]


cut = max(map(max, graph))
temp = []

while True:
    if cut == -1:
        break

    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and graph[i][j]> cut:
                bfs(graph, visited, n, cut, i, j)
                count += 1
    temp.append(count)
    cut -= 1

print(max(temp))


