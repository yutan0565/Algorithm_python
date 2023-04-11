import sys
from collections import defaultdict

# 100 공장 설립
def make_fac(n,m,b_num_list):
    # n 개의 벨트 / m개의 물건
    for now_num in range(1,m+1):
        now_line = b_num_list[now_num-1]
        # 그 라인에 아무것도 없으면
        if line_head[now_line] == -1:
            line_head[now_line] = now_num
            line_tail[now_line] = now_num
            dict_next[now_num] = -1
            dict_prev[now_num] = -1
            line_count[now_line] += 1
        # 다른 물건이 있으면
        else:
            now_tail = line_tail[now_line]
            dict_next[now_num] = now_tail
            dict_prev[now_tail] = now_num
            dict_prev[now_num] = -1

            line_tail[now_line] = now_num
            line_count[now_line] += 1

# 200 박스 모두 옮기기
def move_all_box(m_src, m_dst):
    # m_src에 아무것도 없는 경우
    if line_head[m_src] == -1:
        return line_count[m_dst]
    # m_src에 다른게 있는 경우
    else:
        # m_src의 기존 정보 / 초기화
        src_head = line_head[m_src]
        src_tail = line_tail[m_src]
        src_count = line_count[m_src]
        line_head[m_src] = -1
        line_tail[m_src] = -1
        line_count[m_src] = 0

        # 옮겨 주기
        # dst에 아무것도 없느 경우
        if line_head[m_dst] == -1:
            line_head[m_dst] = src_head
            line_tail[m_dst] = src_tail
            line_count[m_dst] += src_count
        # dst에 다른게 있는 경우
        else:
            dst_head = line_head[m_dst]
            dict_next[dst_head] = src_tail
            dict_prev[src_tail] = dst_head
            line_head[m_dst] = src_head
            line_count[m_dst] += src_count
        return line_count[m_dst]

# 300 앞 물건만 교체하기
def switch_front_box(m_src, m_dst):
    src_head = line_head[m_src]
    src_tail = line_tail[m_src]
    src_count = line_count[m_src]

    dst_head = line_head[m_dst]
    dst_tail = line_tail[m_dst]
    dst_count = line_count[m_dst]

    # 둘다 아무것도 없음
    if src_count == 0 and dst_count == 0:
        pass
    # m_src에만 아무것도 없음
    elif src_count == 0 and dst_count != 0:
        dst_head_prev = dict_prev[dst_head]
        # dst에 1개만 남은 경우
        if dst_head_prev == -1:
            line_head[m_dst] = -1
            line_tail[m_dst] = -1
            line_count[m_dst] -= 1

            line_head[m_src] = dst_head
            line_tail[m_src] = dst_tail
            line_count[m_src] += 1
        # dst 뒤에 다른게 있는 경우
        else:
            line_head[m_dst] = dst_head_prev
            dict_next[dst_head_prev] = -1
            line_count[m_dst] -= 1

            dict_prev[dst_head] = -1
            line_head[m_src] = dst_head
            line_tail[m_src] = dst_head
            line_count[m_src] += 1
    # m_dst에만 아무것도 없음
    elif src_count != 0 and dst_count == 0:
        src_head_prev = dict_prev[src_head]
        # src에 1개만 남은 경우
        if src_head_prev == -1:
            line_head[m_src] = -1
            line_tail[m_src] = -1
            line_count[m_src] -= 1

            line_head[m_dst] = src_head
            line_tail[m_dst] = src_tail
            line_count[m_dst] += 1
        # src 뒤에 다른게 있는 경우
        else:
            line_head[m_src] = src_head_prev
            dict_next[src_head_prev] = -1
            line_count[m_src] -= 1

            dict_prev[src_head] = -1
            line_head[m_dst] = src_head
            line_tail[m_dst] = src_head
            line_count[m_dst] += 1
    # 둘다 물건 있음
    elif src_count != 0 and dst_count != 0:
        src_head_prev = dict_prev[src_head]
        dst_head_prev = dict_prev[dst_head]

        dict_prev[src_head] = dst_head_prev
        dict_prev[dst_head] = src_head_prev

        line_head[m_src] = dst_head
        line_head[m_dst] = src_head

        if src_head_prev != -1:
            dict_next[src_head_prev] = dst_head
        else:
            line_tail[m_src] =dst_head

        if dst_head_prev != -1:
            dict_next[dst_head_prev] = src_head
        else:
            line_tail[m_dst] = src_head
    return line_count[m_dst]

# 400 물건 나누기
def divide_box(m_src, m_dst):
    move_count = line_count[m_src]//2
    # 옮길게 없느 경우
    if move_count == 0:
        pass
    else:
        move_head = line_head[m_src]
        move_tail = move_head
        count = 1
        while 1:
            if count == move_count:
                break
            move_tail = dict_prev[move_tail]
            count += 1
        prev_move_tail = dict_prev[move_tail]

        # 기존에 있는 src 라인 정보 변경
        line_head[m_src] = prev_move_tail
        dict_next[prev_move_tail] = -1
        line_count[m_src] -= move_count

        # 이동하기
        dst_head = line_head[m_dst]
        # 이동하는 곳에 아무것도 없음
        if dst_head == -1:
            dict_prev[move_tail] = -1
            line_head[m_dst] = move_head
            line_tail[m_dst] = move_tail
            line_count[m_dst] += move_count
        else:
            dict_prev[move_tail] = dst_head
            dict_next[dst_head] = move_tail

            line_head[m_dst] = move_head
            line_count[m_dst] += move_count
    return line_count[m_dst]

# 500 박스 정보 얻기
def get_box_info(p_num):
    a = dict_next[p_num]
    b = dict_prev[p_num]
    sum = a + 2*b
    return sum

# 600 벨트 정보 얻기
def get_belt_info(b_num):
    a = line_head[b_num]
    b = line_tail[b_num]
    c = line_count[b_num]
    sum = a + 2*b + 3*c
    return sum

dict_next = defaultdict(lambda  : -1)
dict_prev = defaultdict(lambda  : -1)

line_head = defaultdict(lambda  : -1)
line_tail = defaultdict(lambda  : -1)
line_count = defaultdict(lambda  : 0)


def show_info():
    print("==============================")
    print("다음 : ", dict(dict_next))
    print("이전 : ", dict(dict_prev))
    print("머리 : ", dict(line_head))
    print("꼬리 : ", dict(line_tail))
    print("개수 : ", dict(line_count))

n = int(sys.stdin.readline().rstrip())
for round in range(1,n+1):
    input_info = list(map(int,sys.stdin.readline().rstrip().split()))
    order = input_info[0]
    if order == 100:
        n,m,b_num_list = input_info[1],input_info[2],input_info[3:]
        make_fac(n,m,b_num_list)
    elif order == 200:
        m_src, m_dst = input_info[1],input_info[2]
        result = move_all_box(m_src, m_dst)
        print(result)
    elif order == 300:
        m_src, m_dst = input_info[1],input_info[2]
        result = switch_front_box(m_src, m_dst)
        print(result)
    elif order == 400:
        m_src, m_dst = input_info[1],input_info[2]
        result = divide_box(m_src, m_dst)
        print(result)
    elif order == 500:
        p_num = input_info[1]
        result = get_box_info(p_num)
        print(result)
    elif order == 600:
        b_num = input_info[1]
        result = get_belt_info(b_num)
        print(result)
    show_info()
"""
2
100 3 4 1 1 3 3   
300 1 3
"""