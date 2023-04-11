import copy
import sys

def move_medi_put(d,p):
    new_medi_graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph_medi[i][j] == 1:
                nx = (i + dx_move[d]*p)%n
                ny = (j + dy_move[d]*p)%n
                new_medi_graph[nx][ny] = 1
                graph[nx][ny] += 1
    return new_medi_graph

def grow_flower():
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graph_medi[i][j] == 1:
                count = 0
                for d in range(4):
                    nx = i + dx_check[d]
                    ny = j + dy_check[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] >= 1:
                            count += 1
                new_graph[i][j] += count
    return new_graph

def cut_flower():
    new_medi_graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph_medi[i][j] != 1:
                if graph[i][j] >=2:
                    graph[i][j] -= 2
                    new_medi_graph[i][j] = 1
    return new_medi_graph

def cal_height():
    count = 0
    for i in range(n):
        for j in range(n):
            count += graph[i][j]
    return count

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_medi = [[0 for _ in range(n)] for _ in range(n)]

graph_medi[n-1][0], graph_medi[n-1][1], graph_medi[n-2][0], graph_medi[n-2][1] =1,1,1,1

dx_move = [0,-1,-1,-1,0,1,1,1]
dy_move = [1,1,0,-1,-1,-1,0,1]
![](../../../../../../AppData/Local/Temp/d70e6568-6d86-4a5d-b7e8-b82dc8af1742.png)
dx_check = [1,1,-1,-1]
dy_check = [1,-1,1,-1]

for year in range(1,m+1):
    d,p = map(int,sys.stdin.readline().rstrip().split())
    d = d-1
    # 영양제 이동 / 투입
    graph_medi = move_medi_put(d,p)
    # 꽃 성장
    graph = grow_flower()
    # 잘라내기 / 영야제 추가
    graph_medi = cut_flower()

result = cal_height()
print(result)