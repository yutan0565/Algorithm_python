import sys
from collections import deque

def bfs(graph,x,y, group_count):
    q = deque()
    q.append([x,y])
    graph[x][y] = group_count

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = group_count
                    q.append([nx,ny])

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0] * m for _ in range(n)]
    start = []
    for _ in range(k):
        b, a = map(int, sys.stdin.readline().rstrip().split())
        graph[a][b] = 1

    group_count = 1

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                group_count += 1
                bfs(graph, x,y, group_count)
    # for g in graph:
    #     print(g)
    print(group_count - 1)

