import sys
from collections import deque
"""
1. 90 도 오른쪽 회전
2. 얼름 

"""

def rotation(x,y, graph, temp_size):
    global new_graph
    for i in range(temp_size):
        for j in range(temp_size):
            new_i = x + j
            new_j =  y + temp_size - i -1
            new_graph[new_i][new_j] = graph[x+i][y+j]

def fire():
    global new_graph
    temp_new_graph = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            temp_new_graph[i][j] = new_graph[i][j]

    for i in range(size):
        for j in range(size):
            count = 0
            for a,b in [[i-1,j],[i+1,j] ,[i,j-1] ,[i,j+1] ]:
                if 0<=a<size and 0<=b<size:
                    if temp_new_graph[a][b] != 0:
                        count +=1
            if count <3 and new_graph[i][j] >0:
                new_graph[i][j] = new_graph[i][j]  - 1

def bfs(x,y):
    global  graph, ice_count, result_max
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    ice_count += graph[x][y]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    group_count = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<size and 0<=ny<size:
                if graph[nx][ny] != 0:
                    if visited[nx][ny] == False:
                        q.append([nx,ny])
                        visited[nx][ny] = True
                        ice_count += graph[nx][ny]
                        group_count += 1
    result_max = max(result_max, group_count)




n,f = map(int, sys.stdin.readline().rstrip().split())
size = 2**n

graph = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(size) ]

l = list(map(int, sys.stdin.readline().rstrip().split()))
temp_size = 0


for x in l:
    new_graph = [[0 for _ in range(size)] for _ in range(size)]
    temp_size = 2**x
    for i in range(0,size, temp_size):
        for j in range(0, size, temp_size):
            rotation(i,j, graph, temp_size)
    fire()
    for i in range(size):
        for j in range(size):
            graph[i][j] = new_graph[i][j]

visited = [[False for _ in range(size)] for _ in range(size)]

ice_count = 0
result_max = 0

for i in range(size):
    for j in range(size):
        if visited[i][j] == False and graph[i][j] != 0:
            bfs(i,j)

print(ice_count)
print(result_max)




