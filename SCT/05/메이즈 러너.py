import copy
import sys
from collections import deque


def move_people(num):
    global total_dis

    x,y = dict_pos[num]
    next_x, next_y = -1,-1
    move_flag = False

    now_dis = abs(x-end_x) + abs(y-end_y)
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:
                new_dis = abs(nx-end_x) + abs(ny-end_y)
                if new_dis < now_dis:
                    next_x = nx
                    next_y = ny
                    move_flag = True
                    break

    # 움직일수 있는 경우
    if move_flag == True :
        total_dis += 1
        dict_pos[num] = [next_x, next_y]
        # 도착한 경우
        if [next_x,next_y] == [end_x,end_y]:
            escape_list[num] = 0
            dict_pos[num] = [-1,-1]

def find_square_point():
    for size in range(1, n):
        # 시작 점 설정
        for i in range(n):
            for j in range(n):
                x1,y1,x2,y2 = i,j,i+size,j+size
                # 모든 좌표가 범위 안에 있음
                if 0<=x1<n and 0<=y1<n and 0<=x2<n and 0<=y2<n:
                    # 끝점이 좌표 안에 있나 확인
                    if x1<=end_x<=x2 and y1<=end_y<=y2:
                        # 사람이 들어 있는지 확인
                        in_flag = False
                        in_list = []
                        for num in range(1,m+1):
                            if escape_list[num] == 1:
                                a,b = dict_pos[num]
                                if x1 <= a <= x2 and y1 <= b <= y2:
                                    in_flag = True
                                    in_list.append(num)
                        if in_flag == True:
                            return x1,y1,x2,y2,size+1,in_list

def rotate_right_down(x1,y1,x2,y2,size,in_list):
    global graph,dict_pos, end_x, end_y
    new_graph = copy.deepcopy(graph)

    for i in range(size):
        for j in range(size):
            new_graph[x1+j][y1+size-1-i] = graph[x1+i][y1+j]
            if new_graph[x1+j][y1+size-1-i] != 0:
                new_graph[x1 + j][y1 + size - 1 - i] -= 1
    # 사람 좌표 돌리기
    for num in in_list:
        x,y = dict_pos[num]
        x = x - x1
        y = y - y1
        nx = x1+y
        ny = y1+size-1-x
        dict_pos[num] = [nx,ny]

    # end 좌표 돌리기
    end_x = end_x - x1
    end_y =  end_y - y1
    new_end_x = x1 +end_y
    new_end_y = y1+size-1-end_x
    end_x,end_y = new_end_x,new_end_y

    graph = new_graph

def simulation():
    # print("=============")
    # for g in graph:
    #     print(g)
    # print(dict_pos)
    for turn in range(1, k+1):
        # 모든 참가자 이동
        for num in range(1,m+1):
            if escape_list[num] == 1:
                move_people(num)
        # 모두 탈출하면 끝
        if sum(escape_list) == 0:
            return

        # 미로 회전
        # 끝점 참기
        x1,y1,x2,y2,size,in_list = find_square_point()
        # 해당 블록 돌리기 / 내구도 감소
        rotate_right_down(x1,y1,x2,y2,size,in_list)

        # print("=============", turn, "=============")
        # for g in graph:
        #     print(g)
        # print(dict_pos)
        # print("끝점 : ", [end_x,end_y])
        # print("total dis : ", total_dis)
        # print("탈출 : ", escape_list[1:])


n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
escape_list = [0] + [1 for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

total_dis = 0
dict_pos = {}
for num in range(1,m+1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    dict_pos[num] = [a-1,b-1]
end_x,end_y = map(int,sys.stdin.readline().rstrip().split())
end_x,end_y = end_x-1, end_y-1

simulation()

print(total_dis)
print(end_x+1,end_y+1)
