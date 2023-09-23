import copy
import sys
from collections import deque



def bfs(x,y,group_num):
    global graph_group
    q = deque()
    q.append([x,y])
    now_color = graph[x][y]
    graph_group[x][y] = group_num

    while q:
        a,b= q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if graph_group[nx][ny] == -1:
                    if graph[nx][ny]== now_color:
                        q.append([nx,ny])
                        graph_group[nx][ny] = group_num

def make_group():
    group_num = -1
    for i in range(n):
        for j in range(n):
            if graph_group[i][j] == -1:
                group_num += 1
                bfs(i,j, group_num)
    return group_num+1

def bfs_art(x,y,count_dict,near_count_dict,visited,num_dict):
    global graph_group
    q = deque()
    q.append([x,y])
    now_group = graph_group[x][y]
    num_dict[now_group] = graph[x][y]
    visited[x][y] = 1
    count_dict[now_group] += 1
    while q:
        a,b= q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    # 같은 그룹 내
                    if graph_group[nx][ny] == now_group:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        count_dict[now_group] += 1
                    # 다른 그룹인 경우
                    else:
                        other_group = graph_group[nx][ny]
                        near_count_dict[now_group][other_group] += 1
    return count_dict,near_count_dict,visited,num_dict

def cal_art(num_group):
    global total_score
    count_dict = {}
    near_count_dict = {}
    num_dict = {}
    for num in range(num_group):
        count_dict[num] = 0
        near_count_dict[num] = [0 for _ in range(num_group)]

    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                count_dict,near_count_dict,visited,num_dict = bfs_art(i,j,count_dict,near_count_dict,visited,num_dict)

    for now_g in range(num_group):
        for other_g in range(num_group):
            if now_g != other_g:
                a_count = count_dict[now_g]
                b_count = count_dict[other_g]
                a_num = num_dict[now_g]
                b_num = num_dict[other_g]
                near_count = near_count_dict[now_g][other_g]
                total_score += ((a_count+b_count)*a_num*b_num*near_count)

def rotate_left_cross():
    global graph
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if i == n//2 or j == n//2:
                new_graph[n-1-j][i] = graph[i][j]
    graph = new_graph

def rotate_right(x,y,block_size):
    global graph
    new_graph = copy.deepcopy(graph)
    for i in range(block_size):
        for j in range(block_size):
            new_graph[x+j][y+block_size-1-i] = graph[x+i][y+j]
    graph = new_graph

n = int(sys.stdin.readline().rstrip())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

total_score = 0

for round in range(0,4):
    # 그룹 만들어 주기
    graph_group = [[-1 for _ in range(n)] for _ in range(n)]
    num_group = make_group()
    # 예술성 계산
    cal_art(num_group)
    if round == 3:
        break
    # 십자 모양 왼쪽
    rotate_left_cross()
    #블럭 모양 - 개별 오른
    block_size = n//2
    for i in [0,block_size+1]:
        for j in [0, block_size + 1]:
            rotate_right(i,j,block_size)
print(total_score)