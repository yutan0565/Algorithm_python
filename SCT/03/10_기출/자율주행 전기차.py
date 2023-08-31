import sys
from collections import deque


def find_start_point():
    global taxi_x,taxi_y, battery
    q = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q.append([taxi_x,taxi_y])
    visited[taxi_x][taxi_y] = 1
    candi_list = []
    while q:
        for _ in range(len(q)):
            a,b = q.popleft()
            if graph_start[a][b] != 0:
                candi_list.append([a, b])
                continue
            for d in range(4):
                nx = a + dx[d]
                ny = b + dy[d]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        if graph[nx][ny] == 0:
                            q.append([nx,ny])
                            visited[nx][ny] = 1
        if len(candi_list) != 0:
            candi_list.sort(key = lambda  x : (x[0],x[1]))
            taxi_x,taxi_y = candi_list[0]
            target_num = graph_start[taxi_x][taxi_y]
            graph_start[taxi_x][taxi_y] = 0
            return target_num
        else:
            battery -= 1
            if battery == 0:
                return -1
    return -1

def find_end_point(target_num):
    global taxi_x,taxi_y, battery
    q = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q.append([taxi_x,taxi_y])
    visited[taxi_x][taxi_y] = 1
    move_count = 0
    while q:
        for _ in range(len(q)):
            a,b = q.popleft()
            for d in range(4):
                nx = a + dx[d]
                ny = b + dy[d]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        if target_num in graph_end[nx][ny]:
                            graph_end[nx][ny].remove(target_num)
                            taxi_x, taxi_y = nx,ny
                            battery -= 1
                            move_count += 1
                            battery += (move_count* 2)
                            return target_num
                        if graph[nx][ny] == 0:
                            q.append([nx,ny])
                            visited[nx][ny] = 1
        move_count += 1
        battery -= 1
        if battery == 0:
            return -1
    return -1

n,m,battery = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_start = [[0 for _ in range(n)] for _ in range(n)]
graph_end = [[[] for _ in range(n)] for _ in range(n)]

taxi_x,taxi_y = map(int,sys.stdin.readline().rstrip().split())
taxi_x,taxi_y = taxi_x-1,taxi_y-1

live_num = [0 for _ in range(m+1)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]




for num in range(1,m+1):
    a,b,c,d = map(int,sys.stdin.readline().rstrip().split())
    a,b,c,d = a-1,b-1,c-1,d-1
    graph_start[a][b] = num
    graph_end[c][d].append(num)
    live_num[num] = 1


result = 0
while 1:
    target_num = find_start_point()

    if target_num == -1:
        result = -1
        break
    del_num = find_end_point(target_num)

    if del_num == -1:
        result = -1
        break
    live_num[del_num] = 0

    if sum(live_num) == 0:
        result = battery
        break
print(result)

"""
5 3 7
0 0 0 0 0
1 0 0 1 0
0 0 0 0 0
0 1 0 0 0
0 1 0 0 0
5 1
2 3 3 4
5 3 5 4
1 5 1 1


"""