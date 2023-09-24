import re
import sys

def move_atom():
    global graph
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != []:
                for num in range(len(graph[i][j])):
                    now_m, now_s, now_d = graph[i][j][num]
                    nx = (i + dx[now_d]*now_s)%n
                    ny = (j + dy[now_d] * now_s) % n
                    new_graph[nx][ny].append([now_m,now_s,now_d])
    graph = new_graph

def change_atom():
    global graph
    new_graph = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 아무것도 없는 경우
            if graph[i][j] == []:
                continue
            # 하나만 있는 경우
            elif len(graph[i][j]) == 1:
                new_graph[i][j] = graph[i][j]
            # 2개 이상 존재하는 경우
            else:
                sum_weight = 0
                sum_speed = 0

                odd_flag = False
                even_flag = False

                for num in range(len(graph[i][j])):
                    now_m, now_s, now_d = graph[i][j][num]
                    sum_weight += now_m
                    sum_speed += now_s
                    if now_d%2 == 0:
                        odd_flag = True
                    elif now_d%2 == 1:
                        even_flag = True

                new_weight = sum_weight // 5
                new_speed = sum_speed // len(graph[i][j])

                # 질량이 0인 경우
                if new_weight == 0:
                    continue
                else:
                    # 둘다 True면 대각선
                    if odd_flag == True and even_flag == True:
                        for new_d in range(1, 8, 2):
                            new_graph[i][j].append([new_weight,new_speed,new_d])
                    # 그 외는 -> 하나만 True인 경우 - 4가지 방향
                    else:
                        for new_d in range(0,8,2):
                            new_graph[i][j].append([new_weight, new_speed, new_d])
    graph = new_graph

def simulation():
    for time in range(1, k+1):
        # 자신의 방향대로 이동
        move_atom()
        # 2개 이상 있으면 변화 시작
        change_atom()
    return

def cal_atom():
    result = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] != []:
                for num in range(len(graph[i][j])):
                    result += graph[i][j][num][0]
    return result


n,m,k = map(int,sys.stdin.readline().rstrip().split())

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

graph = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    a,b,c,d,e = map(int,sys.stdin.readline().rstrip().split())
    # 질량 속도 방향
    graph[a-1][b-1].append([c,d,e])

simulation()
result = cal_atom()
print(result)