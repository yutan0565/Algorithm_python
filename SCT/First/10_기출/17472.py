import copy
import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs_find_group(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    graph[x][y] = group_name

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] != 0:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        graph[nx][ny] = group_name



n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
reset_visited = [[-1 for _ in range(m)] for _ in range(n)]

# 영역 나누기
group_name = 1
visited = copy.deepcopy(reset_visited)
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            if visited[i][j] == -1:
                bfs_find_group(i,j)
                group_name += 1

# 다리 종류 만들어 보기
