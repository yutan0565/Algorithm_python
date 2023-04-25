import sys
from collections import deque

def bfs(x,y,visited):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    bomb_list = [[x,y]]
    red_count = 0
    center_x, center_y = -1,-1
    now_color = graph[x][y]

    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    # 빨간색이면
                    if graph[nx][ny] == 0:
                        if [nx,ny] not in bomb_list:
                            q.append([nx,ny])
                            bomb_list.append([nx,ny])
                            red_count += 1
                    elif graph[nx][ny] == now_color:
                        q.append([nx,ny])
                        bomb_list.append([nx,ny])
                        visited[nx][ny] = 1
    bomb_list.sort(key = lambda x : (-x[0],x[1]))
    for x,y in bomb_list:
        if graph[x][y] != 0:
            center_x = x
            center_y = y
            break
    return  bomb_list, red_count, center_x,center_y

def fine_bomb_group():
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    max_bomb_list = []
    max_bomb_count = -1
    min_red_count = n*n+1
    max_center_x, min_center_y = -1, n + 5
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                # 돌 / 빨  아닌 곳에서만 찾기
                if graph[i][j] >= 1:
                    bomb_list, red_count, center_x,center_y = bfs(i,j,visited)
                    bomb_count = len(bomb_list)
                    if len(bomb_list) < 2:
                        continue
                    if bomb_count > max_bomb_count:
                        max_bomb_list, max_bomb_count, min_red_count, max_center_x,min_center_y = bomb_list, bomb_count, red_count, center_x,center_y
                    elif bomb_count == max_bomb_count:
                        if red_count < min_red_count:
                            max_bomb_list, max_bomb_count, min_red_count, max_center_x, min_center_y = bomb_list, bomb_count, red_count, center_x, center_y
                        elif red_count == min_red_count:
                            if center_x > max_center_x:
                                max_bomb_list, max_bomb_count, min_red_count, max_center_x, min_center_y = bomb_list, bomb_count, red_count, center_x, center_y
                            elif center_x == max_center_x:
                                if center_y < min_center_y:
                                    max_bomb_list, max_bomb_count, min_red_count, max_center_x, min_center_y = bomb_list, bomb_count, red_count, center_x, center_y
    return max_bomb_list

def del_bomb(bomb_list):
    for x,y in bomb_list:
        graph[x][y] = -2

def gravity():
    for row in range(n-1,0,-1):
        for col in range(n):
            if graph[row][col] == -2:
                up = 1
                switch_flag = 0
                x,y = -1,-1
                while 1:
                    nx = row - up
                    ny = col
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] >= 0:
                            switch_flag = 1
                            x,y = nx,ny
                            break
                        elif graph[nx][ny] == -1:
                            break
                        else:
                            up += 1
                    else:
                        break
                if switch_flag == 1:
                    graph[row][col], graph[x][y] = graph[x][y],graph[row][col]

def rotation():
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
    # 폭탄 그룹 찾기 / 제거
    bomb_list = fine_bomb_group()
    if bomb_list == []:
        break
    # 폭탄 제거
    del_bomb(bomb_list)
    # 점수 증가
    total_score += (len(bomb_list)*len(bomb_list))
    # 중력 작용
    gravity()

    # 왼쪽 회전
    graph = rotation()

    # 중력 작용
    gravity()



print(total_score)