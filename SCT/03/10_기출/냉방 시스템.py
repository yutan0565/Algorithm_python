import copy
import sys
from collections import deque

def check_temp_office():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                if temper[i][j] < k:
                    return 0
    return 1

def blow_air(x,y,direct):
    q = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    # 다음칸은 무조건 가능
    nx = x + dx[direct]
    ny = y + dy[direct]

    temper[nx][ny] += 5
    visited[nx][ny] = 1
    q.append([nx,ny,4])

    while q:
        a,b,temp = q.popleft()
        if temp == 0:
            continue
        for i in range(3):
            # 직선
            if i == 0:
                nx = a + dx[direct]
                ny = b + dy[direct]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        if direct not in wall[a][b]:
                            temper[nx][ny] += temp
                            q.append([nx,ny,temp-1])
                            visited[nx][ny] = 1
            else :
                if i == 1:
                    check_d =  dict_direct_sub[direct][0]
                elif i == 2:
                    check_d = dict_direct_sub[direct][1]
                check_x = a + dx[check_d]
                check_y = b + dy[check_d]
                nx = check_x + dx[direct]
                ny = check_y + dy[direct]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        if direct not in wall[check_x][check_y]:
                            if check_d not in wall[a][b]:
                                temper[nx][ny] += temp
                                q.append([nx, ny, temp - 1])
                                visited[nx][ny] = 1

def mix_temper():
    new_temper = copy.deepcopy(temper)
    for i in range(n):
        for j in range(n):
            now_temp = temper[i][j]
            for d in range(2, 6):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0<=nx<n and 0<=ny<n:
                    if d not in wall[i][j]:
                        other_temp = temper[nx][ny]
                        gap = abs(now_temp - other_temp) //4
                        if now_temp > other_temp:
                            new_temper[i][j] -= gap
                        elif now_temp < other_temp:
                            new_temper[i][j] += gap
    return new_temper

def down_temper():
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                if temper[i][j] != 0:
                    temper[i][j] -= 1

n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph = []
air_start = []
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if graph[i][j] >= 2:
            air_start.append([i,j])


temper = [[0 for _ in range(n)] for _ in range(n)]
wall = [[[] for _ in range(n)] for _ in range(n)]

# 2 왼쪽 / 3 위 / 4 오른쪽 / 5 아래
dx = [0,0,0,-1,0,1]
dy = [0,0,-1,0,1,0]

dict_direct_sub = {}
dict_direct_sub[2] = [3,5]
dict_direct_sub[3] = [2,4]
dict_direct_sub[4] = [3,5]
dict_direct_sub[5] = [2,4]

# 벽 만들기
for _ in range(m):
    x,y,s = map(int,sys.stdin.readline().rstrip().split())
    x,y = x-1, y-1
    # s == 0  바로 위
    if s == 0:
        wall[x][y].append(3)
        wall[x-1][y].append(5)
    elif s == 1:
        wall[x][y].append(2)
        wall[x][y-1].append(4)

result = 0
while 1:
    end_flag = check_temp_office()
    if end_flag == 1:
        break
    if result == 101:
        result = -1
        break
    # 에어컨에서 바람 불기
    for x,y in air_start:
        direct = graph[x][y]
        blow_air(x,y,direct)

    # 온도가 섞임
    temper = mix_temper()

    # 외벽 감소
    down_temper()

    result += 1

print(result)