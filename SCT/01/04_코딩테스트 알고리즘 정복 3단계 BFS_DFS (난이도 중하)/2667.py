from collections import deque
import sys

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    count_house = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 1:
                    if visited[nx][ny] == -1:
                        q.append([nx,ny])
                        visited[nx][ny] = 0
                        count_house += 1
    return count_house

n = int(sys.stdin.readline().rstrip())
graph = [ list(map(int, list(sys.stdin.readline().rstrip())))  for _ in range(n)      ]
visited = [ [-1] * n for _ in range(n)]

result = []
count = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            if visited[i][j] == -1:
                result.append(bfs(i,j))
                count+=1

print(count)
result.sort()
for r in result:
    print(r)