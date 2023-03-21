import copy
import sys

def move_won():
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) == 0:
                continue
            for now_m, now_s, now_d in graph[i][j]:
                nx = (i + dx[now_d]*now_s)%n
                ny = (j + dy[now_d]*now_s)%n
                new_graph[nx][ny].append([now_m, now_s, now_d])
    return new_graph

def combine_won(x,y):
    won_list = graph[x][y]
    sum_m, sum_s, count = 0,0, len(won_list)
    divide_list = []
    for now_m, now_s, now_d in won_list:
        sum_m += now_m
        sum_s += now_s
        divide_list.append(now_d%2)

    # 4개에 대한 정보
    new_m = sum_m // 5
    new_s = sum_s // count

    graph[x][y] = []
    if new_m != 0:
        # 상하좌우 -> 각가 같음
        if sum(divide_list) == 0 or sum(divide_list) == len(won_list):
            for d in [0,2,4,6]:
                graph[x][y].append([new_m, new_s, d])
        # 대각선
        else:
            for d in [1,3,5,7]:
                graph[x][y].append([new_m, new_s, d])

def cal_sum():
    temp_sum = 0
    for i in range(n):
        for j in range(n):
            for g in graph[i][j]:
                temp_sum += g[0]
    return temp_sum

def show_graph():
    for g in graph:
        print(g)
    print("-"*20)

n,m,k = map(int, sys.stdin.readline().rstrip().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(m):
    x,y,m,s,d = map(int, sys.stdin.readline().rstrip().split())
    x,y = x-1,y-1
    graph[x][y].append([m,s,d])

for time in range(1, k+1):
    # 속력 만큼, 방향 이동  // 범위 넘어가면, 지구 처럼
    graph = move_won()
    # 하나의 칸에 2개 이상 있으면 합성
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) >= 2:
                combine_won(i,j)
    # print(time)
    # show_graph()

result = cal_sum()
print(result)