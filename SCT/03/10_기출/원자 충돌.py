import sys

def move_atom():
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != []:
                for weight, speed, direct in graph[i][j]:
                    nx = (i + dx[direct]*speed)%n
                    ny = (j + dy[direct]*speed)%n
                    new_graph[nx][ny].append([weight,speed,direct])
    return new_graph

def combine_atom():
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):

            if len(graph[i][j]) < 2:
                new_graph[i][j] = graph[i][j]
            elif len(graph[i][j]) >= 2:
                sum_weight, sum_speed, sum_direct = 0,0,0
                for weight, speed, direct in graph[i][j]:
                    sum_weight += weight
                    sum_speed += speed
                    sum_direct += (direct%2)

                new_weight = sum_weight//5
                new_speed = sum_speed // (len(graph[i][j]))
                if new_weight != 0:
                    if sum_direct == 0 or sum_direct == len(graph[i][j]):
                        for d in range(0,8,2):
                            new_graph[i][j].append([new_weight, new_speed,d])
                    else:
                        for d in range(1,8,2):
                            new_graph[i][j].append([new_weight, new_speed,d])
    return new_graph

def cal_atom():
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] != []:
                for weight, speed, direct in graph[i][j]:
                    count += weight
    return count

n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(m):
    x,y,m,s,d = map(int,sys.stdin.readline().rstrip().split())
    x,y = x-1,y-1
    graph[x][y].append([m,s,d])

for time in range(1,k+1):
    graph = move_atom()
    graph = combine_atom()


atom_count = cal_atom()
print(atom_count)

"""
4 1 5
4 2 5 6 0

"""