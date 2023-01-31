import copy
import sys

def spread_dust(graph):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    new_graph = copy.deepcopy(graph)
    for machine in machine_point:
        new_graph[machine[0]][machine[1]] = -1

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if not(0<=nx<n and 0<=ny<m):
                        continue
                    if graph[nx][ny] == -1:
                        continue
                    new_graph[nx][ny] += graph[i][j]// 5
                    new_graph[i][j] -= graph[i][j]// 5
    return new_graph

def up_blow_wind(start):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    direct = 0
    x,y  = start[0] + dx[direct], start[1] + dy[direct]
    while 1:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if not(0<=nx<=start[0] and 0<=ny<m):
            direct = (direct + 1 ) % 4
            nx = x + dx[direct]
            ny = y + dy[direct]
        if graph[nx][ny] == -1:
            graph[x][y] = 0
            break
        graph[x][y] = graph[nx][ny]
        x,y = nx,ny

def down_blow_wind(start):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    direct = 0
    x,y  = start[0] + dx[direct], start[1] + dy[direct]
    while 1:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if not(start[0]<=nx< n and 0<=ny<m):
            direct = (direct + 1 ) % 4
            nx = x + dx[direct]
            ny = y + dy[direct]
        if graph[nx][ny] == -1:
            graph[x][y] = 0
            break
        graph[x][y] = graph[nx][ny]
        x,y = nx,ny

n,m,t = map(int, sys.stdin.readline().rstrip().split())
machine_point = []
graph = []
for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    graph.append(temp)
    for j in range(m):
        if graph[i][j] == -1:
            machine_point.append([i,j])

for time in range(t):
    graph = spread_dust(graph)
    up_blow_wind(machine_point[0])
    down_blow_wind(machine_point[1])

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]  > 0:
            result += graph[i][j]

print(result)