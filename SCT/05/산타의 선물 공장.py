import sys
from collections import defaultdict

class BOX():
    def __init__(self):
        self.weight = -1
        self.front = -1
        self.back = -1
        self.line = -1

def append_box(line, box_id):
    # 아무것도 없는 경우
    if dict_head[line] == -1:
        # 머리와 꼬리 동시에 됨
        dict_head[line] = box_id
        dict_tail[line] = box_id
    # 다른게 있는 경우
    else:
        now_tail = dict_tail[line]
        # 꼬리 정보 바꾸기
        dict_tail[line] = box_id
        # 앞뒤 업데이트
        dict_box[now_tail].back = box_id
        dict_box[box_id].front = now_tail


# 공장 설립
def make_factory(n,m,id_info,weight_info):
    # 한개의 라인에 들어갈 박스의 수
    one_line_box_cnt = n//m
    for line_num in range(m):
        for i in range(one_line_box_cnt):
            index = line_num*one_line_box_cnt + i
            now_id = id_info[index]
            now_weight = weight_info[index]
            now_line = line_num
            # 박스 정보 넣어주기
            dict_box[now_id].weight = now_weight
            dict_box[now_id].line = now_line

            # 박스를 줄에 넣어주기
            append_box(now_line, now_id)

def remove_box(box_id):
    front_box_id = dict_box[box_id].front
    back_box_id = dict_box[box_id].back
    now_line = dict_box[box_id].line

    # 하나만 남아 있는 경우
    if front_box_id == -1 and back_box_id == -1:
        dict_head[now_line] = -1
        dict_tail[now_line] = -1
        dict_box[box_id].weight = -1
        dict_box[box_id].line = -1
    # 지금 머리인 경우
    elif front_box_id == -1:
        dict_head[now_line] = back_box_id
        dict_box[back_box_id].front = -1
        dict_box[box_id].back = -1
        dict_box[box_id].weight = -1
        dict_box[box_id].line = -1
    # 지금 꼬리인 경우
    elif back_box_id == -1:
        dict_tail[now_line] = front_box_id
        dict_box[front_box_id].back = -1
        dict_box[box_id].front = -1
        dict_box[box_id].weight = -1
        dict_box[box_id].line = -1
    # 중간에 있는 경우
    else:
        dict_box[box_id].front = -1
        dict_box[box_id].back = -1
        dict_box[box_id].weight = -1
        dict_box[box_id].line = -1

        dict_box[front_box_id].back = back_box_id
        dict_box[back_box_id].front = front_box_id

def go_back(box_id):
    front_box_id = dict_box[box_id].front
    back_box_id = dict_box[box_id].back
    now_line = dict_box[box_id].line
    now_tail = dict_tail[now_line]

    # 하나만 남아 있는 경우
    if front_box_id == -1 and back_box_id == -1:
        pass
    # 다른게 있는 경우
    else:
        # 머리 업데이트
        dict_head[now_line] = back_box_id
        dict_box[back_box_id].front = -1
        dict_box[box_id].back = -1

        # 꼬리 업데이트
        dict_tail[now_line] = box_id
        dict_box[now_tail].back = box_id
        dict_box[box_id].front = now_tail

# 물건 하차
def down_box(w_max):
    total_down = 0
    # 각 벨트의 맨 앞 만 확인, 맨앞 무게가 w_max 이하면 하차, 아니면 맨뒤로 보내기
    for line_num in range(m):
        # 고장난 곳이면 패스
        if dict_line_stat[line_num] == 0:
            continue
        # 아무것도 없는 경우, 패스
        if dict_head[line_num] == -1:
            continue
        # 다른게 있는 경우 진행
        else:
            # w_max보다 작은 경우, 하차
            now_box = dict_head[line_num]
            if dict_box[now_box].weight <= w_max:
                total_down += dict_box[now_box].weight
                remove_box(now_box)
            # 뒤로 보내기
            else:
                go_back(now_box)
    return total_down
# 물건 제거
def del_box(r_id):
    # 이미 제거된 박스인 경우, -1 반환
    if dict_box[r_id].line == -1:
        return -1
    else:
        remove_box(r_id)
        return r_id

# 물건 확인
def check_box(f_id):
    # 이미 제거된 박스인 경우, -1 반환
    if dict_box[f_id].line == -1:
        return -1
    else:
        # 한개만 있는 경우, 고른게 head인 경우 끝
        if dict_box[f_id].front == -1:
            return f_id
        else:
            # f_id 를 head로, 현재 tail을 기존 head에 연결
            now_line = dict_box[f_id].line
            now_head = dict_head[now_line]
            now_tail = dict_tail[now_line]

            front_box_id = dict_box[f_id].front

            # 지금 꼬리를, 기존 머리와 연결
            dict_box[now_tail].back = now_head
            dict_box[now_head].front = now_tail

            # 꼬리 뒤, 머리 앞 처리
            dict_box[front_box_id].back = -1
            dict_box[f_id].front = -1

            # 머리꼬리 변경
            dict_head[now_line] = f_id
            dict_tail[now_line] = front_box_id
            return now_line+1

# 벨트 고장
def broken_belt(b_num):
    # 이미 고장난 벨트는 패스
    now_line = b_num - 1
    if dict_line_stat[now_line] == 0:
        return -1
    else:
        # 고장 나기
        dict_line_stat[now_line] = 0
        # 아무것도 없는 경우 끝
        if dict_head[now_line] == -1:
            pass
        else:
            for i in range(1,m):
                new_line = (now_line + i)%m
                # 고장난 라인이면 다음
                if dict_line_stat[new_line] == 0:
                    continue
                # 멀쩡한 라인이면 옮기기
                else:
                    now_head = dict_head[now_line]
                    now_tail = dict_tail[now_line]

                    new_head = dict_head[new_line]
                    new_tail = dict_tail[new_line]

                    # 기존 라인 번호 바꾸기
                    now_node = now_head
                    while 1:
                        back_node = dict_box[now_node].back
                        dict_box[now_node].line = new_line
                        if back_node == -1:
                            break
                        else:
                            now_node = back_node
                    # 라인 정보 지우기
                    dict_head[now_line] = -1
                    dict_tail[now_line] = -1

                    # 옮기는 곳에 아무것도 없는 경우
                    if new_head == -1:
                        dict_head[new_line] = now_head
                        dict_tail[new_line] = now_tail
                    else:
                        # 머리 부분 연결
                        dict_box[now_head].front = new_tail
                        dict_box[new_tail].back = now_head
                        # 꼬리 연결
                        dict_box[now_tail].back = -1
                        # 꼬리 정보 변경
                        dict_tail[new_line] = now_tail
                    break
        return b_num

def show_info(turn):
    print("=====================", turn,"==============")
    print("박스 정보")
    for num in dict_box.keys():
        print("id : {}, weight : {} , front : {}, back : {} , line : {}".format(num, dict_box[num].weight, dict_box[num].front, dict_box[num].back, dict_box[num].line))
    print("머리 : ", dict(dict_head))
    print("꼬리 : ", dict(dict_tail))
    print("상태 : ", dict(dict_line_stat))



order_q = int(sys.stdin.readline().rstrip())

dict_box = defaultdict(lambda : BOX())
dict_head = defaultdict(lambda : -1)
dict_tail = defaultdict(lambda : -1)
dict_line_stat = defaultdict(lambda : 1)
n,m = -1,-1

for turn in range(1, order_q+1):
    input_info = list(map(int,sys.stdin.readline().rstrip().split()))
    order = input_info[0]
    # 공장 설립
    print(input_info)
    if order == 100:
        # n 개의 선물, m 개의 벨트
        n,m = input_info[1], input_info[2]
        id_info = input_info[3:3+n]
        weight_info = input_info[3+n:]
        make_factory(n,m,id_info,weight_info)
    # 물건 하차
    elif order == 200:
        w_max = input_info[1]
        result = down_box(w_max)
        print(result)
    # 물건 제거
    elif order == 300:
        r_id = input_info[1]
        result = del_box(r_id)
        print(result)
    # 물건 확인
    elif order == 400:
        f_id = input_info[1]
        result = check_box(f_id)
        print(result)
    # 벨트 고장
    elif order == 500:
        b_num = input_info[1]
        result = broken_belt(b_num)
        print(result)
    show_info(turn)

"""
8
100 5 1 1 2 3 4 5 10 20 30 40 50
200 20
200 20
200 20

8
100 5 1 1 2 3 4 5 10 20 30 40 50
300 3
300 4
300 5
"""