import sys
from collections import deque

def bfs():
    global cheese
    q = deque()
    q.append([0,0])
    visited[0][0] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == False:
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        visited[nx][ny] = True
                        cheese -=1
                    else:
                        q.append([nx, ny])
                        visited[nx][ny] = True

n,m = map(int, sys.stdin.readline().rstrip().split())
cheese = 0
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())) )
    for j in range(m):
        if graph[i][j] == 1:
            cheese += 1
ti = 0
count_list = [cheese]

while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    bfs()
    count_list.append(cheese)
    ti +=1
    if cheese == 0 :
        break
print(ti)
print(count_list[-2])
