import sys
from collections import defaultdict
from collections import deque

def find_people():
    global now_battery
    q = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q.append([taxi_x, taxi_y])
    visited[taxi_x][taxi_y] = 1
    candi_pos = []

    while q:
        for _ in range(len(q)):
            a,b= q.popleft()
            # 다른 사람이 있는 경우
            if graph_info[a][b] > 0:
                candi_pos.append([a,b])
                continue
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        if graph[nx][ny] == 0:
                            q.append([nx,ny])
                            visited[nx][ny] = 1
        # 후보가 있는 경우
        if len(candi_pos) != 0:
            candi_pos.sort(key = lambda  x : (x[0],x[1]))
            target_x, target_y = candi_pos[0][0], candi_pos[0][1]
            target_num = graph_info[target_x][target_y]
            target_pos = dict_end[graph_info[target_x][target_y]]
            return [target_x, target_y], now_battery, target_pos, target_num
        # 한칸 이동 했으니까, 배터리 1 감소
        now_battery -= 1
        # 베터리가 중간에 없는 경우
        if now_battery == -1:
            return [-1, -1], -1, [-1, -1], -1
    return [-1, -1], -1, [-1, -1], -1

def find_end(target_pos, target_num):
    global now_battery
    q = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q.append([taxi_x, taxi_y])
    visited[taxi_x][taxi_y] = 1
    move_count = 0

    while q:
        for _ in range(len(q)):
            a,b = q.popleft()
            # 다른 사람이 있는 경우
            if [a,b] == target_pos:
                # 충전 해주기
                now_battery += move_count*2
                # 지워주기
                list_live[target_num] = 0
                return [a,b], now_battery
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        if graph[nx][ny] == 0:
                            q.append([nx,ny])
                            visited[nx][ny] = 1
        # 한칸 이동 했으니까, 배터리 1 감소
        now_battery -= 1
        # 베터리가 중간에 없는 경우
        if now_battery == -1:
            return [-1, -1], -1
        # 이동칸 증가
        move_count += 1
    return [-1, -1], -1



n,m,now_battery = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_info = [[0 for _ in range(n)] for _ in range(n)]
temp_x,tmep_y = map(int,sys.stdin.readline().rstrip().split())
taxi_x,taxi_y = temp_x-1, tmep_y-1

dict_start = defaultdict(lambda : [])
dict_end = defaultdict(lambda : [])
list_live = [1 for _ in range(m+1)]
list_live[0] = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for num in range(1,m+1):
    a,b,c,d = map(int,sys.stdin.readline().rstrip().split())
    graph_info[a-1][b-1] = num
    dict_end[num] = [c-1,d-1]

result = 0
count = 0
while 1:

    # 사람 찾아 떠나기
    start_point, now_battery, target_pos, target_num = find_people()
    taxi_x, taxi_y = start_point

    graph_info[taxi_x][taxi_y] = 0
    if now_battery == -1:
        result = -1
        break
    # 목적지 따라 떠나기
    end_point, now_battery = find_end(target_pos, target_num)
    taxi_x, taxi_y = end_point

    if now_battery == -1:
        result = -1
        break
    # 모든 승객 태우면 끝
    if sum(list_live) == 0:
        result = now_battery
        break

print(result)