from collections import defaultdict
import sys

# 100 공장 설립
def make_fac(n,m,id_list,w_list):
    for line in range(1, m+1):
        line_break[line] = 0

    # n : 박스 개수 , m : 벨트 개수
    line_max_box = n // m
    line_count = 0
    for index in range(n):
        now_id = id_list[index]
        now_weight = w_list[index]
        now_line = line_count//line_max_box + 1
        dict_line[now_id] = now_line
        # 아무 것도 없는 칸이면
        if line_head[now_line] == -1:
            dict_weight[now_id] = now_weight
            dict_next[now_id] = -1
            dict_before[now_id] = -1
            line_head[now_line] = now_id
            line_tail[now_line] = now_id

        else:
            dict_weight[now_id] = now_weight
            now_tail = line_tail[now_line]
            dict_next[now_id] = now_tail
            dict_before[now_tail] = now_id
            dict_before[now_id] = -1
            line_tail[now_line] = now_id
        line_count = line_count + 1

def reset_box_info(box_id):
    dict_line[box_id] = -1
    dict_weight[box_id] = -1
    dict_next[box_id] = -1
    dict_before[box_id] = -1

# 200 물건 하차
def down_box(w_max):
    down_sum = 0
    for now_line in range(1, m+1):
        # 고장난 벨트면 패스
        if line_break[now_line] == 1:
            continue
        # 아무것도 없으면 패스
        if line_head[now_line] == -1:
            continue
        else:
            now_head = line_head[now_line]
            now_tail = line_tail[now_line]

            now_head_before = dict_before[now_head]
            now_weight = dict_weight[now_head]

            # w_max 이하인 경우 / 하차
            if now_weight <= w_max:
                down_sum += now_weight
                # 박스 정보 삭제
                reset_box_info(now_head)

                # 뒤가 없는 경우
                if now_head_before == -1:
                    line_head[now_line] = -1
                    line_tail[now_line] = -1
                # 뒤가 있는 경우
                else:
                    line_head[now_line] = now_head_before
                    dict_next[now_head_before] = -1
            # 맨 뒤로 옮겨 주기
            else:
                # 뒤가 없는 경우
                if now_head_before == -1:
                    continue
                # 뒤가 있는 경우
                else:
                    line_head[now_line] = now_head_before
                    line_tail[now_line] = now_head
                    dict_next[now_head_before] = -1

                    dict_next[now_head] = now_tail
                    dict_before[now_tail] = now_head

                    dict_before[now_head] = -1

    return down_sum
# 300 물건 제거
def del_box(r_id):
    # 없는 박스 -> return -1
    if dict_line[r_id] == -1:
        return -1
    else:
        now_id = r_id
        now_id_next = dict_next[now_id]
        now_id_before = dict_before[now_id]

        now_line = dict_line[now_id]
        now_head = line_head[now_line]
        now_head_next = dict_next[now_head]
        now_head_before = dict_before[now_head]

        now_tail = line_tail[now_line]
        now_tail_next = dict_next[now_tail]
        now_tail_before = dict_before[now_tail]

        # box가 head  / tail 임 -> 그 라인에 박스가 1개
        if now_id == now_head and now_id == now_tail:
            reset_box_info(now_id)
            line_head[now_line] = -1
            line_tail[now_line] = -1
        # box가 head임
        elif now_id == now_head:
            reset_box_info(now_id)
            line_head[now_line] = now_id_before
            dict_next[now_id_before] = -1

        # box가 tail임
        elif now_id == now_tail:
            reset_box_info(now_id)
            line_tail[now_line] = now_id_next
            dict_before[now_id_next] = -1
        # 중간에 있는 박스
        else:
            reset_box_info(now_id)
            dict_next[now_id_before] = now_id_next
            dict_before[now_id_next] = now_id_before
        return r_id

# 400 물건 확인
def check_box(f_id):
    if dict_line[f_id] == -1:
        return -1
    else:
        now_id = f_id
        now_id_next = dict_next[now_id]
        now_id_before = dict_before[now_id]

        now_line = dict_line[now_id]
        now_head = line_head[now_line]
        now_head_next = dict_next[now_head]
        now_head_before = dict_before[now_head]

        now_tail = line_tail[now_line]
        now_tail_next = dict_next[now_tail]
        now_tail_before = dict_before[now_tail]

        # box가 head  / tail 임  // 아무 짓도 안함
        if now_id == now_head and now_id == now_tail:
            pass
        # box가 head임 // 아무 짓도 안함
        elif now_id == now_head:
            pass
        # box가 tail임 // tail 만 맨 앞으로 가져오기
        elif now_id == now_tail:
            line_head[now_line] = now_tail
            line_tail[now_line] = now_tail_next

            dict_next[now_tail] = -1
            dict_before[now_tail] = now_head
            dict_next[now_head] = now_tail

            dict_before[now_tail_next] = -1
        # 중간에 있는 박스
        else:
            move_head = now_id
            move_tail = now_tail

            move_head_next = dict_next[move_head]

            line_head[now_line] = move_head
            line_tail[now_line] = move_head_next

            dict_next[move_head] = -1
            dict_before[move_head_next] = -1
            dict_next[now_head] = move_tail
            dict_before[move_tail] = now_head
        return now_line

# 500 벨트 고장
def break_belt(b_num):
    #이미 망가짐
    if line_break[b_num] == 1:
        return -1
    else:
        line_break[b_num] = 1
        now_line = b_num

        now_head = line_head[now_line]
        now_head_next = dict_next[now_head]
        now_head_before = dict_before[now_head]

        now_tail = line_tail[now_line]
        now_tail_next = dict_next[now_tail]
        now_tail_before = dict_before[now_tail]

        # 현재 라인에 아무 것도 없음 // 이동할게 없음
        if now_head == -1:
            pass
        # 물건이 있다면
        else:
            # 지금 라인을 비워주기
            line_head[now_line] = -1
            line_tail[now_line] = -1
            for plus in range(1,m):
                new_line = (now_line + plus-1)%m + 1
                # 고장나지 않은 라인이 있다면
                if line_break[new_line] == 0:
                    now_id = now_head
                    # 라인 정보 변경
                    while 1:
                        dict_line[now_id] = new_line
                        now_id = dict_before[now_id]
                        if now_id == -1:
                            break
                    # new line 뒤에 이어 붙여 주기
                    new_line_head = line_head[new_line]
                    new_line_tail = line_tail[new_line]
                    # new_line 에 아무것도 없으면 //
                    if new_line_head == -1:
                        line_head[new_line] = now_head
                        line_tail[new_line] = now_tail
                    # new 라인에 다른게 있으며 // 뒤에 이어 붙이기
                    else:
                        dict_next[now_head] = new_line_tail
                        dict_before[new_line_tail] = now_head
                        line_tail[new_line] = now_tail
                    break
        return b_num

def show_info(turn, order):
    print("=====================")
    print("turn : ", turn, "order :", order)
    print("라인 : ", dict(dict_line))
    print("무게 : ", dict(dict_weight))
    print("다음 : ", dict(dict_next))
    print("이전 : ", dict(dict_before))
    print("머리 : ", dict(line_head))
    print("꼬리 : ", dict(line_tail))
    print("고장 : ", dict(line_break))

dict_line = defaultdict(lambda :-1)
dict_weight = defaultdict(lambda :-1)
dict_next = defaultdict(lambda :-1)
dict_before = defaultdict(lambda :-1)


line_head = defaultdict(lambda :-1)
line_tail = defaultdict(lambda :-1)
line_break = defaultdict(lambda :0)


n = int(sys.stdin.readline().rstrip())
for turn in range(1,n+1):
    input_info = list(map(int,sys.stdin.readline().rstrip().split()))
    order = input_info[0]
    # 100 공장 설립
    if order == 100:
        # n : 박스 개수 , m : 벨트 개수
        n,m = input_info[1], input_info[2]
        id_list, w_list = input_info[3:3+n], input_info[3+n:]
        make_fac(n,m,id_list,w_list)

    # 200 물건 하차
    elif order == 200:
        w_max = input_info[1]
        result = down_box(w_max)
        print(result)

    # 300 물건 제거
    elif order == 300:
        r_id = input_info[1]
        result = del_box(r_id)
        print(result)

    # 400 물건 확인
    elif order == 400:
        f_id = input_info[1]
        result = check_box(f_id)
        print(result)

    # 500 벨트 고장
    elif order == 500:
        b_num = input_info[1]
        result = break_belt(b_num)
        print(result)

    # show_info(turn, order)

"""
5
100 4 2 1 2 3 4 10 20 30 40
300 4
500 2


"""