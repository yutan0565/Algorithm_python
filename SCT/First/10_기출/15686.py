import copy
import sys
from itertools import combinations
from collections import deque


def bfs(list_start):
    q = deque()
    for x,y in list_start:
        q.append([x,y])
        visited[x][y] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    len_chiken = 0
    while q:
        for _ in range(len(q)):
            a,b = q.popleft()
            if graph[a][b] == 1:
                len_chiken += visited[a][b]
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        q.append([nx,ny])
                        visited[nx][ny] = visited[a][b] + 1
    return len_chiken




n,m = map(int,sys.stdin.readline().rstrip().split())
graph = []
list_chicken = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if graph[i][j] == 2:
            list_chicken.append([i,j])
            graph[i][j] = 0
list_candi_chicken = list(combinations(list_chicken, m))
reset_visited = [[-1 for _ in range(n)] for _ in range(n)]

result = int(1e9)
for candi_chicken in list_candi_chicken:
    visited = copy.deepcopy(reset_visited)
    temp = bfs(candi_chicken)
    result = min(temp, result)
print(result)


