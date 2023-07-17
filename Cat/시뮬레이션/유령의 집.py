import sys
from collections import deque

def make_new_direct(direct, type):
    new_direct = -1
    if type == 1:
        if direct == 0:
            new_direct = 1
        elif direct == 1:
            new_direct = 0
        elif direct == 2:
            new_direct = 3
        elif direct == 3:
            new_direct = 2
    elif type == 2:
        if direct == 0:
            new_direct = 3
        elif direct == 1:
            new_direct = 2
        elif direct == 2:
            new_direct = 1
        elif direct == 3:
            new_direct = 0
    else:
        new_direct = direct
    return new_direct

def check_see_line(x,y,now_direct):

def cal_count_dis_gos(start_point,start_direct):
    # 원래 루틴대로 전진 해보기
    gost_count, dis_sum = 0,0
    total_len,end_direct,end_point = -1,-1,[-1,-1]
    x,y = start_point
    now_direct = start_direct

    # x,y,count,dis,direct
    q = deque()
    dis_list = []
    dis = 1

    while 1:
        # 만약 이미 계산했던 곳이야
        ori_x, ori_y = x,y
        # 지금 기준으로 아무것도 없으면, 그냥 끝으로 직진
        flag = check_see_line(x,y,now_direct)

        if graph[x][y] == -1:
            dis_sum += dis
            gost_count += 1
            dis_list.append(dis)
        elif graph[x][y] > 0:
            type = graph[x][y]
            now_direct = make_new_direct(now_direct, type)
        x = x + dx[now_direct]
        y = y + dy[now_direct]
        if not(0<=x<n and 0<=y<m):
            end_point,end_direct,total_len =[ori_x,ori_y],now_direct, dis
            break
        dis+=1
    reverse_dis_sum = sum([(total_len - dis+1) for dis in dis_list])
    return gost_count, dis_sum , end_point, end_direct, reverse_dis_sum

n,m,k,Q = map(int,sys.stdin.readline().rstrip().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    a,b,type = sys.stdin.readline().rstrip().split()
    a = int(a)-1
    b = int(b)-1
    # 유령
    if type == "!":
        graph[a][b] = -1
    # / 거울
    elif type == "/":
        graph[a][b] = 1
    # \ 거울
    elif ord(type) == 92:
        graph[a][b] = 2


# 각 방향에서 들어 왔을떄, 이미 값이 있으면, 앞으로도 그 값만 있을거임
graph_count = [[[[-1,-1] for _ in range(4)] for _ in range(m)] for _ in range(n)]


dx = [-1,0,1,0]
dy = [0,1,0,-1]
result_dict = {}
name_list = ["U","R","D","L"]
for _ in range(Q):
    input_str = sys.stdin.readline().rstrip()
    input_info = list(input_str)
    start_point = []
    start_direct = -1
    if input_info[0] == "U":
        start_point = [0,int(input_info[1])-1]
        start_direct = 2
    elif input_info[0] == "R":
        start_point = [int(input_info[1])-1, m-1]
        start_direct = 3
    elif input_info[0] == "D":
        start_point = [n-1,int(input_info[1])-1]
        start_direct = 0
    elif input_info[0] == "L":
        start_point = [int(input_info[1])-1, 0]
        start_direct = 1

    if result_dict.get(input_str):
        print(result_dict[input_str][0], result_dict[input_str][1])
    else:
        gost_count, dis_sum,end_point,end_direct,reverse_dis_sum = cal_count_dis_gos(start_point,start_direct)
        print(gost_count, dis_sum)
        result_dict[input_str] = [gost_count, dis_sum]

        other_str = name_list[end_direct]
        if end_direct == 0 or end_direct == 2:
            other_str += str(end_point[1]+1)
        else:
            other_str += str(end_point[0]+1)
        result_dict[other_str] = [gost_count, reverse_dis_sum]

"""
3 4 6 5
1 2 /
1 3 !
2 1 !
3 1 \
3 2 !
3 4 !
D2
U1
L1
R2
R1
"""

# import sys
# from collections import deque
#
# def make_new_direct(direct, type):
#     new_direct = -1
#     if type == 1:
#         if direct == 0:
#             new_direct = 1
#         elif direct == 1:
#             new_direct = 0
#         elif direct == 2:
#             new_direct = 3
#         elif direct == 3:
#             new_direct = 2
#     elif type == 2:
#         if direct == 0:
#             new_direct = 3
#         elif direct == 1:
#             new_direct = 2
#         elif direct == 2:
#             new_direct = 1
#         elif direct == 3:
#             new_direct = 0
#     else:
#         new_direct = direct
#     return new_direct
#
# def cal_count_dis_gos(start_point,start_direct):
#     # 원래 루틴대로 전진 해보기
#     gost_count, dis_sum = 0,0
#     x,y = start_point
#     now_direct = start_direct
#     dis = 1
#     # x,y,count,dis,direct
#     q = deque()
#     total_gost, total_dis = 0,0
#     dis_list = []
#     while 1:
#         # 만약 이미 계산했던 곳이야
#         ori_x, ori_y = x,y
#         if graph[x][y] == -1:
#             dis_sum += dis
#             gost_count += 1
#             dis_list.append(dis)
#             type = graph[x][y]
#             now_direct = make_new_direct(now_direct, type)
#         x = x + dx[now_direct]
#         y = y + dy[now_direct]
#
#         dis+=1
#
#         if graph_count[ori_x][ori_y][now_direct] != [-1, -1]:
#             total_gost, total_dis = gost_count, dis_sum
#             total_gost += graph_count[x][y][now_direct][0]
#             total_dis += graph_count[x][y][now_direct][1]
#             break
#         q.append([ori_x, ori_y, now_direct, dis_sum])
#         if not(0<=x<n and 0<=y<m):
#             total_gost, total_dis, end_point,end_direct,total_len = gost_count, dis_sum, [ori_x,ori_y],now_direct, dis-1
#             break
#
#     # 다시 돌아오면서, 그 길, 그 방향에서 최대값 수정
#     while q:
#         x,y,direct,dis = q.popleft()
#         graph_count[x][y][direct] = [total_gost, total_dis]
#         # 귀신이 있던 곳이면
#         total_dis -= total_gost
#         if graph[x][y] == -1:
#             if total_gost != 0:
#                 total_gost -= 1
#         if total_gost == 0:
#             total_dis = 0
#     reverse_dis_sum = sum([ (total_len - dis+1) for dis in dis_list])
#     return gost_count, dis_sum , end_point,end_direct,reverse_dis_sum
#
# n,m,k,Q = map(int,sys.stdin.readline().rstrip().split())
# graph = [[0 for _ in range(m)] for _ in range(n)]
# for _ in range(k):
#     a,b,type = sys.stdin.readline().rstrip().split()
#     a = int(a)-1
#     b = int(b)-1
#     # 유령
#     if type == "!":
#         graph[a][b] = -1
#     # / 거울
#     elif type == "/":
#         graph[a][b] = 1
#     # \ 거울
#     elif ord(type) == 92:
#         graph[a][b] = 2
#
#
# # 각 방향에서 들어 왔을떄, 이미 값이 있으면, 앞으로도 그 값만 있을거임
# graph_count = [[[[-1,-1] for _ in range(4)] for _ in range(m)] for _ in range(n)]
#
#
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# result_dict = {}
# name_list = ["U","R","D","L"]
# for _ in range(Q):
#     input_str = sys.stdin.readline().rstrip()
#     input_info = list(input_str)
#     start_point = []
#     start_direct = -1
#     if input_info[0] == "U":
#         start_point = [0,int(input_info[1])-1]
#         start_direct = 2
#     elif input_info[0] == "R":
#         start_point = [int(input_info[1])-1, m-1]
#         start_direct = 3
#     elif input_info[0] == "D":
#         start_point = [n-1,int(input_info[1])-1]
#         start_direct = 0
#     elif input_info[0] == "L":
#         start_point = [int(input_info[1])-1, 0]
#         start_direct = 1
#
#     if result_dict.get(input_str):
#         print(result_dict[input_str][0], result_dict[input_str][1])
#     else:
#         gost_count, dis_sum,end_point,end_direct,reverse_dis_sum = cal_count_dis_gos(start_point,start_direct)
#         print(gost_count, dis_sum)
#         result_dict[input_str] = [gost_count, dis_sum]
#
#         other_str = name_list[end_direct]
#         if end_direct == 0 or end_direct == 2:
#             other_str += str(end_point[1]+1)
#         else:
#             other_str += str(end_point[0]+1)
#         result_dict[other_str] = [gost_count, reverse_dis_sum]
#
# """
# 3 4 6 5
# 1 2 /
# 1 3 !
# 2 1 !
# 3 1 \
# 3 2 !
# 3 4 !
# D2
# U1
# L1
# R2
# R1
# """