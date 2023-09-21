import copy
import sys
import copy
from collections import deque

def dfs(graph, pos_dict, direct_dict,x,y, score):
    global max_score
    new_graph = copy.deepcopy(graph)
    new_pos_dict = copy.deepcopy(pos_dict)
    new_direct_dict = copy.deepcopy(direct_dict)
    # 말 위치에 있는 도둑 잡기
    check_num = new_graph[x][y][0]
    score += new_graph[x][y][0]
    horse_direct = new_graph[x][y][1]
    new_graph[x][y] = [-1,-1]
    new_pos_dict[check_num] = [-1,-1]
    new_direct_dict[check_num] = -1
    max_score = max(score, max_score)

    # 번호가 작은 순서대로 본인 방향으로 이동
    for num in range(1, 17):
        if new_direct_dict[num] == -1:
            continue
        now_x = new_pos_dict[num][0]
        now_y = new_pos_dict[num][1]
        now_direct = new_direct_dict[num]

        for i in range(8):
            new_direct = (now_direct + i)%8
            new_x = now_x + dx[new_direct]
            new_y = now_y + dy[new_direct]
            if 0<=new_x<4 and 0<=new_y<4:
                # 움직이는 칸이, 말이 있는 위치인 경우
                if [new_x,new_y] == [x,y]:
                    continue
                # 빈칸인 경우
                if new_graph[new_x][new_y] == [-1,-1]:
                    new_pos_dict[num] = [new_x,new_y]
                    new_direct_dict[num] = new_direct

                    new_graph[now_x][now_y] = [-1,-1]
                    new_graph[new_x][new_y] = [num, new_direct]
                    break

                # 다른 말이 있는 경우
                if new_graph[new_x][new_y] != [-1,-1] and [new_x,new_y] != [x,y]:
                    other_num = new_graph[new_x][new_y][0]
                    other_direct = new_graph[new_x][new_y][1]

                    new_pos_dict[num] = [new_x,new_y]
                    new_direct_dict[num] = new_direct

                    new_pos_dict[other_num] = [now_x, now_y]
                    new_direct_dict[other_num] = other_direct

                    new_graph[now_x][now_y] = [other_num, other_direct]
                    new_graph[new_x][new_y] = [num, new_direct]
                    break


    # 술래말이 이동 (자신의 방향대로, 이동하기 - 범위 안에서)
    while 1:
        x = x + dx[horse_direct]
        y = y + dy[horse_direct]
        if not(0<=x<4 and 0<=y<4):
            return
        if new_graph[x][y] == [-1,-1]:
            continue
        dfs(new_graph, new_pos_dict, new_direct_dict, x,y,score)
    return
graph_ori = [[[-1,-1] for _ in range(4)] for _ in range(4)]
pos_dict_ori = {}
direct_dict_ori = {}
horse_x = 0
horse_y = 0
start_score = 0
max_score = -1

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1 ]

for i in range(4):
    input_info = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(4):
        a,b = input_info[2*j], input_info[2*j+1]
        graph_ori[i][j][0] = a
        graph_ori[i][j][1] = b - 1
        pos_dict_ori[a] = [i,j]
        direct_dict_ori[a] = b -1
        if i==0 and j ==0:
            pos_dict_ori[a] = [-1, -1]
            direct_dict_ori[a] = -1

dfs(graph_ori, pos_dict_ori, direct_dict_ori, horse_x, horse_y, start_score)
print(max_score)