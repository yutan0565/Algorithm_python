import sys

def move_atom():
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 원자가 있는 곳에서 진행
            if len(graph[i][j]) != 0:
                # 각 원자 마다 이동
                for atom_info in graph[i][j]:
                    weight, speed, direct = atom_info
                    nx = (i + dx[direct]*speed)%n
                    ny = (j + dy[direct]*speed)%n
                    new_graph[nx][ny].append([weight,speed,direct])
    return new_graph

def combine_atom():
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 원자가 2개 이상 있는 칸에서 합성 진행
            if len(graph[i][j]) >= 2:
                sum_weight = 0
                sum_speed = 0
                count = 0
                type_list = []
                for atom_info in graph[i][j]:
                    weight, speed, direct = atom_info
                    sum_weight += weight
                    sum_speed += speed
                    type_list.append(direct%2)
                    count += 1
                # 새로운 원자
                new_weight = sum_weight // 5
                new_speed = sum_speed // count

                # 새로운 질량이 0 이 아닌 경우에만
                if new_weight != 0:
                    # 바향의 타입이 같음 (상하좌우 / 대각선) 2로 나누면 0 나와야함
                    if sum(type_list) == 0 or sum(type_list) == count:
                        for new_d in range(0,8,2):
                            new_graph[i][j].append([new_weight, new_speed, new_d])
                    # 다른거 섞임
                    else:
                        for new_d in range(1,8,2):
                            new_graph[i][j].append([new_weight, new_speed, new_d])
            # 빈칸이거나, 1개만 있으면, 그냥 이어 붙여주기
            else:
                new_graph[i][j] += graph[i][j]
    return new_graph

def cal_sum_weight():
    sum_weight = 0
    for i in range(n):
        for j in range(n):
            # 원자가 있는 곳에서 진행
            if len(graph[i][j]) != 0:
                # 각 원자 마다 이동
                for atom_info in graph[i][j]:
                    weight, speed, direct = atom_info
                    sum_weight += weight
    return sum_weight

n,won,k = map(int,sys.stdin.readline().rstrip().split())
graph = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(won):
    x,y,m,s,d = map(int,sys.stdin.readline().rstrip().split())
    x,y = x-1,y-1
    graph[x][y].append([m,s,d])

for time in range(1, k+1):
    # 원자 이동
    graph = move_atom()

    # 원자 합성
    graph = combine_atom()


result = cal_sum_weight()
print(result)

