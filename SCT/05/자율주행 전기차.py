import sys
from collections import deque
from collections import defaultdict

def find_start_point():
    global now_battery, graph_start, taxi_x, taxi_y
    q = deque()
    q.append([taxi_x, taxi_y])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[taxi_x][taxi_y] = 0

    # 지금 자리가 시작점인 경우
    if graph_start[taxi_x][taxi_y] != 0:
        re_num = graph_start[taxi_x][taxi_y]
        graph_start[taxi_x][taxi_y] = 0
        return taxi_x, taxi_y, re_num


    while q:
        if now_battery == 0:
            return -1,-1,-1

        start_candi = []
        for _ in range(len(q)):
            a,b = q.popleft()
            for d in range(4):
                nx = a + dx[d]
                ny = b + dy[d]
                if 0<=nx<n and 0<=ny<n:
                    if graph[nx][ny] == 0:
                        if visited[nx][ny] == -1:
                            # start 지점이 아닌 경우
                            if graph_start[nx][ny] == 0:
                                q.append([nx,ny])
                                visited[nx][ny] = visited[a][b] + 1
                            # start 지점인 경우
                            else:
                                start_candi.append([nx,ny,graph_start[nx][ny]])
        # 이동 끝났으니, 배터리 줄어들기
        now_battery -= 1

        # 후보군이 있는 경우
        if len(start_candi) != 0:
            start_candi.sort(key = lambda x : (x[0],x[1]))
            re_x = start_candi[0][0]
            re_y = start_candi[0][1]
            re_num = start_candi[0][2]
            graph_start[re_x][re_y] = 0
            taxi_x = re_x
            taxi_y = re_y
            return re_x, re_y, re_num
    return -1, -1, -1

def find_end_point(end_num):
    global now_battery, graph_end, taxi_x, taxi_y
    q = deque()
    q.append([taxi_x, taxi_y])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[taxi_x][taxi_y] = 0

    while q:
        if now_battery == 0:
            return False
        for _ in range(len(q)):
            a, b = q.popleft()
            for d in range(4):
                nx = a + dx[d]
                ny = b + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 0:
                        if visited[nx][ny] == -1:
                            # 끝나는 지점에 도착
                            if end_num in graph_end[nx][ny] :
                                graph_end[nx][ny].remove(end_num)
                                done_list[end_num] = 0
                                now_battery = now_battery-1 +  2*(visited[a][b] + 1)
                                taxi_x = nx
                                taxi_y = ny
                                return True
                            # 아무것도 없는 경우
                            else:
                                q.append([nx,ny])
                                visited[nx][ny] = visited[a][b] + 1

        now_battery -= 1
    return False

def show_info():
    print("======taxi_point=======")
    print([taxi_x,taxi_y])

    print("======battery=======")
    print(now_battery)
    print("======graph_start=======")
    for g in graph_start:
        print(g)
    print("======graph_end=======")
    for g in graph_end:
        print(g)
    print("======done_list=========")
    print(done_list)
    print()
    return

def simulation():
    while 1:
        # 시작 점 찾기
        x,y,num = find_start_point()
        # 배터리가 부족한 경우
        if [x,y,num] == [-1,-1,-1]:
            return -1
        # 도착 점 찾기
        done_falg = find_end_point(num)
        if done_falg == False:
            return -1
        # 다 끝났는지 검사
        if sum(done_list) == 0:
            break

    return now_battery


n,m,now_battery = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

graph_start = [[0 for _ in range(n)] for _ in range(n)]
graph_end = [[[] for _ in range(n)] for _ in range(n)]
done_list = [1 for _ in range(m+1)]
done_list[0] = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

taxi_x, taxi_y = map(int,sys.stdin.readline().rstrip().split())
taxi_x -=1
taxi_y -= 1
for num in range(1, m+1):
    a,b,c,d = map(int,sys.stdin.readline().rstrip().split())
    graph_start[a-1][b-1] = num
    graph_end[c-1][d-1].append(num)

result = simulation()
print(result)