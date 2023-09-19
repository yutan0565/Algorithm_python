import sys
from collections import deque

def bfs(visited,x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    total_cnt = 1
    red_cnt = 0
    center_x = 0
    center_y = 0
    member_list = [[x,y]]
    red_list = []

    now_color = graph[x][y]
    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    # 빨간색인 경우
                    if graph[nx][ny] == 0:
                        red_list.append([nx,ny])
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        total_cnt += 1
                        red_cnt += 1
                    # 같은 색
                    elif graph[nx][ny] == now_color:
                        visited[nx][ny] = 1
                        q.append([nx,ny])
                        total_cnt += 1
                        member_list.append([nx,ny])

    # 빨간색 visited 복귀
    for a,b in red_list:
        visited[a][b] = -1

    # center 점 찾기
    member_list.sort(key = lambda  x : (-x[0], x[1]))
    center_x = member_list[0][0]
    center_y = member_list[0][1]
    member_list = member_list + red_list

    return [total_cnt, red_cnt, center_x, center_y, member_list]

def find_candi_group():
    candi_group_list = []
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                # 돌 또는 빨간색이 아닌 경우임
                if graph[i][j] >= 1:
                    # 총개수 많, 빨 적, 기준행 큰, 기준열 작은, 멤버 위치
                    new_group = bfs(visited,i,j)
                    # 2개 이상의 멤버가 존재해야함
                    if new_group[0] >= 2:
                        candi_group_list.append(new_group)
    return candi_group_list

def choose_one(candi_group_list):
    candi_group_list.sort(key = lambda x : (-x[0],x[1],-x[2],x[3]) )
    return candi_group_list[0]

def del_group_bomb(del_group):
    global graph, total_score
    del_list = del_group[4]
    for a,b in del_list:
        graph[a][b] = -3
    total_score += (len(del_list)*len(del_list))

def gravity():
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            # 현재 자리가 빈공간인 경우
            if graph[i][j] == -3:
                # 바로 위에 부터 돌 찾기
                x,y = i,j
                while 1:
                    x -= 1
                    # 범위 벗어나면 그만
                    if(not(0<=x<n and 0<=y<n)):
                        break
                    # 검은 돌이 있는 경우
                    if graph[x][y] == -1:
                        # 이전 칸이랑, 바꾸기
                        x += 1
                        graph[i][j], graph[x][y] = graph[x][y], graph[i][j]
                        break
                    # 다른 돌이 있는 경우
                    if graph[x][y] >= 0:
                        graph[i][j], graph[x][y] = graph[x][y], graph[i][j]
                        break
            # 다른 돌이 있는 겨우, 검은돌이 있는 경우
            else:
                continue

def rotate_left():
    global  graph
    new_graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[n-1-j][i] = graph[i][j]
    graph = new_graph

def simulation():
    while 1:
        # 폭탄 묶음 찾기
        candi_group_list = find_candi_group()
        # 후보가 없으면 그만두기
        if len(candi_group_list) == 0:
            return
        # 그중에 하나 선택
        del_group = choose_one(candi_group_list)
        # 선택한거 폭발 ( 점수 획득 )
        del_group_bomb(del_group)

        # 중력 작용
        gravity()

        # 왼쪽으로 회전
        rotate_left()

        # 중력 작용
        gravity()



n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
total_score = 0
simulation()
print(total_score)


# 6 2
# 0 -1 2 2 1 1
# 0 0 2 2 1 1
# -1 1 1 1 1 1
# 0 0 0 0 2 2
# 1 2 -1 1 -1 1
# 2 1 -1 0 2 0