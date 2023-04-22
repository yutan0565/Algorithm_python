import copy
import sys
import heapq

def move_theif(horse_pos , now_dict_pos, now_dict_direct,now_graph):
    new_dict_pos = copy.deepcopy(now_dict_pos)
    new_dict_direct = copy.deepcopy(now_dict_direct)
    new_graph = copy.deepcopy(now_graph)

    new_dict_pos[new_graph[horse_pos[0]][horse_pos[1]]] = [-1,-1]
    new_dict_direct[new_graph[horse_pos[0]][horse_pos[1]]] = -1
    new_graph[horse_pos[0]][horse_pos[1]] = -1
    for number in range(1,17):
        x,y = new_dict_pos[number]
        if [x,y] == [-1,-1]:
            continue
        now_d = new_dict_direct[number]
        for i in range(8):
            new_d = (now_d + i)%8
            nx = x + dx[new_d]
            ny = y + dy[new_d]
            if 0<=nx<4 and 0<=ny<4:
                if [nx,ny] != horse_pos:
                    check_number = new_graph[nx][ny]
                    if check_number == -1: # 말이 없어
                        new_graph[x][y], new_graph[nx][ny] = new_graph[nx][ny], new_graph[x][y]
                        new_dict_pos[number] = [nx,ny]
                        new_dict_direct[number] = new_d
                        break
                    else: # 말이 있어
                        new_graph[x][y], new_graph[nx][ny] = new_graph[nx][ny], new_graph[x][y]
                        new_dict_pos[number], new_dict_pos[check_number] = new_dict_pos[check_number], new_dict_pos[number]
                        new_dict_direct[number] = new_d
                        break
    return new_dict_pos, new_dict_direct, new_graph


def bfs():
    # 초기 상태
    del_number = graph[0][0]
    score = del_number
    start_direct = dict_direct[del_number]
    init_dict_pos, init_dict_direct, init_graph = move_theif([0,0] , dict_pos, dict_direct,graph)
    q = []
    heapq.heappush(q,[-score, score,start_direct, init_dict_pos, init_dict_direct,init_graph, 0,0])

    max_score = score

    while q:
        _, now_socre,now_direct,now_dict_pos, now_dict_direct,now_graph,a,b = heapq.heappop(q)
        if max_score < now_socre:
            max_score = max(max_score, now_socre)

        count = 1
        while 1:
            nx = a + dx[now_direct]*count
            ny = b + dy[now_direct]*count
            if 0<=nx< 4 and 0<=ny<4:
                if now_graph[nx][ny] != -1:
                    new_score = now_socre + now_graph[nx][ny]
                    new_direct = now_dict_direct[now_graph[nx][ny]]
                    new_dict_pos, new_dict_direct,new_graph = move_theif([nx,ny],now_dict_pos, now_dict_direct,now_graph )
                    heapq.heappush(q, [-new_score,new_score, new_direct,  new_dict_pos, new_dict_direct,new_graph, nx,ny])
            else:
                break
            count += 1
    return max_score
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

dict_pos = {}
dict_direct = {}
graph = [[ 0 for _ in range(4)] for _ in range(4)]

count = 0
for _ in range(4):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    for i in range(0,8,2):
        temp_number = temp[i]
        temp_direct = temp[i+1] - 1
        x = count //4
        y = count % 4
        graph[x][y] = temp_number
        dict_pos[temp_number] = [x,y]
        dict_direct[temp_number] = temp_direct
        count += 1

result = bfs()
print(result)


