import sys
from collections import deque

def bfs(x,y,visited):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    now_color = graph_color[x][y]
    bomb_group, red_count, cen_x, cen_y = [[x,y]],0,0,0

    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph_color[nx][ny] == 0:
                        if [nx,ny] not in bomb_group:
                            q.append([nx, ny])
                            bomb_group.append([nx,ny])
                            red_count += 1
                    elif graph_color[nx][ny] == now_color:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        bomb_group.append([nx,ny])
    bomb_group.sort(key = lambda x : (-x[0],x[1]))
    for x,y in bomb_group:
        if graph_color[x][y] != 0:
            cen_x = x
            cen_y = y
            break
    return bomb_group, red_count, cen_x, cen_y

def find_bomb_group():
    max_bomb_group = []
    max_bomb_count = 0
    max_cen_x, min_cen_y = 0,n+1
    min_red_count = n*n+1
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                if graph_color[i][j] >= 1:
                    bomb_group, red_count, cen_x, cen_y = bfs(i,j,visited)
                    bomb_count = len(bomb_group)
                    if bomb_count >= 2:
                        if bomb_count > max_bomb_count:
                            max_bomb_group = bomb_group
                            max_bomb_count = bomb_count
                            max_cen_x, min_cen_y = cen_x, cen_y
                            min_red_count = red_count
                        elif bomb_count == max_bomb_count:
                            if red_count < min_red_count:
                                max_bomb_group = bomb_group
                                max_bomb_count = bomb_count
                                max_cen_x, min_cen_y = cen_x, cen_y
                                min_red_count = red_count
                            elif red_count == min_red_count:
                                if cen_x > max_cen_x:
                                    max_bomb_group = bomb_group
                                    max_bomb_count = bomb_count
                                    max_cen_x, min_cen_y = cen_x, cen_y
                                    min_red_count = red_count
                                elif cen_x == max_cen_x:
                                    if cen_y < min_cen_y:
                                        max_bomb_group = bomb_group
                                        max_bomb_count = bomb_count
                                        max_cen_x, min_cen_y = cen_x, cen_y
                                        min_red_count = red_count
    return max_bomb_group

def del_bomb_block(bomb_group):
    global total_score
    total_score += (len(bomb_group)*len(bomb_group))
    for x,y in bomb_group:
        graph_color[x][y] = -2

def gravity():
    for i in range(n-1,0,-1):
        for j in range(n):
            if graph_color[i][j] == -2:
                for up in range(1, n):
                    nx = i - up
                    ny = j
                    if not(0<=nx<n and 0<=ny<n):
                        break
                    else:
                        if graph_color[nx][ny] == -2:
                            continue
                        elif graph_color[nx][ny] == -1:
                            break
                        else:
                            graph_color[i][j], graph_color[nx][ny] = graph_color[nx][ny], graph_color[i][j]
                            break

def rotation_left():
    new_graph_color = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph_color[n-1-j][i] = graph_color[i][j]
    return new_graph_color


n,m = map(int,sys.stdin.readline().rstrip().split())
graph_color = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

total_score = 0
while 1:
    # 그룹 만들기
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    bomb_group = find_bomb_group()
    if bomb_group == []:
        break
    # 그룹 지우기
    del_bomb_block(bomb_group)
    # 중력 작용
    gravity()
    # 반시계 방향 회전
    graph_color = rotation_left()
    # 중력 작용
    gravity()

print(total_score)