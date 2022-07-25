import sys
from collections import deque


def bfs():
    q = deque()
    x,y = start
    e_x, e_y = end
    x -= 1
    y -= 1
    e_x -=1
    e_y -=1

    q.append([x,y,0])
    visited[x][y][0] = 0

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b,pos = q.popleft()
        if a == e_x and b == e_y:
            return visited[a][b][pos]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1 and pos == 0:
                    visited[nx][ny][1] = visited[a][b][pos] + 1
                    q.append([nx,ny,1])
                elif graph[nx][ny] == 0 and visited[nx][ny][pos] == -1:
                    visited[nx][ny][pos] = visited[a][b][pos] + 1
                    q.append([nx, ny, pos])


    return -1






n,m = map(int, sys.stdin.readline().rstrip().split())

start = list(map(int,sys.stdin.readline().rstrip().split()))
end = list(map(int,sys.stdin.readline().rstrip().split()))

graph = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

visited_1 = [[ [-1,-1]] * m for _ in range(n)]
visited = [[ [-1,-1]  for _ in range(m) ] for _ in range(n)]

print(visited)
print(visited_1)
result = bfs()
print(result)