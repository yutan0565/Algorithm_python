import sys
from collections import defaultdict

class BOX():
    def __init__(self):
        self.front = -1
        self.back = -1

def append_box(box, line):
    # line 에 아무것도 없는 경우
    if dict_head[line] == -1:
        dict_head[line] = box
        dict_tail[line] = box
        dict_count[line] += 1
    # 다른 물건이 있는 경우
    else:
        now_tail = dict_tail[line]
        dict_tail[line] = box
        dict_box[box].front = now_tail
        dict_box[now_tail].back = box
        dict_count[line] += 1

def make_factory(n,m,line_info):
    for line_num in range(1, n+1):
        dict_head[line_num] = -1
        dict_tail[line_num] = -1
        dict_count[line_num] = 0

    for idx in range(m):
        now_box = idx+1
        now_line = line_info[idx]
        append_box(now_box, now_line)

def move_all_box(m_src, m_dst):
    # m_src에 아무것도 없느 경우 / 아무것도 안함
    if dict_head[m_src] == -1:
        pass
    # m_src에 물건이 있는 경우
    else:
        m_dst_head = dict_head[m_dst]
        # m_dst에 아무것도 없는 경우
        if m_dst_head == -1:
            src_head = dict_head[m_src]
            src_tail = dict_tail[m_src]
            src_count = dict_count[m_src]

            # src 정리
            dict_head[m_src] = -1
            dict_tail[m_src] = -1
            dict_count[m_src] = 0

            # dst 옮기기
            dict_head[m_dst] = src_head
            dict_tail[m_dst] = src_tail
            dict_count[m_dst] = src_count

        # 다른 물건이 있는 경우
        else:
            src_head = dict_head[m_src]
            src_tail = dict_tail[m_src]
            src_count = dict_count[m_src]

            # src 정리
            dict_head[m_src] = -1
            dict_tail[m_src] = -1
            dict_count[m_src] = 0

            dict_box[m_dst_head].front = src_tail
            dict_box[src_tail].back = m_dst_head
            dict_head[m_dst] = src_head
            dict_count[m_dst] += src_count

    return dict_count[m_dst]

def update_tail(line):
    if dict_count[line] == 1:
        dict_tail[line] = dict_head[line]
    elif dict_count[line] == 0:
        dict_tail[line] = -1

def change_front_box(m_src, m_dst):
    src_head = dict_head[m_src]
    dst_head = dict_head[m_dst]
    src_head_back = dict_box[src_head].back
    dst_head_back = dict_box[dst_head].back

    # 둘다 아무것도 없는 경우
    if src_head == -1 and dst_head == -1:
        pass
    # 둘다 있는 경우
    elif src_head != -1 and dst_head != -1:
        # 머리 정보 교체
        dict_head[m_src],dict_head[m_dst] = dict_head[m_dst], dict_head[m_src]
        # fron 정보 update
        dict_box[src_head_back].front = dst_head
        dict_box[dst_head_back].front = src_head
        # back 정보 교체
        dict_box[src_head].back = dst_head_back
        dict_box[dst_head].back = src_head_back
        # 1개 씩만 있던 경우, tail update
        update_tail(m_src)
        update_tail(m_dst)
    # src만 있는 경우
    elif src_head != -1 and dst_head == -1:
        # 머리 정보 교체
        dict_head[m_src] = src_head_back
        if src_head_back != -1:
            dict_box[src_head_back].front = -1
        dict_head[m_dst] = src_head
        # back 정보 교체
        dict_box[src_head].back = -1
        # 개수 정보 업데이트
        dict_count[m_src] -= 1
        dict_count[m_dst] += 1
        # tail 정보 업데이트
        update_tail(m_src)
        dict_tail[m_dst] = src_head

    # dst만 있는 경우
    elif src_head == -1 and dst_head != -1:
        # 머리 정보 교체
        dict_head[m_dst] = dst_head_back
        if dst_head_back != -1:
            dict_box[dst_head_back].front = -1
        dict_head[m_src] = dst_head
        # back 정보 교체
        dict_box[dst_head].back = -1
        # 개수 정보 업데이트
        dict_count[m_dst] -= 1
        dict_count[m_src] += 1
        # tail 정보 업데이트
        update_tail(m_dst)
        dict_tail[m_src] = dst_head
    return dict_count[m_dst]

def move_half_box(m_src, m_dst):
    src_count = dict_count[m_src]
    half_count = src_count // 2

    # 옮길게 없는 경우
    if half_count == 0:
        pass
    else:
        move_head = dict_head[m_src]
        move_tail = move_head
        cnt = 1
        while 1:
            if cnt == half_count:
                break
            move_tail = dict_box[move_tail].back
            cnt += 1
        # src 정보 업데이트
        dict_head[m_src] = dict_box[move_tail].back
        dict_box[dict_box[move_tail].back].front = -1
        dict_count[m_src] -= cnt

        # move head 부터 move tail 까지 m_dst의 앞으로 옮기기
        m_dst_head = dict_head[m_dst]
        # m_dst에 아무것도 없는 경우
        if m_dst_head == -1:
            # dst 옮기기
            dict_head[m_dst] = move_head
            dict_tail[m_dst] = move_tail
            dict_box[move_tail].back = -1
            dict_count[m_dst] = cnt

        # 다른 물건이 있는 경우
        else:
            dict_box[m_dst_head].front = move_tail
            dict_box[move_tail].back = m_dst_head
            dict_head[m_dst] = move_head
            dict_count[m_dst] += cnt
    return dict_count[m_dst]


def get_box_info(p_num):
    a = dict_box[p_num].front
    b = dict_box[p_num].back
    return a + 2*b

def get_line_info(b_num):
    a = dict_head[b_num]
    b = dict_tail[b_num]
    c = dict_count[b_num]
    return a + 2*b + 3*c

def show_info():
    for id in range(1,m+1):
        print("{}  front : {}  back : {}".format(id,dict_box[id].front,dict_box[id].back))
    print("머리 : ", dict(dict_head))
    print("꼬리 : ", dict(dict_tail))
    print("개수 : ", dict(dict_count))


dict_box = defaultdict(lambda  : BOX())

dict_head = defaultdict(lambda : -1)
dict_tail = defaultdict(lambda : -1)
dict_count = defaultdict(lambda : 0)

q = int(sys.stdin.readline().rstrip())
n,m = 0,0

for turn in range(1, q+1):
    input_info = list(map(int,sys.stdin.readline().rstrip().split()))
    order = input_info[0]
    #공장 설립

    if order == 100:
        # 벨트 개수, 선물 개수
        n,m = input_info[1],input_info[2]
        line_info = input_info[3:]
        make_factory(n,m,line_info)
    # 물건 모두 옮기기
    elif order == 200:
        m_src, m_dst = input_info[1],input_info[2]
        result = move_all_box(m_src, m_dst)
        print(result)
    # 앞 물건만 교체하기
    elif order == 300:
        m_src, m_dst = input_info[1], input_info[2]
        result = change_front_box(m_src, m_dst)
        print(result)
    # 물건 나누기
    elif order == 400:
        m_src, m_dst = input_info[1], input_info[2]
        result = move_half_box(m_src, m_dst)
        print(result)
    # 선물 정보 얻기
    elif order == 500:
        p_num = input_info[1]
        result = get_box_info(p_num)
        print(result)
    #벨트 정보 얻ㄱ기
    elif order == 600:
        b_num = input_info[1]
        result = get_line_info(b_num)
        print(result)




"""
8
100 4 6 1 2 2 2 1 4
400 2 3

"""