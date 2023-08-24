import copy
import sys
from collections import deque

def move_theif(horse_x,horse_y,graph, dict_direct, dict_pos, dict_live):
    new_graph = copy.deepcopy(graph)
    new_dict_direct = copy.deepcopy(dict_direct)
    new_dict_pos = copy.deepcopy(dict_pos)

    new_graph[horse_x][horse_y] = 0
    for num in range(1,17):
        if dict_live[num] == 1:
            x,y = new_dict_pos[num]
            now_direct = new_dict_direct[num]
            for plus in range(8):
                new_direct = (now_direct + plus)%8
                nx = x + dx[new_direct]
                ny = y + dy[new_direct]
                if 0<=nx<4 and 0<=ny<4:
                    if [nx,ny] != [horse_x,horse_y]:
                        # 이동하는 곳이 빈곳
                        if new_graph[nx][ny] == 0:
                            new_dict_pos[num] = [nx,ny]
                            new_dict_direct[num] = new_direct
                            new_graph[x][y],new_graph[nx][ny] = new_graph[nx][ny],new_graph[x][y]
                            break
                        else:
                            other_num = new_graph[nx][ny]
                            new_dict_pos[num],new_dict_pos[other_num] = new_dict_pos[other_num], new_dict_pos[num]
                            new_dict_direct[num] = new_direct
                            new_graph[x][y], new_graph[nx][ny] = new_graph[nx][ny], new_graph[x][y]
                            break
    return new_graph, new_dict_direct,new_dict_pos


def bfs():
    global start_graph, start_dict_direct, start_dict_pos, start_dict_live
    q = deque()
    start_num = start_graph[0][0]
    start_horse_direct = start_dict_direct[start_num]
    max_score = start_num
    start_dict_live[start_num] = 0
    # 첫 도둑 움직임
    start_graph, start_dict_direct,start_dict_pos = move_theif(0,0,start_graph, start_dict_direct, start_dict_pos, start_dict_live)
    q.append([0,0,start_horse_direct,start_graph,start_dict_pos,start_dict_direct,start_dict_live, max_score])

    while q:
        a,b,now_horse_direct,now_graph,now_dict_pos,now_dict_direct,now_dict_live,score = q.popleft()

        max_score = max(score, max_score)
        for mul in range(1,4):
            nx = a + dx[now_horse_direct]*mul
            ny = b + dy[now_horse_direct]*mul
            if 0<=nx<4 and 0<=ny<4:
                if now_graph[nx][ny] != 0:
                    other_num = now_graph[nx][ny]
                    new_horse_direct = now_dict_direct[other_num]
                    new_score = score + other_num
                    new_dict_live = copy.deepcopy(now_dict_live)
                    new_dict_live[other_num] = 0
                    new_graph, new_dict_direct,new_dict_pos = move_theif(nx,ny,now_graph, now_dict_direct, now_dict_pos, new_dict_live)
                    q.append([nx, ny, new_horse_direct, new_graph, new_dict_pos, new_dict_direct, new_dict_live,new_score])
    return max_score

start_graph = [[0 for _ in range(4)] for _ in range(4)]
start_dict_direct = {}
start_dict_pos = {}
start_dict_live = {}
for i in range(4):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(0,8,2):
        start_graph[i][j//2] = temp[j]
        start_dict_pos[temp[j]] = [i,j//2]
        start_dict_direct[temp[j]] = temp[j+1]-1
        start_dict_live[temp[j]] = 1


dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

result = bfs()
print(result)