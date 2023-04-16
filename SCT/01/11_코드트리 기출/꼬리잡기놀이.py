import copy
from collections import deque
import sys

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def find_member(head):  # 머리부터 꼬리까지 순서대로, 좌표 반환
    x = head[0]
    y = head[1]
    member_list =[[x,y]]

    while 1:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] in [2,3]:
                    if not(graph[x][y] == 1 and graph[nx][ny] == 3):
                        if [nx,ny] not in member_list:
                            x = nx
                            y = ny
                            break
        member_list.append([x,y])
        if graph[x][y] == 3:
            return member_list

def move_group(member_list):
    head_x = member_list[0][0]
    head_y = member_list[0][1]
    nx,ny,temp_x,temp_y = 0,0,0,0
    for i in range(4):
        nx = head_x + dx[i]
        ny = head_y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] in [3,4]:
                break
    new_point = []
    for member in member_list:
        temp_x , temp_y = member[0],  member[1]
        new_point.append([nx,ny])
        nx, ny  = temp_x, temp_y
        graph[temp_x][temp_y] = 4

    for i, point in enumerate(new_point):
        x = point[0]
        y = point[1]
        if i == 0:
            graph[x][y] = 1
        elif i == len(new_point) -1:
            graph[x][y] = 3
        else:
            graph[x][y] = 2

def find_all_member():
    all_member_list = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                head = [i,j]
                all_member_list.append(find_member(head))
    return all_member_list

def move():
    # 1. 머리 찾기
    all_member_list = find_all_member()
    # 각 팀을 한 칸씩 이동 하기
    for member_list in all_member_list:
        move_group(member_list)

def drow_ball(round):
    round = round % (n*4)
    direct = round // n
    if round < n:
        x, y = round, 0
    elif round < n*2:
        x, y = n-1, round%n
    elif round < n * 3:
        x, y = n-1-round%n, n-1
    elif round < n * 4:
        x, y = 0, n-1-round%n

    for _ in range(n):
        if graph[x][y] not in [0,4]:
            return [x,y]
        x = x + dx[direct]
        y = y + dy[direct]
    return [-1,-1]

def add_point(hit_member):
    all_member_list = find_all_member()
    # 각 팀을 한 칸씩 이동 하기
    for member_list in all_member_list:
        hit_index = 1
        for member in member_list:
            if member == hit_member:
                head_x, head_y = member_list[0]
                tail_x, tail_y = member_list[-1]
                graph[head_x][head_y], graph[tail_x][tail_y] = graph[tail_x][tail_y],graph[head_x][head_y]
                return hit_index*hit_index
            hit_index += 1
    return 0
n,m,k = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
result = 0

for round in range(k):
    move()
    hit_member = drow_ball(round)
    if hit_member != [-1,-1]:
        point = add_point(hit_member)
        result += point
print(result)
