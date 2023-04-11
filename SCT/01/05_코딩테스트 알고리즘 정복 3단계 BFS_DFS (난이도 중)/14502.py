from collections import deque
import sys
from itertools import combinations

def bfs(x,y):
    q = deque()
    for s in virus:
        a = s[0]
        b = s[1]
        q.append([a,b])
        visited[a][b] = 1
    count = 0

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    if [nx,ny] not in wall_point:
                        if visited[nx][ny] == -1:
                            q.append([nx,ny])
                            visited[nx][ny] = 1
                            count += 1
    return count

def make_point(number):
    x = number//m
    y = number%m
    return x,y

n,m = map(int ,sys.stdin.readline().rstrip().split())
graph = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

virus = []
ori_wall = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append([i,j])
        if graph[i][j] == 1:
            ori_wall.append([i,j])


wall_case = list(combinations(range(n*m), 3))

final_result = -1

for k in range(len(wall_case)):
    wall_point = []
    for p in wall_case[k]:
        a,b = make_point(p)
        if graph[a][b] != 0:
            break
        wall_point.append([a,b])

    if len(wall_point) != 3:
        continue

    visited = [[-1] * m for _ in range(n)]
    temp = bfs(i,j)
    safe_zone = n*m - len(virus) - len(ori_wall) - 3- temp
    final_result = max(safe_zone, final_result)

print(final_result)