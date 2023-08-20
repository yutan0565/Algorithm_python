import copy
import sys

def move_medi(direct,speed):
    global graph_medi
    new_graph_medi = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph_medi[i][j] == 1:
                nx = (i + dx[direct]*speed)%n
                ny = (j + dy[direct]*speed)%n
                new_graph_medi[nx][ny] = 1
    graph_medi = new_graph_medi

def add_medi():
    global graph
    for i in range(n):
        for j in range(n):
            if graph_medi[i][j] == 1:
                graph[i][j] += 1

def grow():
    global graph
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            # 영양제가 있는 곳에 대해서
            if graph_medi[i][j] == 1:
                cnt = 0
                for d in range(1, 8, 2):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] >= 1:
                            cnt += 1
                new_graph[i][j] += cnt
    graph = new_graph

def new_medi():
    global graph, graph_medi
    new_graph_medi = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph_medi[i][j] == 0:
                if graph[i][j] >= 2:
                    new_graph_medi[i][j] = 1
                    graph[i][j] -= 2
    graph_medi = new_graph_medi

def simulation():
    for year in range(1, m+1):
        direct, speed = map(int,sys.stdin.readline().rstrip().split())
        direct -= 1
        # 영양제 이동
        move_medi(direct,speed)
        # 영양제 투입
        add_medi()
        # 추가 성장
        grow()
        # 새로운 영양제 투입
        new_medi()


def cal_total_height():
    total_height = 0
    for i in range(n):
        for j in range(n):
            total_height += graph[i][j]
    return total_height

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_medi = [[0 for _ in range(n)] for _ in range(n)]
graph_medi[n-1][0], graph_medi[n-1][1],graph_medi[n-2][0], graph_medi[n-2][1] = 1,1,1,1

dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]

simulation()
result = cal_total_height()
print(result)