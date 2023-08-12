import copy
import sys
from collections import deque
from collections import defaultdict

def bfs(x,y,number, visited):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    group_graph[x][y] = number
    now_num = color_graph[x][y]
    count = 1
    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if color_graph[nx][ny] == now_num:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        group_graph[nx][ny] = number
                        count += 1
    return count

def make_group():
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    number = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                number += 1
                count = bfs(i,j, number , visited)
                dict_group_coler[number] = color_graph[i][j]
                dict_group_count[number] = count
    for num in range(1, number + 1):
        dict_neightbor_count[num] = [0 for _ in range(number + 1)]
    return group_graph

def find_neigbor(x,y,visited):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    now_group = group_graph[x][y]
    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    # 가는 곳이 다른 그룹 이라면
                    if group_graph[nx][ny] != now_group:
                        other_group = group_graph[nx][ny]
                        dict_neightbor_count[now_group][other_group] += 1
                        dict_neightbor_count[other_group][now_group] += 1

                    # 같은 그룹이라면
                    elif group_graph[nx][ny] == now_group:
                        q.append([nx,ny])
                        visited[nx][ny] = 1

def cal_score():
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                find_neigbor(i,j, visited)

    # 이웃 / 그룹 정보 토대로 점수 계산 시작
    temp_score = 0
    for now in dict_group_count.keys():
        for to in dict_group_count.keys():
            #자기 자신이면 패스
            if now == to:
                continue
            # now - to 접점이 없으면 패스
            elif dict_neightbor_count[now][to] == 0:
                continue
            # 접점이 있따면
            else:
                now_count = dict_group_count[now]
                to_count = dict_group_count[to]
                now_color = dict_group_coler[now]
                to_color = dict_group_coler[to]
                now_to_count = dict_neightbor_count[now][to]

                add_socre = (now_count +to_count)*now_color*to_color*now_to_count
                temp_score += add_socre
    return temp_score // 2

def rotation_right(x,y, block_size, new_color_graph):
    for i in range(block_size):
        for j in range(block_size):
            new_color_graph[x+j][y+block_size-1-i] = color_graph[x+i][y+j]
    return new_color_graph

def rotation_block():
    block_size = n // 2
    new_color_graph = copy.deepcopy(color_graph)
    for x in [0, block_size + 1]:
        for y in [0, block_size + 1]:
            new_color_graph = rotation_right(x,y, block_size, new_color_graph)
    return new_color_graph

def  rotation_cross():
    new_color_graph = copy.deepcopy(color_graph)
    for x in range(n):
        for y in range(n):
            if x == center_x or y == center_y:
                new_color_graph[n-1-y][x]  = color_graph[x][y]
    return new_color_graph

n  =int(sys.stdin.readline().rstrip())
center_x,center_y = n//2, n//2
color_graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
group_graph = [[0 for _ in range(n)] for _ in range(n)]


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def show_info(round, score):
    print("round ; ", round)
    print("점수 :", score)
    print("색")
    for g in color_graph:
        print(g)
    print("그룹")
    for g in group_graph:
        print(g)
    print("dict 정보")
    print(dict_group_count)
    print(dict_neightbor_count)
    print(dict_group_coler)
    print("-----------------")


total_score = 0
for round in range(1, 5):
    dict_group_count = defaultdict(lambda: -1)
    dict_neightbor_count = defaultdict(lambda: [])
    dict_group_coler = defaultdict(lambda: -1)
    # 그룹 만들기
    group_graph = make_group()
    # 점수 계산
    score = cal_score()
    total_score += score
    if round == 4:
        break
    # 외부 회전
    color_graph = rotation_block()
    # 십자 회전
    color_graph = rotation_cross()

    # show_info(round, score)
print(total_score)
