import copy
import sys
from collections import deque

def rotation_block(level):
    new_graph = [[0 for _ in range(total_len)] for _ in range(total_len)]
    group_size = 2**level
    block_size = group_size // 2

    for g_x in range(0,total_len, group_size):
        for g_y in range(0,total_len,group_size):
            for b_x in range(0,group_size,block_size):
                for b_y in range(0,group_size,block_size):
                    new_x = g_x + b_y
                    new_y = g_y + group_size - block_size- b_x
                    for i in range(block_size):
                        for j in range(block_size):
                            new_graph[new_x+i][new_y+j] = graph[g_x+b_x+i][g_y+b_y+j]
    return new_graph

def melt_ice():
    new_graph = copy.deepcopy(graph)
    for i in range(total_len):
        for j in range(total_len):
            if graph[i][j] != 0:
                count = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<total_len and 0<=ny<total_len:
                        if graph[nx][ny] >= 1:
                            count += 1
                if count < 3:
                    new_graph[i][j] -= 1
    return new_graph

def cal_total_ice():
    ice = 0
    for i in range(total_len):
        for j in range(total_len):
            ice += graph[i][j]
    return ice

def fine_max_group(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    size = 1

    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<total_len and 0<=ny<total_len:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] != 0:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        size += 1
    return size

n,turn = map(int,sys.stdin.readline().rstrip().split())
total_len = 2**n
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(total_len)]
level_list = list(map(int,sys.stdin.readline().rstrip().split()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for l in level_list:
    if l == 0:
        pass
    else:
        graph = rotation_block(l)
    graph = melt_ice()

total_ice = cal_total_ice()

max_size = 0
visited = [[-1 for _ in range(total_len)] for _ in range(total_len)]
for i in range(total_len):
    for j in range(total_len):
        if visited[i][j] == -1:
            if graph[i][j] != 0:
                size = fine_max_group(i,j)
                max_size = max(size, max_size)
print(total_ice)
print(max_size)