import sys

def hunt_shark(hunter_index):
    global result
    for i in range(r):
        if graph[i][hunter_index] != []:
            result += graph[i][hunter_index][0][2]
            graph[i][hunter_index] = []
            break

def change_direct(direct):
    if direct == 0:
        return 1
    elif direct == 1:
        return 0
    elif direct == 2:
        return 3
    elif direct == 3:
        return 2

def move_shark(graph):
    new_graph = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] != []:
                speed = graph[i][j][0][0]
                size = graph[i][j][0][2]
                x,y = i,j

                for d in range(1,speed+1):
                    nx = x + dx[graph[i][j][0][1]]
                    ny = y + dy[graph[i][j][0][1]]
                    if not(0<=nx<r and 0<=ny<c):
                        graph[i][j][0][1] = change_direct(graph[i][j][0][1])
                        nx = x + dx[graph[i][j][0][1]]
                        ny = y + dy[graph[i][j][0][1]]
                    x,y = nx,ny
                new_graph[x][y].append([speed,graph[i][j][0][1],size ])
    return new_graph

def eat_shark(graph):
    new_graph = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if len(graph[i][j]) == 1:
                new_graph[i][j] = graph[i][j]
            elif len(graph[i][j]) >= 2:
                temp = graph[i][j]
                temp.sort(key = lambda x:x[2])
                new_graph[i][j].append(temp[-1])
    return new_graph
dx = [-1,1,0,0]
dy = [0,0,1,-1]

r,c, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[[] for _ in range(c)] for _ in range(r)]
dict_shark = {}
for i in range(1,m+1):
    a,b,s,d,z = map(int, sys.stdin.readline().rstrip().split())
    if d-1 == 0 or d-1 == 1:
        s = s % ((r - 1) * 2)
    else:
        s = s % ((c - 1) * 2)

    graph[a-1][b-1].append([s,d-1,z])  # 속력 방향 크기


hunter_index = 0
result = 0
while 1:
    if m == 0:
        break

    hunt_shark(hunter_index)

    graph = move_shark(graph)

    graph = eat_shark(graph)

    hunter_index += 1
    if hunter_index == c:
        break

print(result)



# import copy
# import sys
#
# def hunt_shark(hunter_index):
#     global result
#     shark_list.sort(key = lambda x:x[0])
#     for i in range(len(shark_list)):
#         if shark_list[i][1] == hunter_index:
#             result += shark_list[i][4]
#             shark_list.remove(shark_list[i])
#             break
#     return shark_list
#
# def change_direct(direct):
#     if direct == 0:
#         return 1
#     elif direct == 1:
#         return 0
#     elif direct == 2:
#         return 3
#     elif direct == 3:
#         return 2
#
# def move_shark(shark_list):
#     for i in range(len(shark_list)):
#         speed = shark_list[i][2]
#         x,y = shark_list[i][0], shark_list[i][1]
#         for d in range(1, speed + 1):
#             nx = x + dx[shark_list[i][3]]
#             ny = y + dy[shark_list[i][3]]
#             if not (0 <= nx < r and 0 <= ny < c):
#                 shark_list[i][3] = change_direct(shark_list[i][3])
#                 nx = x + dx[shark_list[i][3]]
#                 ny = y + dy[shark_list[i][3]]
#             x, y = nx, ny
#         shark_list[i][0],  shark_list[i][1] = x,y
#     return shark_list
#
# def eat_shark(shark_list):
#     new_shark_list = copy.deepcopy(shark_list)
#     del_list = []
#     for i in range(len(shark_list)-1):
#         if i in del_list:
#             continue
#         max_size = shark_list[i][4]
#         for j in range(i+1, len(shark_list)):
#             if j in del_list:
#                 continue
#             if shark_list[i][0] == shark_list[j][0] and shark_list[i][1] == shark_list[j][1]:
#                 if max_size > shark_list[j][4]:
#                     new_shark_list.remove(shark_list[j])
#                     del_list.append(j)
#                 elif max_size < shark_list[j][4]:
#                     if shark_list[i] in new_shark_list:
#                         new_shark_list.remove(shark_list[i])
#                     max_size = shark_list[j][4]
#     return new_shark_list
#
# dx = [-1,1,0,0]
# dy = [0,0,1,-1]
#
# r,c, m = map(int, sys.stdin.readline().rstrip().split())
# shark_list = []
# for i in range(1,m+1):
#     x,y,s,d,z = map(int, sys.stdin.readline().rstrip().split())
#     x,y,d = x-1, y-1, d-1
#     shark_list.append([x,y,s,d,z])
#
# hunter_index = 0
# result = 0
# while 1:
#     if len(shark_list) == 0:
#         break
#     shark_list = hunt_shark(hunter_index)
#
#     if len(shark_list) == 0:
#         break
#     shark_list = move_shark(shark_list)
#
#     if len(shark_list) == 0:
#         break
#     shark_list = eat_shark(shark_list)
#
#     hunter_index += 1
#     if hunter_index == c:
#         break
#
# print(result)


