import sys
from collections import deque

def find_group_bfs(x,y,num):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    graph_group[x][y] = num
    dict_group_count[num] = 1
    color = graph_color[x][y]
    dict_group_color[num] = color
    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph_color[nx][ny] == color:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        graph_group[nx][ny] = num
                        dict_group_count[num] += 1

def find_near_group_bfs(x,y,now_group):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph_group[nx][ny] == now_group:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                    # 다른 색이 등장하는 경우
                    else:
                        other_group = graph_group[nx][ny]
                        dict_near_count[now_group][other_group] += 1

def rotation_left_cross(i,j,new_graph_color):
    new_graph_color[n-1-j][i] = graph_color[i][j]

def rotation_right(x,y,block_size,new_graph_color):
    for i in range(block_size):
        for j in range(block_size):
            new_graph_color[x+j][y+block_size-1-i] = graph_color[x+i][y+j]


n = int(sys.stdin.readline().rstrip())
graph_color = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

dict_group_count = {}
dict_near_count = {}
dict_group_color = {}

total_score = 0
for turn in range(4):
    graph_group = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    # 그룹 지정 해주기
    group_num = 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                find_group_bfs(i,j,group_num)
                group_num += 1

    # 총 그룹 개수 만큼 / dict_near_count 묶음 만들어 주기
    for g_num in range(1, group_num):
        dict_near_count[g_num] = {}
        for near_g_num in range(1, group_num):
            if g_num != near_g_num:
                dict_near_count[g_num][near_g_num] = 0

    # 각 그룹 별로 bfs 진행 하면서 / near에 있는 개수 측정
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    group_num = 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                find_near_group_bfs(i,j,group_num)
                group_num += 1
    # near 개수 기반 점수 측정
    score = 0
    for now_g in range(1, group_num):
        for other_g in range(1, group_num):
            if now_g != other_g:
                now_g_count = dict_group_count[now_g]
                other_g_count = dict_group_count[other_g]
                color_now = dict_group_color[now_g]
                color_other = dict_group_color[other_g]
                line_count = dict_near_count[now_g][other_g]
                score += ((now_g_count+other_g_count)*color_now*color_other*line_count)
    total_score += score
    if turn == 4:
        break

    block_size = n//2
    new_graph_color = [[0 for _ in range(n)] for _ in range(n)]
    # 십자는 왼쪽 90
    for i in range(n):
        for j in range(n):
            if i == block_size or j == block_size:
                rotation_left_cross(i,j,new_graph_color)

    # 나머지 블럭은 오른 쪽으로 회전
    for i in [0,block_size+1]:
        for j in [0,block_size+1]:
            rotation_right(i,j,block_size,new_graph_color)
    graph_color = new_graph_color

print(total_score)