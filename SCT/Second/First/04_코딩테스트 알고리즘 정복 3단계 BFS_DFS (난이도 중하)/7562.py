from collections import deque
import sys

def bfs(x,y, x_e, y_e):
    q = deque()
    q.append([x,y])
    visited[x][y] = 0

    dx = [2, 2 ,-2 ,-2 , 1 , 1, -1 , -1]
    dy = [1, -1 ,1, -1 , 2, -2, 2, -2 ]

    while q:
        a,b = q.popleft()
        if a == x_e and b == y_e:
            return visited[a][b]
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<l and 0<=ny<l:
                if visited[nx][ny] == -1:
                    q.append([nx,ny])
                    visited[nx][ny] = visited[a][b] + 1

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    l = int(sys.stdin.readline().rstrip())
    a_s, b_s = map(int, sys.stdin.readline().rstrip().split())
    a_e, b_e = map(int, sys.stdin.readline().rstrip().split())

    graph = [[1 for _ in range(l)] for _ in range(l)]
    visited = [[-1 for _ in range(l)] for _ in range(l)]

    result = bfs(a_s,b_s, a_e, b_e)
    print(result)