import sys

# 100 공장 설립
def make_fac(n,m,list_belt):
    for i in range(1, n+1):
        line_head[i] = -1
        line_tail[i] = -1
        line_count[i] = 0
    for i in range(m):
        id = i+1
        now_line = list_belt[i]
        line_count[now_line] += 1
        # 아무것도 없는 경우
        if line_head[now_line] == -1:
            next[id] = -1
            before[id] = -1
            line_head[now_line] = id
            line_tail[now_line] = id
        # 다른 물건이 있는 경우
        else:
            next[id] = line_tail[now_line]
            before[line_tail[now_line]] = id
            before[id] = -1
            line_tail[now_line] = id

# 200 물건 모두 옮기기   src 에 벨트에 있는 모든 물건을 dst로 옮기기
def move_all_obj(m_src, m_dst):
    # m_src 벨트에 아무것도 없으면, 그냥 끝
    if line_head[m_src] == -1:
        pass
    # 옮길 선물이 있으면,  지금 라인에 있는 제품들은, m_dst의 앞으로 옮기기
    else:
        # 옮길꺼 정보
        move_head = line_head[m_src]
        move_tail = line_tail[m_src]

        # 목적지 정보
        des_head = line_head[m_dst]
        des_tail = line_tail[m_dst]

        # 꼬리랑 머리 이어주기
        before[move_tail] = des_head
        next[des_head] = move_tail

        # line 정보 업데이트
        line_head[m_dst] = move_head
        if line_count[m_dst] == 0:
            line_tail[m_dst] = move_tail
        line_head[m_src] = -1
        line_tail[m_src] = -1

        line_count[m_dst] += line_count[m_src]
        line_count[m_src] = 0
    return line_count[m_dst]


# 300 앞 물건만 교체 하기
def move_front_obj(m_src, m_dst):
    # 둘다 없는 경우
    if line_head[m_src] == -1 and line_head[m_dst] == -1:
        pass
    # src 에 물건이 없는 경우
    elif line_head[m_src] == -1:
        move_id = line_head[m_dst]
        move_id_before = before[move_id]
        # dst에 있던거,  src로 옮겨 주기
        before[move_id] = -1
        next[move_id] = -1

        # dst의 앞부분 처리
        if move_id_before == -1:
            line_head[m_dst] = -1
            line_tail[m_dst] = -1
        else:
            line_head[m_dst] = move_id_before
        next[move_id_before] = -1
        line_head[m_src] = move_id
        line_tail[m_src] = line_head[m_src]

        line_count[m_src] += 1
        line_count[m_dst] -= 1

    # dst에 물건이 없는 경우
    elif line_head[m_dst] == -1:
        move_id = line_head[m_src]
        move_id_before = before[move_id]
        # src로 있던거,  dst로 옮겨 주기
        before[move_id] = -1
        next[move_id] = -1

        # src 앞부분 처리
        # 옮기는 쪽에 1개만 남아있는 경우
        if move_id_before == -1:
            line_head[m_src] = -1
            line_tail[m_src] = -1
        else:
            line_head[m_src] = move_id_before
        next[move_id_before] = -1
        line_head[m_dst] = move_id
        line_tail[m_dst] = line_head[m_dst]

        line_count[m_dst] += 1
        line_count[m_src] -= 1
    # 둘다 있는 경우
    else:
        src_head_id = line_head[m_src]
        dst_head_id = line_head[m_dst]
        src_before_id = before[line_head[m_src]]
        dst_before_id = before[line_head[m_dst]]

        next[src_head_id], next[dst_head_id] = next[dst_head_id],next[src_head_id]
        before[src_head_id], before[dst_head_id] = before[dst_head_id],before[src_head_id]
        line_head[m_src], line_head[m_dst] = line_head[m_dst],line_head[m_src]
        if line_count[m_src] == 1:
            line_tail[m_src] = line_head[m_src]
        else:
            next[src_before_id] = dst_head_id

        if line_count[m_dst] == 1:
            line_tail[m_dst] = line_head[m_dst]
        else:
            next[dst_before_id] = src_head_id

    return line_count[m_dst]

# 400 물건 나누기
def divide_obj(m_src, m_dst):
    count_cut = int(line_count[m_src] /2)
    if count_cut == 0:
        return line_count[m_dst]

    move_start_id = line_head[m_src]

    move_last_id = 0
    now_id = move_start_id
    count = 0
    while 1:
        count += 1
        if count == count_cut:
            move_last_id = now_id
            break
        now_id = before[now_id]
    before_last_id = before[move_last_id]

    # 옮기는거 처음과 끝 바꾸기
    next[move_start_id] = -1
    before[move_last_id] = line_head[m_dst]
    # 옮기는 곳이 빈곳이 아니라면, 기존에 있던거의 next가 옮기는거의 tail
    if line_head[m_dst] != -1:
        next[line_head[m_dst]] = move_last_id

    next[before_last_id] = -1
    line_head[m_src] = before_last_id

    line_head[m_dst] = move_start_id
    if line_count[m_dst] == 0:
        line_tail[m_dst] = move_last_id

    line_count[m_src] -= count_cut
    line_count[m_dst] += count_cut

    return line_count[m_dst]

# 500 선물 정보 얻기
def get_info_obj(p_num):
    a,b = next[p_num], before[p_num]
    temp = a + 2*b
    return temp

# 600 벨트 정보 얻기
def get_info_belt(b_num):
    a,b,c = line_head[b_num], line_tail[b_num], line_count[b_num]
    temp = a + 2*b + 3*c
    return temp

def show_dict():
    print("-----------------------------------------------")
    print("다음 : ", next)
    print("이전 : ", before)
    print("헤드 : ", line_head)
    print("테일 : ", line_tail)
    print("개수 : ", line_count)
    print("-----------------------------------------------")
    pass

next = {}
before = {}

line_head = {}
line_tail = {}
line_count = {}

round = int(sys.stdin.readline().rstrip())
for aa in range(round):
    input_order = list(map(int,sys.stdin.readline().rstrip().split()))
    order = input_order[0]
    if order == 100:
        n,m = input_order[1], input_order[2]
        list_belt = input_order[3:]
        make_fac(n,m,list_belt)
    elif order == 200:
        m_src, m_dst = input_order[1], input_order[2]
        result = move_all_obj(m_src, m_dst)
        print(result)
    elif order == 300:
        m_src, m_dst = input_order[1], input_order[2]
        result = move_front_obj(m_src, m_dst)
        print(result)
    elif order == 400:
        m_src, m_dst = input_order[1], input_order[2]
        result = divide_obj(m_src, m_dst)
        print(result)
    elif order == 500:
        p_num = input_order[1]
        result = get_info_obj(p_num)
        print(result)
    elif order == 600:
        b_num = input_order[1]
        result = get_info_belt(b_num)
        print(result)
    # print("round : ", aa+1, "order : ", order)
    # show_dict()




"""
2
100 2 2 1 1
300 1 2


9
100 4 4 4 1 4 4
500 4
200 4 2
300 2 1
300 4 2
300 1 4
500 4
200 3 2
500 1
"""


# import sys
#
# # 100 공장 설립
# def make_fac(n,m,list_belt):
#     for i in range(1, n+1):
#         line_head[i] = -1
#         line_tail[i] = -1
#         line_count[i] = 0
#     for i in range(m):
#         id = i+1
#         now_line = list_belt[i]
#         line[id] = now_line
#         line_count[now_line] += 1
#         # 아무것도 없는 경우
#         if line_head[now_line] == -1:
#             next[id] = -1
#             before[id] = -1
#             line_head[now_line] = id
#             line_tail[now_line] = id
#         # 다른 물건이 있는 경우
#         else:
#             next[id] = line_tail[now_line]
#             before[line_tail[now_line]] = id
#             before[id] = -1
#             line_tail[now_line] = id
#
# # 200 물건 모두 옮기기   src 에 벨트에 있는 모든 물건을 dst로 옮기기
# def move_all_obj(m_src, m_dst):
#     # m_src 벨트에 아무것도 없으면, 그냥 끝
#     if line_head[m_src] == -1:
#         pass
#     # 옮길 선물이 있으면,  지금 라인에 있는 제품들은, m_dst의 앞으로 옮기기
#     else:
#         # 옮길꺼 정보
#         move_head = line_head[m_src]
#         move_tail = line_tail[m_src]
#
#         # 목적지 정보
#         des_head = line_head[m_dst]
#         des_tail = line_tail[m_dst]
#
#         # 라인 정보 변경
#         now_id = move_head
#         while 1:
#             line[now_id] = m_dst
#             now_id = before[now_id]
#             if now_id == -1:
#                 break
#
#         # 꼬리랑 머리 이어주기
#         before[move_tail] = des_head
#         next[des_head] = move_tail
#
#         # line 정보 업데이트
#         line_head[m_dst] = move_head
#         if line_count[m_dst] == 0:
#             line_tail[m_dst] = move_tail
#         line_head[m_src] = -1
#         line_tail[m_src] = -1
#
#         line_count[m_dst] += line_count[m_src]
#         line_count[m_src] = 0
#     return line_count[m_dst]
#
#
# # 300 앞 물건만 교체 하기
# def move_front_obj(m_src, m_dst):
#     # 둘다 없는 경우
#     if line_head[m_src] == -1 and line_head[m_dst] == -1:
#         pass
#     # src 에 물건이 없는 경우
#     elif line_head[m_src] == -1:
#         move_id = line_head[m_dst]
#         move_id_before = before[move_id]
#         # dst에 있던거,  src로 옮겨 주기
#         before[move_id] = -1
#         next[move_id] = -1
#         line[move_id] = m_src
#
#         # dst의 앞부분 처리
#         if move_id_before == -1:
#             line_head[m_dst] = -1
#             line_tail[m_dst] = -1
#         else:
#             line_head[m_dst] = move_id_before
#         next[move_id_before] = -1
#         line_head[m_src] = move_id
#         line_tail[m_src] = line_head[m_src]
#
#         line_count[m_src] += 1
#         line_count[m_dst] -= 1
#
#     # dst에 물건이 없는 경우
#     elif line_head[m_dst] == -1:
#         move_id = line_head[m_src]
#         move_id_before = before[move_id]
#         # src로 있던거,  dst로 옮겨 주기
#         before[move_id] = -1
#         next[move_id] = -1
#         line[move_id] = m_dst
#
#         # src 앞부분 처리
#         # 옮기는 쪽에 1개만 남아있는 경우
#         if move_id_before == -1:
#             line_head[m_src] = -1
#             line_tail[m_src] = -1
#         else:
#             line_head[m_src] = move_id_before
#         next[move_id_before] = -1
#         line_head[m_dst] = move_id
#         line_tail[m_dst] = line_head[m_dst]
#
#         line_count[m_dst] += 1
#         line_count[m_src] -= 1
#     # 둘다 있는 경우
#     else:
#         src_head_id = line_head[m_src]
#         dst_head_id = line_head[m_dst]
#         src_before_id = before[line_head[m_src]]
#         dst_before_id = before[line_head[m_dst]]
#
#         line[src_head_id], line[dst_head_id] = line[dst_head_id],line[src_head_id]
#         next[src_head_id], next[dst_head_id] = next[dst_head_id],next[src_head_id]
#         before[src_head_id], before[dst_head_id] = before[dst_head_id],before[src_head_id]
#         line_head[m_src], line_head[m_dst] = line_head[m_dst],line_head[m_src]
#         if line_count[m_src] == 1:
#             line_tail[m_src] = line_head[m_src]
#         else:
#             next[src_before_id] = dst_head_id
#
#         if line_count[m_dst] == 1:
#             line_tail[m_dst] = line_head[m_dst]
#         else:
#             next[dst_before_id] = src_head_id
#
#     return line_count[m_dst]
#
# # 400 물건 나누기
# def divide_obj(m_src, m_dst):
#     count_cut = int(line_count[m_src] /2)
#     if count_cut == 0:
#         return line_count[m_dst]
#
#     move_start_id = line_head[m_src]
#
#     move_last_id = 0
#     now_id = move_start_id
#     count = 0
#     while 1:
#         count += 1
#         line[now_id] = m_dst
#         if count == count_cut:
#             move_last_id = now_id
#             break
#         now_id = before[now_id]
#
#     before_last_id = before[move_last_id]
#
#     # 옮기는거 처음과 끝 바꾸기
#     next[move_start_id] = -1
#     before[move_last_id] = line_head[m_dst]
#     # 옮기는 곳이 빈곳이 아니라면, 기존에 있던거의 next가 옮기는거의 tail
#     if line_head[m_dst] != -1:
#         next[line_head[m_dst]] = move_last_id
#
#     next[before_last_id] = -1
#     line_head[m_src] = before_last_id
#
#     line_head[m_dst] = move_start_id
#     if line_count[m_dst] == 0:
#         line_tail[m_dst] = move_last_id
#
#     line_count[m_src] -= count_cut
#     line_count[m_dst] += count_cut
#
#     return line_count[m_dst]
#
# # 500 선물 정보 얻기
# def get_info_obj(p_num):
#     a,b = next[p_num], before[p_num]
#     temp = a + 2*b
#     return temp
#
# # 600 벨트 정보 얻기
# def get_info_belt(b_num):
#     a,b,c = line_head[b_num], line_tail[b_num], line_count[b_num]
#     temp = a + 2*b + 3*c
#     return temp
#
# def show_dict():
#     print("-----------------------------------------------")
#     print("라인 : ", line)
#     print("다음 : ", next)
#     print("이전 : ", before)
#     print("헤드 : ", line_head)
#     print("테일 : ", line_tail)
#     print("개수 : ", line_count)
#     print("-----------------------------------------------")
#     pass
#
# next = {}
# before = {}
# line = {}
#
# line_head = {}
# line_tail = {}
# line_count = {}
#
# round = int(sys.stdin.readline().rstrip())
# for aa in range(round):
#     input_order = list(map(int,sys.stdin.readline().rstrip().split()))
#     order = input_order[0]
#     if order == 100:
#         n,m = input_order[1], input_order[2]
#         list_belt = input_order[3:]
#         make_fac(n,m,list_belt)
#     elif order == 200:
#         m_src, m_dst = input_order[1], input_order[2]
#         result = move_all_obj(m_src, m_dst)
#         print(result)
#     elif order == 300:
#         m_src, m_dst = input_order[1], input_order[2]
#         result = move_front_obj(m_src, m_dst)
#         print(result)
#     elif order == 400:
#         m_src, m_dst = input_order[1], input_order[2]
#         result = divide_obj(m_src, m_dst)
#         print(result)
#     elif order == 500:
#         p_num = input_order[1]
#         result = get_info_obj(p_num)
#         print(result)
#     elif order == 600:
#         b_num = input_order[1]
#         result = get_info_belt(b_num)
#         print(result)
#     # print("round : ", aa+1, "order : ", order)
#     # show_dict()
#
#
#
#
# """
# 2
# 100 2 2 1 1
# 300 1 2
#
#
# 9
# 100 4 4 4 1 4 4
# 500 4
# 200 4 2
# 300 2 1
# 300 4 2
# 300 1 4
# 500 4
# 200 3 2
# 500 1
# """