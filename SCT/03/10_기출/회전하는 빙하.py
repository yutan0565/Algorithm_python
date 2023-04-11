import copy
import sys
from collections import deque

def rotation(level):
    new_graph = [[0 for _ in range(map_len)] for _ in range(map_len)]
    group_size = 2**level
    rotation_size = group_size//2

    for group_row in range(0,map_len, group_size):
        for group_col in range(0,map_len, group_size):
            for rotation_row in range(0,group_size, rotation_size):
                for rotation_col in range(0,group_size, rotation_size):
                    new_x = group_row + rotation_col
                    new_y = group_col +rotation_size - rotation_row
                    for i in range(rotation_size):
                        for j in range(rotation_size):
                            new_graph[new_x+i][new_y+j]= graph[group_row+rotation_row+i][group_col+rotation_col+j]
    return new_graph

def melt_ice():
    new_graph = copy.deepcopy(graph)
    for i in range(map_len):
        for j in range(map_len):
            if graph[i][j] != 0:
                count = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<map_len and 0<=ny<map_len:
                        if graph[nx][ny] != 0:
                            count += 1
                if count < 3:
                    new_graph[i][j] -= 1
    return new_graph

def cal_ice():
    count = 0
    for i in range(map_len):
        for j in range(map_len):
            count += graph[i][j]
    return count

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    count = 1

    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<map_len and 0<=ny<map_len:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] != 0:
                        count += 1
                        q.append([nx,ny])
                        visited[nx][ny] = 1
    return count

n, turn = map(int,sys.stdin.readline().rstrip().split())
map_len = 2**n
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(map_len)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

l_list = list(map(int,sys.stdin.readline().rstrip().split()))

for level in l_list:
    if level != 0:
        graph = rotation(level)
    graph = melt_ice()

ice_count = cal_ice()

visited = [[-1 for _ in range(map_len)] for _ in range(map_len)]
max_group = 0
for i in range(map_len):
    for j in range(map_len):
        if visited[i][j] == -1:
            if graph[i][j] != 0:
                temp = bfs(i,j)
                max_group = max(temp, max_group)

print(ice_count)
print(max_group)

