import sys
from collections import deque

def bfs(x,y):
    candi_group, red_point = [],[]
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    candi_group.append([x,y])
    now_color = graph[x][y]
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] != -1:
                        # 빨간 돌
                        if graph[nx][ny] == 0 and [nx,ny] not in red_point:
                            q.append([nx,ny])
                            candi_group.append([nx,ny])
                            red_point.append([nx,ny])
                        # 다른 돌
                        elif graph[nx][ny] == now_color:
                            q.append([nx,ny])
                            candi_group.append([nx,ny])
                            visited[nx][ny] = 1
    return candi_group, red_point


def find_center(bomb, red):
    bomb.sort(key = lambda x: (-x[0], x[1]))
    center_x, center_y = 0,0
    for b in bomb:
        if b not in red:
            center_x, center_y = b
            break
    return center_x, center_y

def find_bomb_group():
    max_len = -1
    bomb_group = []
    red_group = []
    none_bomb = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                if graph[i][j] != -1 and graph[i][j] != -2:
                    if graph[i][j] != 0 :
                        candi_group , red_point = bfs(i,j)
                        # 혼자 있는게 아니라면
                        if len(candi_group) >= 2:
                            none_bomb = 1
                            # 빨간색만 있는게 아니라면
                            if candi_group != red_point:
                                # 새로운 더 큰 그룹 발견
                                if len(candi_group) > max_len:
                                    # 새롭게 시작
                                    max_len = len(candi_group)
                                    bomb_group = candi_group
                                    red_group = red_point
                                # 기존과 길이가 같다면
                                elif len(candi_group) == max_len:
                                    # 새로운게, red가 더 적다면
                                    if len(red_group) > len(red_point):
                                        max_len = len(candi_group)
                                        bomb_group = candi_group
                                        red_group = red_point
                                    # 같다면
                                    elif len(red_group) == len(red_point):
                                        ori_center_x,ori_center_y = find_center(bomb_group, red_group)
                                        new_center_x, new_center_y = find_center(candi_group, red_point)
                                        # 새로운 것의 행이 더 크면
                                        if ori_center_x < new_center_x:
                                            max_len = len(candi_group)
                                            bomb_group = candi_group
                                            red_group = red_point
                                        elif ori_center_x == new_center_x:
                                            if ori_center_y > new_center_y:
                                                max_len = len(candi_group)
                                                bomb_group = candi_group
                                                red_group = red_point
    if none_bomb == 0:
        return []
    else:
        return bomb_group

def del_bomb():
    for x,y in bomb_group:
        graph[x][y] = -2

def gravity():
    for i in range(n-1, 0, -1):
        for j in range(n-1,-1,-1):
            # 지금 칸이 빈칸
            if graph[i][j] == -2:
                # 위에 다른 폭탄이 있어 (돌이 아님, 빈공간 아님) (바로 위에 부터, 맨 위까지 조사 시작)
                x,y = i,j
                while 1:
                    x  = x - 1
                    if x == -1 or graph[x][y] == -1:
                        break

                        # 다른 돌 찾으면
                    if graph[x][y] != -1 and graph[x][y] != -2:
                        graph[i][j], graph[x][y] = graph[x][y], graph[i][j]
                        break

def rotation_left():
    new_graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[n-1-j][i] = graph[i][j]
    return new_graph

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]


total_score = 0
while 1:
    # 폭탄 묶음 찾기
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    bomb_group = find_bomb_group()
    if len(bomb_group) == 0:
        break
    # 폭탄 묶음 제거
    total_score += (len(bomb_group)*len(bomb_group))
    del_bomb()
    # 중력 작용
    gravity()
    # 판 회전
    graph = rotation_left()
    # 중력 작용
    gravity()

print(total_score)
"""
-1 검은돌
0 빨간색 폭탄
1 ~ m 다른 폭탄

4 3
1 2 2 -1
1 1 -1 -1
0 -1 2 2
3 3 3 2

"""