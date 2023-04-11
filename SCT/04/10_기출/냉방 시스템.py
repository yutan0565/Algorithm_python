import copy
import sys
from collections import deque

def check_office():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                if graph_temper[i][j] < k:
                    return -1
    return 1

def blow_air(x,y,direct):
    q= deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    x = x + dx[direct]
    y = y + dy[direct]
    graph_temper[x][y] += 5
    visited[x][y] = 1
    q.append([x,y,4])
    while q:
        a,b,temp = q.popleft()
        if temp == 0:
            continue
        for type in range(3):
            # 직선 이동
            if type == 0:
                nx = a + dx[direct]
                ny = b + dy[direct]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        if direct not in graph_wall[a][b]:
                            graph_temper[nx][ny] += temp
                            visited[nx][ny] = 1
                            q.append([nx,ny,temp-1])
            # 위 or 좌
            else:
                sub_direct = dict_check_direct[direct][type-1]
                check_x = a + dx[sub_direct]
                check_y = b + dy[sub_direct]

                nx = check_x + dx[direct]
                ny = check_y + dy[direct]

                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        if direct not in graph_wall[check_x][check_y]:
                            if sub_direct not in graph_wall[a][b]:
                                graph_temper[nx][ny] += temp
                                visited[nx][ny] = 1
                                q.append([nx, ny, temp - 1])

def combine_temper():
    new_graph_temper = copy.deepcopy(graph_temper)
    for i in range(n):
        for j in range(n):
            now_temp = graph_temper[i][j]
            for d in range(2,6):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0<=nx<n and 0<=ny<n:
                    if d not in graph_wall[i][j]:
                        other_temp = graph_temper[nx][ny]
                        gap = abs(now_temp - other_temp) // 4
                        if now_temp > other_temp:
                            new_graph_temper[i][j] -= gap
                        elif now_temp < other_temp:
                            new_graph_temper[i][j] += gap
    return new_graph_temper

def down_temper():
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                if graph_temper[i][j] != 0:
                    graph_temper[i][j] -= 1

n,m,k = map(int,sys.stdin.readline().rstrip().split())
machine_pos = []
graph = []
graph_temper = [[0 for _ in range(n)] for _ in range(n)]
graph_wall = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(temp)
    for j in range(n):
        if graph[i][j] >= 2:
            machine_pos.append([i,j])

for _ in range(m):
    x,y,s = map(int,sys.stdin.readline().rstrip().split())
    x,y = x-1,y-1
    if s == 0:
        graph_wall[x][y].append(3)
        graph_wall[x-1][y].append(5)
    elif s == 1:
        graph_wall[x][y].append(2)
        graph_wall[x][y-1].append(4)

# 2 좌 3 위 4 오 5 아래
dx = [-2,-2,0,-1,0,1]
dy = [-2,-2,-1,0,1,0]
dict_check_direct = {2:[3,5],3:[2,4],4:[3,5],5:[2,4]}

result = 0
while 1:
    stop_flag = check_office()
    if result == 101:
        result = - 1
        break
    if stop_flag == 1:
        break
    # 에어컨 바람 불기
    for x,y in machine_pos:
        direct = graph[x][y]
        blow_air(x,y,direct)
    # 공기 섞이기
    graph_temper = combine_temper()
    # 벽 온도 ㄱ마소
    down_temper()
    result += 1

print(result)



