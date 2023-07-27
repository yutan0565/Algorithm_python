import copy
import sys
from collections import deque

def rotation(x,y,size):
    half_size = size//2
    # print(half_size)
    # print(x,y)
    for i in range(0, size, half_size):
        for j in range(0, size, half_size):
            for a in range(half_size):
                for b in range(half_size):
                    # print([x+i+a, y+j+b])
                    # print([x+j+a, y+size-half_size-i+b])
                    new_graph[x+j+a][y+size-half_size-i+b] = graph[x+i+a][y+j+b]

def melt_ice():
    new_graph = copy.deepcopy(graph)
    for i in range(2**n):
        for j in range(2**n):
            if graph[i][j] == 0:
                continue
            count = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0<=nx<2**n and 0<=ny<2**n:
                    if graph[nx][ny] >= 1:
                        count += 1
            if count < 3:
                new_graph[i][j] -= 1
    return new_graph

def cal_sum():
    sum_ = 0
    for i in range(2**n):
        for j in range(2**n):
            sum_ += graph[i][j]
    return sum_

def bfs(x,y):
    global result_2
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    count = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<2**n and 0<=ny<2**n:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] != 0:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        count += 1
    result_2 = max(result_2, count)

n,q = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(2**n)]
rotation_level = list(map(int,sys.stdin.readline().rstrip().split()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for l in rotation_level:
    # 회전
    if l != 0:
        block_size = 2**l
        new_graph = [[0 for _ in range(2**n)] for _ in range(2**n)]
        for x in range(0, 2**n, block_size):
            for y in range(0,2**n, block_size):
                rotation(x,y,block_size)
        graph = new_graph
    # 녹이기
    graph = melt_ice()

result_1 = cal_sum()
print(result_1)

visited = [[-1 for _ in range(2**n)] for _ in range(2**n)]
result_2 = 0
for i in range(2 ** n):
    for j in range(2 ** n):
        if visited[i][j] == -1:
            if graph[i][j] != 0:
                bfs(i,j)
print(result_2)
