"""
1. 각 칸마다 블럭 있음 ( 검정(-1)_, 무지개(0), 일반( = M개의 색상, 1~M))
2. 블록 그룹 = 인접한 블록 ( 2개 이상)
3. 그룹의 기준 = 무지개 블록이 아닌거 중에, 행/열 번호가 가장 작은 것
4. 빈공간  = -3
"""
from collections import deque
import sys
import copy


def rotation():
    global graph
    temp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            graph[n-j-1][i] = temp_graph[i][j]

def gravity():
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            for k in range(0, n-1-i):
                if graph[i+k+1][j] == -3 and graph[i+k][j] != -1  and i+k+1 < n:
                    temp = graph[i+k][j]
                    graph[i+k+1][j] = temp
                    graph[i+k][j] = -3

def bfs_find_group(x,y):
    q = deque()
    q.append([x,y])
    group_color = graph[x][y]
    group_mask = [[0 for _ in range(n)] for _ in range(n)]
    group_mask[x][y] = 1

    visited = copy.deepcopy(reset_visited)
    visited[x][y] = 1
    count = 1
    rainbow_count =0
    center_point = []
    if graph[x][y] == 0:
        rainbow_count += 1
    else:
        center_point.append([x, y])
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == 0:
                        q.append([nx,ny])
                        visited[nx][ny] = visited[a][b] + 1
                        group_mask[nx][ny] = 1
                        count += 1
                        rainbow_count += 1
                    elif graph[nx][ny] == group_color:
                        q.append([nx,ny])
                        visited[nx][ny] = visited[a][b] + 1
                        group_mask[nx][ny] = 1
                        center_point.append([nx,ny])
                        count += 1

    if count - rainbow_count == 0 :
        return count, group_mask, [-20, -20], rainbow_count
    else:
        center_point.sort(key = lambda x:(x[0], x[1]))
        cen_point = center_point[0]
        return count, group_mask,cen_point, rainbow_count

def find_group():
    global result_score
    temp_big_group = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != -3 and graph[i][j] != -1:
                group_size, mask, cen_block, count_rain = bfs_find_group(i,j)
                if group_size >= 2 and group_size - count_rain != 0:
                    temp_big_group.append([-group_size, mask, [-cen_block[0], -cen_block[1]], -count_rain])
    if len(temp_big_group) != 0:
        temp_big_group.sort(key=lambda x: (x[0],x[3], x[2][0], x[2][1]))
        temp_result_mask  = temp_big_group[0][1]
        score = 0
        for i in range(n):
            for j in range(n):
                if temp_result_mask[i][j] == 1:
                    score += 1
                    graph[i][j] = -3
        result_score += (score**2)
        return 1
    else :
        return -1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

result_score = 0
n,m = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
reset_visited = [ [-1 for _ in range(n)] for _ in range(n)]

cont_flag = 0

time = 0
while 1:
    cont_flag = find_group()
    if cont_flag == -1:
            break
    gravity()
    rotation()
    gravity()

print(result_score)

"""
2 2
0 0
0 0
"""