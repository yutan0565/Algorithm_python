import copy
import sys

def find_start_point():
    start_end_point = []
    line_flag = 0
    first_direct = -1
    first_d_flag = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "#":
                load_count = 0
                load_direct = -1
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<m:
                        if graph[nx][ny] == "#":
                            load_count += 1
                            load_direct = d
                if load_count == 1:
                    start_end_point.append(([i,j]))
                    line_flag = 1
                    if first_d_flag == 0:
                        first_direct = load_direct
                        first_d_flag = 1
    if line_flag == 1:
        return start_end_point, first_direct
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == "#":
                    for d in range(4):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if graph[nx][ny] == "#":
                                start_end_point = [[i,j],[nx,ny]]
                                return start_end_point, d

def find_result(start, end, first_direct):
    x,y = start[0], start[1]
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[x][y] = 1
    order_list = []
    now_d = first_direct
    while 1:
        if [x,y] == end:
            break
        nx_check = x + dx[now_d]
        ny_check = y + dy[now_d]
        nx = x + dx[now_d]*2
        ny = y + dy[now_d]*2
        # 그냥 갈 수 있는 경우
        if 0<=nx<n and 0<=ny<m:
            if visited[nx][ny] == -1 and visited[nx_check][ny_check] == -1:
                if graph[nx][ny] == "#" and graph[nx_check][ny_check]=="#":
                    order_list.append("A")
                    visited[nx][ny] = 1
                    visited[nx_check][ny_check] = 1
                    x,y = nx,ny
                    continue
        right_d = (now_d + 1)%4
        nx_check = x + dx[right_d]
        ny_check = y + dy[right_d]
        nx = x + dx[right_d] * 2
        ny = y + dy[right_d] * 2
        # 오른 쪽 회전하면 이동 가능
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == -1 and visited[nx_check][ny_check] == -1:
                if graph[nx][ny] == "#" and graph[nx_check][ny_check]=="#":
                    order_list.append("R")
                    now_d = right_d
                    continue
        left_d = (now_d - 1)%4
        nx_check = x + dx[left_d]
        ny_check = y + dy[left_d]
        nx = x + dx[left_d] * 2
        ny = y + dy[left_d] * 2
        # 오른 쪽 회전하면 이동 가능
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == -1 and visited[nx_check][ny_check] == -1:
                if graph[nx][ny] == "#" and graph[nx_check][ny_check]=="#":
                    order_list.append("L")
                    now_d = left_d
                    continue
    return order_list
n,m = map(int,sys.stdin.readline().rstrip().split())
graph = []
count = 0
for i in range(n):
    temp = list(sys.stdin.readline().rstrip())
    graph.append(temp)
    for j in range(m):
        if graph[i][j] == "#":
            count += 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]
direct_list = ["^", ">", "v", "<"]

start_end_point, first_direct = find_start_point()
order_list = find_result(start_end_point[0], start_end_point[1], first_direct)
print(start_end_point[0][0]+1, start_end_point[0][1]+1)
print(direct_list[first_direct])
for order in order_list:
    print(order, end = "")

