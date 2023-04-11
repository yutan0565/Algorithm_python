import copy
from collections import deque
from itertools import combinations
import sys

def bfs(x,y):
    q = deque()
    q.append([x,y,1])
    visited[x][y] = 1

    dx = [0,-1,0]
    dy = [-1,0,1]


    while q:
        a,b,dis = q.popleft()
        if graph[a][b] == 1 and dis <= d:
            if [a,b] not in dead_list:
                dead_list.append([a,b])
            break

        for i in range(3):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == -1:
                    if dis+1 <= d:
                        q.append([nx,ny,dis+1])
                        visited[nx][ny] = 1


n,m,d = map(int, sys.stdin.readline().rstrip().split())
reset_graph = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

reset_visited = [[-1 for _ in range(m)] for _ in range(n)]

new_line = [[0 for _ in range(m)]]

arrow_list= list(combinations(range(m), 3))

result = 0
for arrow in arrow_list:
    graph = copy.deepcopy(reset_graph)
    start_list = []
    kill_count = 0

    for next in range(n+1):
        dead_list = []
        for arr_idx in arrow:
            visited = copy.deepcopy(reset_visited)
            bfs(n-1,arr_idx )
        kill_count += len(dead_list)
        for dead_x,dead_y in dead_list:
            graph[dead_x][dead_y] = 0
        graph = new_line + graph
        graph =  graph[0:n]

    result = max(kill_count, result)

print(result)

