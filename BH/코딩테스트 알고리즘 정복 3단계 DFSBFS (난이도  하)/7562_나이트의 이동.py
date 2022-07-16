import sys
from collections import deque

def bfs(graph, start, end):
    q = deque()
    q.append(start)
    graph[start[0]][start[1]] = 1

    dx = [2, 2 , -2 , -2, 1, 1, -1, -1]
    dy = [1, -1, 1 , -1 , 2, -2, 2 , -2 ]

    while q:
        a, b = q.popleft()
        if a == end[0] and b == end[1]:
            print(graph[end[0]][end[1]] - 1)
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >=0 and ny >=0 and nx <n and ny <n:
                if graph[nx][ny] == 0:
                    q.append([nx, ny])
                    graph[nx][ny] = graph[a][b] + 1


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    start = list(map(int, sys.stdin.readline().rstrip().split()))
    end = list(map(int, sys.stdin.readline().rstrip().split()))

    graph = [[0]*n for _ in range(n)]
    bfs(graph, start, end)

