import sys

# 공장 설립 100
def make_fac(n,m,id_list, weight_list):
    # m 개 벨트, n개 선물
    # 초기화
    # 라인 정보
    id_base = 0
    box_line = n // m
    for now_line in range(1, m+1):
        line_head[now_line] = -1
        line_tail[now_line] = -1
        line_stop[now_line] = 0
        for i in range(box_line):
            id = id_list[id_base+ i]
            list_id.append(id)
            dict_weight[id] = weight_list[id_base+ i]
            # 아직 아무 것도 없는 경우
            if line_head[now_line] == -1 and line_tail[now_line] == -1:
                dict_next[id] = -1
                dict_before[id] = -1
                dict_line[id] = now_line

                line_head[now_line] = id
                line_tail[now_line] = id
            # 다른 물건이 있는 경우
            else:
                # 새로운 id를, 그 라인 tail에 연결하기
                dict_next[id] = line_tail[now_line]
                dict_before[line_tail[now_line]] = id
                dict_before[id] = -1
                dict_line[id] = now_line
                line_tail[now_line] = id
        id_base += box_line

def reset_id_info(id):
    dict_weight[id] = -1
    dict_line[id] = -1
    dict_next[id] = -1
    dict_before[id] = -1
    list_id.remove(id)

# 물건 하차 200
def down_box(w_max):
    down_sum = 0
    for line in range(1, m + 1):
        if line_stop[line] == 1:
            continue
        now_head = line_head[line]
        # 아무것도 없으면 패스
        if now_head == -1:
            continue
        else:
            now_weight = dict_weight[now_head]
            # w_max 이하 - 하차
            if now_weight <= w_max:
                before_id = dict_before[now_head]
                down_sum += now_weight
                # 정보 초기화
                reset_id_info(now_head)
                # 이전 노드가 있으면
                if before_id != -1:
                    dict_next[before_id] = -1
                    line_head[line] = before_id
                # 이전 노드가 없으면
                else:
                    line_head[line] = -1
                    line_tail[line] = -1
            # w_max 보다 크면, 맨 뒤로 보내야함
            else:
                before_id = dict_before[now_head]
                # 이전 노드가 있으면
                if before_id != -1:
                    ori_tail = line_tail[line]
                    dict_next[now_head] = line_tail[line]
                    dict_before[now_head] = -1
                    dict_before[ori_tail] = now_head

                    dict_next[before_id] = -1
                    line_head[line] = before_id
                    line_tail[line] = now_head
                # 이전 노드가 없으면 / 아무것도 안함
                else:
                    continue
    return down_sum

# 물건 제거 300
def del_box(r_id):
    # 상자 없으면
    if r_id not in list_id:
        return -1
    # 상자 있는 경우
    else:
        now_line = dict_line[r_id]
        next_id = dict_next[r_id]
        before_id = dict_before[r_id]

        # 노드 정보 지우기
        reset_id_info(r_id)

        # 기존 노드간 연결
        # 앞뒤에 다른게 있음 // 중간임
        if next_id != -1 and before_id != -1:
            dict_next[before_id] = next_id
            dict_before[next_id] = before_id
        # 앞에만 다른게 없음 // 헤드임
        elif next_id == -1 and before_id != -1:
            dict_next[before_id] = -1
            line_head[now_line] = before_id
        # 뒤에만 다른게 없음 // 테일임
        elif next_id != -1 and before_id == -1:
            dict_before[next_id] = -1
            line_tail[now_line] = next_id
        # 둘다 없음 // 혼자임
        else:
            line_head[now_line] = -1
            line_tail[now_line] = -1

        return r_id

# 물건 확인 400
def check_box(f_id):
    # 상자 없으면
    if f_id not in list_id:
        return -1
    else:
        now_line = dict_line[f_id]
        move_head = f_id
        move_tail = line_tail[now_line]

        if move_head == line_head[now_line]:
            return now_line
        # 다음이 있다면 (옮기는게 헤드가 아니면)
        else:
            next_move_head = dict_next[move_head]
            ori_head = line_head[now_line]

            # move_head 부분 변경
            dict_next[move_head] = -1
            dict_before[next_move_head] = -1

            # move_tail 변경
            dict_before[move_tail] = ori_head
            dict_next[ori_head] = move_tail

            # 라인 정보 변경
            line_tail[now_line] = next_move_head
            line_head[now_line] = move_head

            return now_line

# 벨트 고장 500
def stop_belt(b_num):
    if line_stop[b_num] == 1:
        return -1
    line_stop[b_num] = 1
    # 아무 것도 없음
    if line_head[b_num] == -1:
        return -1
    # 물건이 있는 경우
    else:
        now_line = b_num
        for i in range(1, m):
            check_line = (now_line + i - 1) % m + 1
            #고장나지 않은 곳이면  // 모든 상자 옮기기
            if line_stop[check_line] == 0 :
                # 옮길 곳의 tail 정보
                dst_tail = line_tail[check_line]
                # 옮길 것의 head, tail
                move_head = line_head[now_line]
                move_tail = line_tail[now_line]

                line_head[now_line] = -1
                line_tail[now_line] = -1

                # 라인 번호 바꿔 주기
                now_id = move_head

                while 1:
                    print("ddd : ", now_id)
                    dict_line[now_id] = check_line
                    before_id = dict_before[now_id]
                    if before_id == -1:
                        break
                    now_id = before_id
                # move_head 수정
                dict_next[move_head] = dst_tail
                # 옮기는 곳에 물건이 있다면
                if dst_tail != -1:
                    dict_before[dst_tail] = move_head
                # 물건이 없다면
                else:
                    line_head[check_line] = move_head

                # move_tail 수정
                dict_before[move_tail] = -1
                line_tail[check_line] = move_tail
                return b_num


dict_weight = {}
dict_line = {}
dict_next = {}
dict_before = {}
list_id = []

line_head = {}
line_tail = {}
line_stop = {}

def show_info(order):
    print("order : ", order)
    print("무게 : ", dict_weight)
    print("라인 : ", dict_line)
    print("다음 : ", dict_next)
    print("전 : ", dict_before)
    print("헤드 : ", line_head)
    print("꼬리 : ", line_tail)
    print("고장 : ", line_stop)

n = int(sys.stdin.readline().rstrip())
for round in range(1, n+1):
    order_list = list(map(int,sys.stdin.readline().rstrip().split()))
    order = order_list[0]
    if order == 100:
        # 선물 / 벨트
        n,m = order_list[1], order_list[2]
        id_list = order_list[3:3+n]
        weight_list = order_list[3+n:]
        make_fac(n,m,id_list, weight_list)

    elif order == 200:
        w_max = order_list[1]
        result = down_box(w_max)
        print(result)

    elif order == 300:
        r_id = order_list[1]
        result = del_box(r_id)
        print(result)

    elif order == 400:
        f_id = order_list[1]
        result = check_box(f_id)
        print(result)

    elif order == 500:
        b_num = order_list[1]
        result = stop_belt(b_num)
        print(result)
    show_info(order)

"""
7
100 12 3 10 12 20 15 14 19 22 25 16 17 21 18 30 30 20 20 10 18 17 15 25 11 14 17
200 25
300 22
300 999
400 14
400 18
500 3


5
100 4 2 1 2 3 4 10 20 30 40
300 1
200 30
300 4
500 2

"""