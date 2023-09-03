import sys
from collections import deque

def find_base(num):
    x,y = dict_mart[num]
    move_list = [[x,y]]
    q = deque()
    q.append([x,y, move_list])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    candi_list = []
    while q:
        for _ in range(len(q)):
            a,b,now_move_list = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        # 그냥 길이면
                        if graph[nx][ny] == 0:
                            new_move_list = [[nx,ny]] +  now_move_list
                            q.append([nx,ny,new_move_list])
                            visited[nx][ny] = 1
                        # 베이스 캠프 찾았으면
                        elif graph[nx][ny] == 1:
                            new_move_list = [[nx,ny]] +  now_move_list
                            visited[nx][ny] = 1
                            candi_list.append([nx,ny,new_move_list])
        if len(candi_list) != 0:
            candi_list.sort(key = lambda x:(x[0],x[1]))
            base_x, base_y = candi_list[0][0], candi_list[0][1]
            best_walk = candi_list[0][2]

            dict_base[num] = [base_x, base_y]
            dict_best_walk[num] = best_walk[1:] # base 지점 제외

            # 처음 시자 위치 지정
            dict_pos[num] = [base_x, base_y]
            # base 지정 된 곳은 움직이지 못하는 곳으로 설정
            graph[base_x][base_y]  = -10
            break

def find_new_best_walk(num, start, end):
    q = deque()
    x,y = start
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    now_best_walk = []

    visited[x][y] = 1
    q.append([x,y, now_best_walk])

    while q:
        a,b,best_walk = q.popleft()
        if [a,b] == end:
            dict_best_walk[num] = best_walk
            dict_pos[num] = [x,y]
            break

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1:
                    # 못지나가는 길이 아니면 / -10인 경우
                    if graph[nx][ny] != -10:
                        new_best_walk = best_walk + [[nx, ny]]
                        q.append([nx, ny, new_best_walk])
                        visited[nx][ny] = 1

def move_one_step_people(num):
    mart_x, mart_y = dict_mart[num]
    now_x,now_y = dict_pos[num]
    best_walk = dict_best_walk[num]

    # 다음 움직임 장소
    nx,ny = best_walk[0]
    del best_walk[0] # 뽑아냈으면 / 제거

    # 내 목적지인 경우
    if [nx,ny] == [mart_x, mart_y]:
        list_arrive[num] = 0
        dict_pos[num] = [nx,ny]
        dict_best_walk[num] = []
        # 도착 지점은 다른 애들이 못오게 막기
        graph[nx][ny] = -10
    # 움직이는 장소가  이동 가능  0 / 1
    elif graph[nx][ny] == 0 or graph[nx][ny] == 1:
        dict_pos[num] = [nx,ny]
        dict_best_walk[num] = best_walk
    # 이동 불가능한 곳인 경우 -> 다시 새로운 최적 경로 탐색
    else:
        start = [now_x,now_y]
        end = [mart_x, mart_y]
        find_new_best_walk(num, start, end)
        move_one_step_people(num)

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_pos = [[0 for _ in range(n)] for _ in range(n)]

dict_mart = {}
dict_base = {}
dict_pos = {}
dict_best_walk = {}
list_arrive = [0 for _ in range(m+1)]

for num in range(1, m+1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    dict_mart[num] = [a-1,b-1]

dx = [-1,0,0,1]
dy = [0,-1,1,0]

time = 1
while 1:
    # 사람 새롭게 추가 하기
    if time <= m:
        find_base(time)
        list_arrive[time] = 1

    # 지금 올라가 있는 사람만 , 순서대로 이동하기
    for num in range(1, m+1):
        # 지금 들어온 사람은 이동 안함
        if num == time:
            continue
        # 아직 살아있는 사람만
        if list_arrive[num] == 1 :
            # print(num)
            move_one_step_people(num)



    if sum(list_arrive) == 0:
        break
    time += 1

print(time)
