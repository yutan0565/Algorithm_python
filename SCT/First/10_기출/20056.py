#마법사 상어와 파이어볼
import sys

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def move_fire():
    temp_graph = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) != 0:
                for d in range(len(graph[i][j])):
                    weight =  graph[i][j][d][0]
                    speed = graph[i][j][d][1]
                    direct = graph[i][j][d][2]

                    nx = (i + dx[direct]*speed)%n
                    ny = (j + dy[direct]*speed)%n
                    temp_graph[nx][ny].append([weight,speed,direct])
    return temp_graph

def find_new_direct(direct):
    for i in range(1, len(direct)):
        if direct[i]%2 != direct[i-1]%2:
            return [1,3,5,7]
    return [0,2,4,6]

def divide_fire(x,y):
    direct_list = []
    number_fire = len(graph[x][y])
    sum_weight, sum_speed = 0,0
    for i in range(len(graph[x][y])):
        sum_weight += graph[x][y][i][0]
        sum_speed += graph[x][y][i][1]
        direct_list.append(graph[x][y][i][2])

    new_weihgt = sum_weight // 5
    new_speed = sum_speed // number_fire
    new_direct = find_new_direct(direct_list)

    if new_weihgt == 0:
        graph[x][y] = []
    else:
        graph[x][y] = []
        for i in range(4):
            graph[x][y].append([new_weihgt, new_speed, new_direct[i]])

def check_weight_fire():
    weight_sum = 0
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) != 0:
                for d in range(len(graph[i][j])):
                    weight_sum += graph[i][j][d][0]
    return weight_sum

n,ball_count,k = map(int, sys.stdin.readline().rstrip().split())

graph = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(ball_count):
    x,y,m,s,d = map(int, sys.stdin.readline().rstrip().split())
    x,y = x-1, y-1
    graph[x][y].append([m,s,d])

for _ in range(k):

    # 파이어볼 이동
    graph = move_fire()

    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) >= 2:
                divide_fire(i,j)
    # 파이어볼 2개인 경우, 명령 진행



result = check_weight_fire()
print(result)

"""
fire_ball
    r,c  위치
    m 질량
    d 방향
    s 속력
    
명령
     1. d 방향으로 s 칸 만큼 이동 (같은 칸에 여러개의 파이어볼 가능)
     
     2. 두개의 파이어 볼이 있는 경우
        같은 칸에 있는 파이어볼은 모두 하나로 합쳐짐
        파이어볼은 4개로 나누어짐
        나누어진 파어볼
            질량 : 합쳐진 파이어 볼의 /5
            속력 : 합쳐진 파이어볼의 속력 합 / 파이어볼 개수
            방향 : 모두 홀수 or 짝수 (두개의 경우를 고려 해야함)
        질량이 0인 파이볼은 벗어짐

k번 명령하면, 질량이 몇 남음 ?


"""