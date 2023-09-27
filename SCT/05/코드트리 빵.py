import sys
from collections import deque

def find_start_camp(num):
    end_x,end_y = dict_end[num]
    q = deque()
    move_load = [[end_x, end_y]]
    q.append([end_x,end_y,move_load ])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[end_x][end_y] = 1

    while q:
        candi_result = []
        for _ in range(len(q)):
            a,b, now_load = q.popleft()
            # camp를 발견한 경우
            if graph_camp[a][b] == 1:
                candi_result.append([a,b,now_load])
                continue
            for d in range(4):
                nx = a + dx[d]
                ny = b + dy[d]
                if 0<=nx<n and 0<=ny<n:
                    # 이미 시작점인 곳 빼고
                    if graph_camp[nx][ny] != -1:
                        # 도착해서 못지나가는곳 빼고
                        if graph_no[nx][ny] != 1:
                            if visited[nx][ny] == -1:
                                visited[nx][ny] = 1
                                new_load = [[nx,ny]] + now_load
                                q.append([nx,ny, new_load])
        if len(candi_result) != 0:
            candi_result.sort(key = lambda x:(x[0],x[1]))
            real_x,real_y,real_load = candi_result[0]
            # 출발 상태로 만들기
            graph_no[real_x][real_y] = 1
            dict_move_load[num] = real_load
            return

def find_new_load(num,x,y):
    end_x,end_y = dict_end[num]
    q = deque()
    move_load = [[end_x, end_y]]
    q.append([end_x,end_y,move_load ])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[end_x][end_y] = 1

    while q:
        for _ in range(len(q)):
            a,b, now_load = q.popleft()
            # 목적지 말견한 경우
            if [a,b] == [x,y]:
                dict_move_load[num] = now_load
                return
            for d in range(4):
                nx = a + dx[d]
                ny = b + dy[d]
                if 0<=nx<n and 0<=ny<n:
                    # 이미 도착한 편의점이라, 지나가지 못하는곳
                    if graph_no[nx][ny] != 1:
                        if visited[nx][ny] == -1:
                            visited[nx][ny] = 1
                            new_load = [[nx,ny]] + now_load
                            q.append([nx,ny, new_load])

def move_indi(num):
    global dict_move_load
    # 다음 칸이 있는 경우
    nx,ny = dict_move_load[num][1] # 다음 칸
    if [nx,ny] == dict_end[num]:
        list_end[num] = 0
        graph_no[nx][ny] = 1
        dict_move_load[num] = [[-1, -1]]
    # 다음칸이 막힌 경우 -- x,y
    elif graph_no[nx][ny] == 1:
        x, y = dict_move_load[num][0]
        find_new_load(num,x,y)
        dict_move_load[num] = dict_move_load[num][1:]
    else:
        dict_move_load[num] = dict_move_load[num][1:]



def simulation():
    # 각 분 마다, 그에 해당하는 번호의 사람이 이동
    now_time = 1
    while 1:

        for num in range(1, min(now_time,m)+1):
            # 도착하지 않은 사람만
            if list_end[num] == 1:
                # 지금 출발한 사람 제외
                if num != now_time:
                    move_indi(num)

        # 새로운 살마 출발
        if 1<= now_time <= m:
            # 출발할 캠프 지점 탐색
            find_start_camp(now_time)
        # 모두 도착했으면 끝
        if sum(list_end) == 0:
            return now_time
        now_time += 1



n,m = map(int,sys.stdin.readline().rstrip().split())
graph_camp = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

graph_no = [[0 for _ in range(n)] for _ in range(n)]

dx = [1,0,0,-1]
dy = [0,1,-1,0]

dict_end = {}
dict_move_load = {}
list_end = [1 for _ in range(m+1)]
list_end[0] = 0

for num in range(1,m+1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    a -= 1
    b -= 1
    dict_end[num] = [a,b]
    dict_move_load[num] = []

result = simulation()
print(result)

"""
4 5
1 0 1 1
1 0 1 1
0 0 0 1
1 0 1 1
4 2
3 1
3 3
3 2
1 2

7

5 3
0 0 0 0 0
1 0 0 0 1
0 0 0 0 0
0 1 0 0 0
0 0 0 0 1
2 3
4 4
5 1


"""