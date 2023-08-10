import copy
import sys
from collections import deque

def move_theif(x,y,dict_direct, dict_pos, graph):
    dict_pos[graph[x][y]] = [-1, -1]
    dict_direct[graph[x][y]] = -1
    graph[x][y] = 0

    for num in range(1, 17):
        a,b = dict_pos[num]
        if [a,b] == [-1,-1]:
            continue
        now_direct = dict_direct[num]
        for plus in range(8):
            new_direct = (now_direct + plus)%8
            nx = a + dx[new_direct]
            ny = b + dy[new_direct]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if [nx,ny] != [x,y]:
                    other_num = graph[nx][ny]
                    if other_num ==0:
                        graph[a][b], graph[nx][ny] = graph[nx][ny], graph[a][b]
                        dict_pos[num] = [nx,ny]
                        dict_direct[num] = new_direct
                    else:
                        graph[a][b], graph[nx][ny] = graph[nx][ny], graph[a][b]
                        dict_pos[num],dict_pos[other_num] = dict_pos[other_num], dict_pos[num]
                        dict_direct[num] = new_direct
                    break
    return dict_direct, dict_pos, graph

def show_graph(graph):
    print("=========")
    for g in graph:
        print(g)

def bfs():
    global max_score
    # 초기 시작
    q = deque()
    max_score = start_graph[start_x][start_y]
    start_direct = start_dict_direct[start_graph[start_x][start_y]]

    # 도둑말 움직임
    new_dict_direct, new_dict_pos, new_graph = move_theif(start_x, start_y, start_dict_direct, start_dict_pos, start_graph)
    q.append([start_x,start_y, max_score, start_direct,new_dict_direct, new_dict_pos, new_graph])

    while q:
        a,b,now_score, now_direct,now_dict_direct, now_dict_pos, now_graph = q.popleft()
        max_score = max(max_score, now_score)
        for mul in range(1, 4):
            nx = a + dx[now_direct]*mul
            ny = b + dy[now_direct]*mul
            if 0<=nx<4 and 0<=ny<4:
                if now_graph[nx][ny] != 0:
                    new_score = now_score + now_graph[nx][ny]
                    new_direct = now_dict_direct[now_graph[nx][ny]]

                    new_dict_direct = copy.deepcopy(now_dict_direct)
                    new_dict_pos = copy.deepcopy(now_dict_pos)
                    new_graph  = copy.deepcopy(now_graph)

                    new_dict_direct, new_dict_pos, new_graph = move_theif(nx,ny,new_dict_direct, new_dict_pos, new_graph)
                    q.append([nx,ny, new_score, new_direct, new_dict_direct,new_dict_pos,new_graph])

start_graph = [[0 for _ in range(4)] for _ in range(4)]
start_dict_direct = {}
start_dict_pos = {}


start_x,start_y = 0,0

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

for i in range(4):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(4):
        number = temp[j*2]
        direct = temp[j*2+1]
        start_dict_direct[number] = direct-1
        start_dict_pos[number] = [i,j]
        start_graph[i][j] = number
max_score = -1
bfs()
print(max_score)