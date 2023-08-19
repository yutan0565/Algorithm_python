import copy
import re
import sys

def move_medi_put_medi(direct, p):
    new_graph_medi = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph_medi[i][j] == 1:
                nx = (i + dx_move[direct]*p)%n
                ny = (j + dy_move[direct]*p)%n
                new_graph_medi[nx][ny] = 1
                graph_flower[nx][ny] += 1
    return new_graph_medi

def check_cross():
    new_graph_flower = copy.deepcopy(graph_flower)
    for i in range(n):
        for j in range(n):
            if graph_medi[i][j] == 1:
                count = 0
                for d in range(4):
                    nx = i + dx_check[d]
                    ny = j + dy_check[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph_flower[nx][ny] >= 1:
                            count += 1
                new_graph_flower[i][j] += count
    return new_graph_flower

def cut_flower():
    new_graph_medi = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph_medi[i][j] != 1:
                if graph_flower[i][j] >= 2:
                    graph_flower[i][j] -= 2
                    new_graph_medi[i][j] = 1
    return new_graph_medi

def cal_flower():
    count = 0
    for i in range(n):
        for j in range(n):
            count += graph_flower[i][j]
    return count

dx_move = [0,-1,-1,-1,0,1,1,1]
dy_move = [1,1,0,-1,-1,-1,0,1]

dx_check = [1,1,-1,-1]
dy_check = [1,-1,1,-1]

n,m = map(int,sys.stdin.readline().rstrip().split())
graph_flower = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_medi = [[0 for _ in range(n)] for _ in range(n)]
graph_medi[n-1][0], graph_medi[n-1][1], graph_medi[n-2][0], graph_medi[n-2][1] = 1,1,1,1

for round in range(1,m+1):
    d,p = map(int,sys.stdin.readline().rstrip().split())
    d = d-1
    # 영양제 이동 / 영야제 투입
    graph_medi = move_medi_put_medi(d,p)
    # 대각선 체크 / 성장
    graph_flower = check_cross()
    # 영양제 투입칸 제외하고 / 높이 2 이상 잘라내기
    graph_medi = cut_flower()

result = cal_flower()
print(result)