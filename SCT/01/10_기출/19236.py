import copy
from collections import deque
import sys

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def moving_fish(shark_x, shark_y, graph_f, dict_f):
    for fish_number in range(1, 17):
        if not(dict_f.get(fish_number)):
            continue

        x = dict_f[fish_number][0]
        y = dict_f[fish_number][1]
        direct = graph_f[x][y][1]

        for i in range(8):
            n_direct = (direct+i)%8
            nx = x + dx[n_direct]
            ny = y + dy[n_direct]
            if 0<=nx<4 and 0<=ny<4:
                if not(nx == shark_x and ny == shark_y):
                    # 바뀐 방향 업데이트
                    graph_f[x][y][1] = n_direct
                    #새로운 곳과 위치 전환
                    new_pos_fish = graph_f[nx][ny][0]
                    graph_f[x][y], graph_f[nx][ny] = graph_f[nx][ny], graph_f[x][y]
                    if new_pos_fish != -1:
                        dict_f[fish_number], dict_f[new_pos_fish] = dict_f[new_pos_fish], dict_f[fish_number]
                    else:
                        dict_f[fish_number] = [nx,ny]
                    break
    return graph_f

def moving_shark():
    q = deque()
    eating_fish = graph[0][0][0]
    shark_direct = graph[0][0][1]
    del dict_fish_pos[graph[0][0][0]]
    graph[0][0] = [-1, -1]
    q.append([0, 0, eating_fish,shark_direct, graph, dict_fish_pos])

    max_eat = eating_fish
    while q:
        a,b,eat,direct,temp_graph, dict_fish= q.popleft()
        if eat >max_eat:
            max_eat = eat
        temp_graph = moving_fish(a,b,temp_graph, dict_fish)
        for i in range(1, 5):
            nx = a + dx[direct]*i
            ny = b + dy[direct]*i
            if 0<=nx<4 and 0<=ny<4:
                if temp_graph[nx][ny][0] != -1:
                    new_eat = eat+temp_graph[nx][ny][0]
                    new_direct = temp_graph[nx][ny][1]
                    new_graph = copy.deepcopy(temp_graph)
                    new_dict = copy.deepcopy(dict_fish)
                    del new_dict[temp_graph[nx][ny][0]]
                    new_graph[a][b] = [-1, -1]
                    q.append([nx,ny,new_eat,new_direct, new_graph, new_dict])

    return max_eat


# 물고기 번호 / 방향
graph = [[[0,0] for _ in range(4)] for _ in range(4)]
dict_fish_pos = {}
for i in range(4):
    temp = list(map(int ,sys.stdin.readline().rstrip().split()))
    for j in range(0,8,2):
        graph[i][j//2][0] = temp[j]
        graph[i][j//2][1] = temp[j+1]-1
        dict_fish_pos[temp[j]] = [i , j//2]

# 상어가 이동한 곳은 빈칸
result = moving_shark()
print(result)

"""
상어가 집가면 모두 끝
    
    각 물고기
        번호 (1 ~ 16)
        번호는 모두 다름
        상하좌우대각선  방향을 가짐
    
    상어
        0,0 부터 시작
        0,0 의 물고기를 먹음
        
        물고기 이동 시작
            번호가 작은 물고기 부터 이동
            한칸 이동
                방향을 45도 씩 반시계 방향으로 회전
                    빈칸 / 다른 물고기 있는 칸   이동 가능
                    상어 / 범위 밖 은 이동 불가
                    다른 물고기가 있는 칸으로 이동하면, 서로의 위치를 바꾸면서 이동
                    
                이동 가능한 칸 없으면  이동 x
        
        상어 이동 시작
            그 칸에서 먹은 물고기 방향으로 이동
            해당 방향으로 칸을 늘려감
                이동한 칸의 물고기 먹음 (지나가는 칸 물고기는 먹지 않음)
                먹은 물고기의 방향을 가짐
            먹을게 없으면, 집으로 감

"""