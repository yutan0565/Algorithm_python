import sys
from collections import defaultdict

# 100 공장 설립
def make_fac(n,m,id_list,w_list):
    # n개의 선물, m개의 벨트
    line_max_box = n//m
    for i in range(n):
        now_id = id_list[i]
        now_weight = w_list[i]
        now_line = i//line_max_box + 1

        dict_line[now_id] = now_line
        dict_weight[now_id] = now_weight

        if line_head[now_line] == -1:
            dict_next[now_id] = -1
            dict_prev[now_id] = -1
            line_head[now_line] = now_id
            line_tail[now_line] = now_id
        else:
            now_tail = line_tail[now_line]
            dict_next[now_id] = now_tail
            dict_prev[now_tail] = now_id

            dict_prev[now_id] = -1
            line_tail[now_line] = now_id

def clear_box(box_id):
    dict_line[box_id] = -1
    dict_weight[box_id] = -1
    dict_next[box_id] = -1
    dict_prev[box_id] = -1

# 200 물건 하차
def down_box(w_max):
    total_down = 0
    for now_line in range(1,m+1):
        # 고장난 벨트인 경우
        if line_stop[now_line] == 1:
            continue
        # 벨트에 아무것도 없는 경우
        if line_head[now_line] == -1:
            continue
        else:
            now_head = line_head[now_line]
            now_tail = line_tail[now_line]
            prev_head = dict_prev[now_head]
            now_weight = dict_weight[now_head]
            # w_max 이하
            if now_weight <= w_max:
                total_down += now_weight
                clear_box(now_head)
                if prev_head != -1:
                    dict_next[prev_head] = -1
                    line_head[now_line] = prev_head
                else:
                    line_head[now_line] = -1
                    line_tail[now_line] = -1
            # 뒤로 보내기
            else:
                # tail == head인 경우
                if now_tail == now_head:
                    continue
                else:
                    dict_next[now_head] = now_tail
                    dict_prev[now_tail] = now_head

                    dict_prev[now_head] = -1
                    dict_next[prev_head] = -1

                    line_head[now_line] = prev_head
                    line_tail[now_line] = now_head
    return total_down
# 300 물건 제거
def del_box(r_id):
    # 물건 없으면
    if dict_line[r_id] == -1:
        return -1
    else:
        now_line = dict_line[r_id]
        now_head = line_head[now_line]
        now_tail = line_tail[now_line]

        next_del = dict_next[r_id]
        prev_del = dict_prev[r_id]
        clear_box(r_id)

        # 하나만 있던게 없어지는경우
        if r_id == now_head and r_id == now_tail:
            line_head[now_line] = -1
            line_tail[now_line] = -1
        # 헤드 인 경우
        elif r_id == now_head and r_id != now_tail:
            dict_next[prev_del] = -1
            line_head[now_line] = prev_del
        # 꼬리인 경우
        elif r_id != now_head and r_id == now_tail:
            dict_prev[next_del] = -1
            line_tail[now_line] = next_del
        # 중간에 낀거
        else:
            dict_next[prev_del] = next_del
            dict_prev[next_del] = prev_del
        return r_id

# 400 물건 확인
def check_box_info(f_id):
    # 없는 물건
    if dict_line[f_id] == -1:
        return -1
    else:
        now_line = dict_line[f_id]
        now_head = line_head[now_line]
        now_tail = line_tail[now_line]
        move_head = f_id
        next_move_head = dict_next[move_head]
        move_tail = now_tail

        # 맨 앞 물건을 확인한 경우
        if move_head == now_head:
            pass
        else:
            dict_next[move_head] = -1
            dict_prev[next_move_head] = -1
            line_head[now_line] = move_head
            line_tail[now_line] = next_move_head

            dict_prev[move_tail] = now_head
            dict_next[now_head] = move_tail
        return now_line
# 500 벨트 고장
def stop_belt(b_num):
    if line_stop[b_num] == 1:
        return -1
    else:
        now_line = b_num
        now_head = line_head[now_line]
        now_tail = line_tail[now_line]

        # 고장
        line_stop[now_line] = 1
        line_head[now_line] = -1
        line_tail[now_line] = -1

        # 옮길게 없는 경우
        if now_head == -1:
            pass
        else:
            for plus in range(1,m):
                new_line = (now_line + plus-1)%m+1
                # 고장나지 않은 라인 발견
                if line_stop[new_line] == -1:
                    new_head = line_head[new_line]
                    new_tail = line_tail[new_line]

                    # 라인 번호 변경
                    now_id = now_head
                    while 1:
                        dict_line[now_id] = new_line
                        now_id = dict_prev[now_id]
                        if now_id == -1:
                            break
                    # new에 아무 것도 없음
                    if new_head == -1:
                        line_head[new_line] = now_head
                        line_tail[new_line] = now_tail
                    else:
                        dict_next[now_head] = new_tail
                        dict_prev[new_tail] = now_head
                        line_tail[new_line] = now_tail
                    break
        return b_num

def show_info():
    print("============================")
    print("무게 : ", dict(dict_weight))
    print("라인 : ", dict(dict_line))
    print("다음 : ", dict(dict_next))
    print("이전 : ", dict(dict_prev))
    print("머리 : ", dict(line_head))
    print("꼬리 : ", dict(line_tail))
    print("정지 : ", dict(line_stop))

dict_weight = defaultdict(lambda :-1)
dict_line = defaultdict(lambda :-1)
dict_next = defaultdict(lambda :-1)
dict_prev = defaultdict(lambda :-1)

line_head = defaultdict(lambda :-1)
line_tail = defaultdict(lambda :-1)
line_stop = defaultdict(lambda :-1)

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    input_info = list(map(int,sys.stdin.readline().rstrip().split()))
    order = input_info[0]
    if order == 100:
        n,m = input_info[1],input_info[2]
        id_list,w_list = input_info[3:3+n],input_info[3+n:]
        make_fac(n,m,id_list,w_list)
    elif order == 200:
        w_max = input_info[1]
        result = down_box(w_max)
        print(result)
    elif order == 300:
        r_id = input_info[1]
        result = del_box(r_id)
        print(result)
    elif order == 400:
        f_id = input_info[1]
        result = check_box_info(f_id)
        print(result)
    elif order == 500:
        b_num = input_info[1]
        result = stop_belt(b_num)
        print(result)

"""
7
100 6 2 1 2 3 4 5 6 10 20 30 40 50 60
400 3

3
100 2 2 1 2 10 20
300 1
500 2
"""