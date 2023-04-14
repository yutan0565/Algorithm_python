import copy
import sys

def move_people():
    for num in range(1, m + 1):
        if list_live[num] == 1:
            x,y = dict_pos[num]
            distance = abs(x - end_point[0]) + abs(y - end_point[1])
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 0:
                        new_distance = abs(nx - end_point[0]) + abs(ny - end_point[1])
                        if new_distance < distance:
                            dict_move_len[num] += 1
                            if [nx,ny] == end_point:
                                list_live[num] = 0
                                dict_pos[num] = [-2,-2]
                            else:
                                dict_pos[num] = [nx, ny]
                            break

def find_rotation_block():
    for line_size in range(2, n+1):
        for i in range(n):
            for j in range(n):
                s_x, s_y, e_x, e_y = i,j,i+line_size-1, j+line_size-1
                if not(0<=e_x<n and 0<=e_y<n):
                    continue
                if s_x <= end_point[0] <= e_x and s_y <= end_point[1] <= e_y:
                    for num in range(1,m+1):
                        if list_live[num] == 1:
                            x,y = dict_pos[num]
                            if s_x <= x <= e_x and s_y <= y <= e_y:
                                return s_x, s_y, e_x, e_y

def rotation_block_right(s_x, s_y, e_x, e_y ):
    new_graph = copy.deepcopy(graph)
    line_size = e_x - s_x +1
    for i in range(line_size):
        for j in range(line_size):
            if s_x<=s_x+i<=e_x and s_y<=s_y+j<=e_y:
                if graph[s_x+i][s_y+j] != 0:
                    graph[s_x+i][s_y+j] -= 1
                new_graph[s_x + j][s_y+line_size-1-i] = graph[s_x+i][s_y+j]
    return new_graph

def rotation_people(s_x, s_y, e_x, e_y):
    line_size = e_x - s_x + 1
    for num in range(1,m+1):
        if list_live[num] == 1:
            x,y = dict_pos[num]
            if s_x <= x <= e_x and s_y <= y <= e_y:
                new_x = s_x + y-s_y
                new_y = s_y+line_size-1-(x-s_x)
                dict_pos[num] = [new_x,new_y]

def rotation_end(s_x, s_y, e_x, e_y ):
    global end_point
    line_size = e_x - s_x + 1
    x, y = end_point
    new_x = s_x + y - s_y
    new_y = s_y + line_size - 1 - (x - s_x)
    end_point = [new_x, new_y]

n,m,k = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dict_pos = {}
dict_move_len = {}
dict_distance = {}
dict_load = {}
list_live = [0 for _ in range(m+1)]

for num in range(1,m+1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    a,b = a-1,b-1
    dict_pos[num] = [a,b]
    dict_move_len[num] = 0
    list_live[num] = 1

end_point = list(map(int,sys.stdin.readline().rstrip().split()))
end_point = [end_point[0]-1,end_point[1]-1]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for round in range(1,k+1):
    # 한칸씩 움직이기
    move_people()
    # 모든 애들이 탈출함
    if sum(list_live) == 0:
        break
    # 돌릴 블럭 찾기
    s_x, s_y, e_x, e_y = find_rotation_block()
    # 블럭 돌리기
    graph = rotation_block_right(s_x, s_y, e_x, e_y)
    # 사람 돌리기
    rotation_people(s_x, s_y, e_x, e_y )
    # 출구 돌리기
    rotation_end(s_x, s_y, e_x, e_y )
    # print("round : ",round)
    # for g in graph:
    #     print(g)
    # print([s_x, s_y, e_x, e_y])
    # print(dict_pos)
    # print(list_live)
    # print(end_point)
    # print(dict_move_len)

result = sum(dict_move_len.values())
print(result)
print(end_point[0]+1, end_point[1]+1)
"""
5 3 8
0 0 0 0 1
9 2 2 0 0
0 0 0 1 0
0 0 0 1 0
0 0 0 0 0
1 3
3 1
3 5
3 3
"""