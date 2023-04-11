import sys

def reverse(list):
    new_list = []
    for i in range(len(list)-1, -1 , -1):
        new_list.append(list[i])
    return new_list

def move_circle(number):
    for i in range(n):
        for j in range(n):
            for d in range(len(graph[i][j])):
                if graph[i][j][d][0] ==  number :
                    nx = i + dx[graph[i][j][d][1]]
                    ny = j + dy[graph[i][j][d][1]]
                    if not(0<=nx<n and 0<=ny<n) or color[nx][ny] == 2:
                        if graph[i][j][d][1] == 0:
                            graph[i][j][d][1] = 1
                        elif graph[i][j][d][1] == 1:
                            graph[i][j][d][1] = 0
                        elif graph[i][j][d][1] == 2:
                            graph[i][j][d][1] = 3
                        elif graph[i][j][d][1] == 3:
                            graph[i][j][d][1] = 2
                        nx = i + dx[graph[i][j][d][1]]
                        ny = j + dy[graph[i][j][d][1]]
                    if not(0<=nx<n and 0<=ny<n) or color[nx][ny] == 2:
                        return
                    if color[nx][ny] == 0:
                        move_list = graph[i][j][d:]
                        graph[i][j] = graph[i][j][:d]
                        graph[nx][ny] += move_list
                        if len(graph[nx][ny]) >= 4:
                            return 1
                    elif color[nx][ny] == 1:
                        move_list = graph[i][j][d:]
                        graph[i][j] = graph[i][j][:d]
                        reverse_list = reverse(move_list)
                        graph[nx][ny] += reverse_list
                        if len(graph[nx][ny]) >= 4:
                            return 1
                    return -1


def check_graph():
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) >= 4:
                return 1
    return -1



def cal_turn():
    turn = 0
    while 1:
        turn += 1
        if turn == 1001:
            return -1
        for number in range(1, k + 1):
            stop_flag = move_circle(number)
            if stop_flag == 1:
                return turn

n,k = map(int,sys.stdin.readline().rstrip().split())
color = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph = [[[] for _ in range(n)] for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for number in range(1,k+1):
    x,y,d = map(int,sys.stdin.readline().rstrip().split())
    x,y,d = x-1, y-1, d-1
    graph[x][y].append([number, d])

result =  cal_turn()
print(result)

