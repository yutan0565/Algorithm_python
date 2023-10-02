import copy
import sys
from collections import deque

def rotatate_right(level):
    global graph
    mid_size = 2**level
    small_size = 2**(level-1)
    new_graph = [[0 for _ in range(total_size)] for _ in range(total_size)]
    for mid_i in range(0, total_size, mid_size):
        for mid_j in range(0, total_size, mid_size):
            for small_i in range(0,mid_size, small_size):
                for small_j in range(0,mid_size, small_size):
                    a = mid_i + small_i
                    b = mid_j + small_j

                    nx = mid_i + small_j
                    ny = mid_j + mid_size- small_size - small_i

                    for i in range(small_size):
                        for j in range(small_size):

                            new_graph[nx + i][ny+j] = graph[a+i][b+j]
    graph =  new_graph

def melt_ice():
    global graph
    new_graph = copy.deepcopy(graph)
    for i in range(total_size):
        for j in range(total_size):
            ice_cnt = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0<=nx<total_size and 0<=ny<total_size:
                    if graph[nx][ny] != 0:
                        ice_cnt += 1
            if ice_cnt < 3:
                if graph[i][j] != 0:
                    new_graph[i][j] -= 1
    graph = new_graph

def cal_total_ice():
    total_ice = 0
    for i in range(total_size):
        for j in range(total_size):
            total_ice += graph[i][j]
    return total_ice

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    cnt = 1
    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<total_size and 0<=ny<total_size:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] != 0:
                        cnt += 1
                        visited[nx][ny] = 1
                        q.append([nx,ny])
    return cnt

n,q = map(int,sys.stdin.readline().rstrip().split())
total_size = 2**n
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(total_size)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

input_level_list = list(map(int,sys.stdin.readline().rstrip().split()))

for now_level in input_level_list:
    if now_level != 0:
        rotatate_right(now_level)
    melt_ice()

total_ice = cal_total_ice()
visited = [[-1 for _ in range(total_size)] for _ in range(total_size)]
max_size = 0
for i in range(total_size):
    for j in range(total_size):
        if visited[i][j] == -1:
            if graph[i][j] != 0:
                now_size = bfs(i,j)
                max_size = max(max_size, now_size)
print(total_ice)
print(max_size)