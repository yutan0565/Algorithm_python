import copy
import sys



dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

def move_cloud():
    global cloud
    temp_cloud = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                nx = (i + dx[direct]*speed)%n
                ny = (j + dy[direct]*speed)%n
                temp_cloud[nx][ny] = 1
                graph[nx][ny] += 1
    cloud = temp_cloud

def copy_water():
    global graph, cloud
    temp_graph = copy.deepcopy(graph)
    temp_cloud = [[0 for _ in range(n)] for _ in range(n)]
    dx_copy = [-1,-1,1,1]
    dy_copy = [1,-1,1,-1]

    for i in range(n):
        for j in range(n):
            # 구름이 있던곳
            if cloud[i][j] == 1:
                near_water = 0
                for d in range(4):
                    nx = i + dx_copy[d]
                    ny = j + dy_copy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] != 0:
                            near_water += 1
                temp_graph[i][j] += near_water

            # 구름이 없던 곳
            elif cloud[i][j] == 0:
                if temp_graph[i][j] >= 2:
                    temp_cloud[i][j] = 1
                    temp_graph[i][j] -= 2

    graph = temp_graph
    cloud =temp_cloud

def sum_water():
    water = 0
    for i in range(n):
        for j in range(n):
            water += graph[i][j]
    return water

n,m = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
cloud = [[0 for _ in range(n)] for _ in range(n)]
order_list = []
for _ in range(m):
    d,s = map(int, sys.stdin.readline().rstrip().split())
    order_list.append([d-1, s])

# 첫 구름 생성
cloud[n-1][0] = 1
cloud[n-1][1] = 1
cloud[n-2][0] = 1
cloud[n-2][1] = 1

for direct, speed in order_list:
    move_cloud()
    copy_water()


result = sum_water()
print(result)