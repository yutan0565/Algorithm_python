import copy
import sys
from collections import deque

def check_temper():
    for i in range(n):
        for j in range(n):
            if graph_pos[i][j] == 1:
                if graph_temper[i][j] < k:
                    return False
    return True

def blow_air(now_direct, x, y):
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    blow_direct = blow_direct_dict[now_direct]
    x = x + dx[now_direct]
    y = y + dy[now_direct]
    graph_temper[x][y] += 5

    q = deque()
    q.append([x,y,4])
    visited[x][y] = 1

    while q:
        a,b, now_temp = q.popleft()
        if now_temp == 0:
            break
        for d in range(3):
            if d == 0:
                nx = a + dx[blow_direct[d]]
                ny = b + dy[blow_direct[d]]
            # 직전 방향이 아닌 경우 - 자기 방향으로 한칸이동
            if d != 0:
                check_x = a + dx[blow_direct[d]]
                check_y = b + dy[blow_direct[d]]
                nx = check_x + dx[now_direct]
                ny = check_y + dy[now_direct]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    # 직선으로 부는 바람
                    if d == 0:
                        # 벽이 없다면 바람 불기
                        if now_direct not in graph_wall[a][b]:
                            visited[nx][ny] = 1
                            graph_temper[nx][ny] += now_temp
                            q.append([nx,ny,now_temp-1])
                    # 위 or 좌
                    elif d == 1:
                        # 위 확인하는 경우
                        if now_direct == 0 or now_direct == 2:
                            # check 기준  now_direct와, 아래에 벽이 없음
                            if now_direct not in graph_wall[check_x][check_y]:
                                if 3 not in graph_wall[check_x][check_y]:
                                    visited[nx][ny] = 1
                                    graph_temper[nx][ny] += now_temp
                                    q.append([nx, ny, now_temp - 1])
                        # 좌측 확인하는 경우
                        else:
                            if now_direct not in graph_wall[check_x][check_y]:
                                if 2 not in graph_wall[check_x][check_y]:
                                    visited[nx][ny] = 1
                                    graph_temper[nx][ny] += now_temp
                                    q.append([nx, ny, now_temp - 1])
                    # 아 or 우
                    elif d == 2:
                        # 아래 확인하는 경우
                        if now_direct == 0 or now_direct == 2:
                            if now_direct not in graph_wall[check_x][check_y]:
                                if 1 not in graph_wall[check_x][check_y]:
                                    visited[nx][ny] = 1
                                    graph_temper[nx][ny] += now_temp
                                    q.append([nx, ny, now_temp - 1])
                        # 오른쪽 확인하는 경우
                        else:
                            if now_direct not in graph_wall[check_x][check_y]:
                                if 0 not in graph_wall[check_x][check_y]:
                                    visited[nx][ny] = 1
                                    graph_temper[nx][ny] += now_temp
                                    q.append([nx, ny, now_temp - 1])

def mix_air():
    global graph_temper
    # 높은곳에서 낮은곳으로만 이동
    new_graph_temper = copy.deepcopy(graph_temper)
    for i in range(n):
        for j in range(n):
            center_temp = graph_temper[i][j]
            for d in range(4):
                # 해당 방향으로 벽이 없음
                if d not in graph_wall[i][j]:
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        other_temp = graph_temper[nx][ny]
                        gap_add = (center_temp - other_temp) // 4
                        # 내가 더 높으면
                        if center_temp > other_temp:
                            new_graph_temper[i][j] -= gap_add
                            new_graph_temper[nx][ny] += gap_add
    graph_temper = new_graph_temper

def down_temper():
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i == n-1 or j == n-1:
                if graph_temper[i][j] != 0:
                    graph_temper[i][j] -= 1

def simulation():
    result = 0
    while 1:
        result += 1
        if result == 101:
            return -1
        # 바람이 나옴 / 온도 올리기
        for now_direct, x,y in air_pos:
            blow_air(now_direct, x, y)

        # 공기 섞이기
        mix_air()

        # 외벽 온도 감사
        down_temper()

        if check_temper():
            return result

n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph_pos = [list(map(int,sys.stdin.readline().rstrip().split())) for  _ in range(n)]
graph_temper = [[0 for _ in range(n)] for _ in range(n)]
graph_wall = [[[] for _ in range(n)] for _ in range(n)]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

blow_direct_dict = {    0 : [0, 1,3],
                        1 : [1, 0,2],
                        2 : [2,1,3],
                        3 : [3,0,2]
            }

# 에어컨  0 왼, 1 위, 2 오른, 3 아래
air_pos = []
for i in range(n):
    for j in range(n):
        if graph_pos[i][j] >= 2:
            # 방향, x,y
            air_pos.append([graph_pos[i][j]-2, i,j])
            graph_pos[i][j] = 0

# 벽 등록
for _ in range(m):
    x,y,s = map(int,sys.stdin.readline().rstrip().split())
    x -= 1
    y -= 1
    # 위에 벽
    if s == 0:
        graph_wall[x][y].append(1)
        graph_wall[x-1][y].append(3)
    # 왼쪽 벽
    elif s == 1:
        graph_wall[x][y].append(0)
        graph_wall[x][y-1].append(2)

result = simulation()
print(result)