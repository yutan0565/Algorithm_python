import sys
from collections import defaultdict

# 100  공장 설립
def make_fac(n,m,b_num_list):
    # n개의 라인 /  m 개의 물건 개수
    for num in range(1, m+1):
        now_line = b_num_list[num-1]

        # now line에 아무것도 없는경우
        if line_head[now_line] == -1:
            dict_next[num] = -1
            dict_before[num] = -1

            line_head[now_line] = num
            line_tail[now_line] = num

            line_count[now_line] += 1
        # 다른 물건이 있는 경우
        else:
            dict_next[num] = line_tail[now_line]
            dict_before[line_tail[now_line]] = num

            dict_before[num] = -1

            line_tail[now_line] = num

            line_count[now_line] += 1

# 200 물건 모두 옮기기
def move_all_box(m_src, m_dst):
    # m_src가 비어 있으면 아무것도 안함
    if line_head[m_src] == -1 and line_tail[m_src] == -1:
        return line_count[m_dst]
    # 옮길 물건이 있으면
    else:
        # 옮길거 정보
        now_head = line_head[m_src]
        now_tail = line_tail[m_src]
        now_count = line_count[m_src]
        # m_src 라인 정보 지우기
        line_head[m_src] = -1
        line_tail[m_src] = -1
        line_count[m_src] = 0

        # m_dst 기존의 정보
        dst_head = line_head[m_dst]
        # dst에 아무 것도 없는 경우
        if dst_head == -1:
            line_head[m_dst] = now_head
            line_tail[m_dst] = now_tail
        # 다른 물건이 있는 경우
        else:
            dict_next[dst_head] = now_tail
            dict_before[now_tail] = dst_head

            line_head[m_dst] = now_head
        line_count[m_dst] += now_count
        return line_count[m_dst]

# 300  앞 물건만 교체하기
def switch_front(m_src, m_dst):
    src_head = line_head[m_src]
    src_tail = line_tail[m_src]

    dst_head = line_head[m_dst]
    dst_tial = line_tail[m_dst]

    # 둘다 아무것도 없음
    if src_head == -1 and dst_head == -1:
        pass
    # src 에만 물건이 있음
    elif src_head != -1 and dst_head == -1:
        # src 에 있는거 정리
        src_head_before = dict_before[src_head]
        # 뒤에 아무것도 없으면
        if src_head_before == -1:
            line_head[m_src] = -1
            line_tail[m_src] = -1
        else:
            dict_next[src_head_before] = -1
            line_head[m_src] = src_head_before

        # dst 쪽으로 옮기기
        dict_next[src_head] = -1
        dict_before[src_head] = -1
        line_head[m_dst] = src_head
        line_tail[m_dst] = src_head

        # 개수 조정
        line_count[m_src] -= 1
        line_count[m_dst] += 1
    # 위에랑 반대
    elif src_head == -1 and dst_head != -1:
        # dst 에 있는거 정리
        dst_head_before = dict_before[dst_head]
        # 뒤에 아무것도 없으면
        if dst_head_before == -1:
            line_head[m_dst] = -1
            line_tail[m_dst] = -1
        else:
            dict_next[dst_head_before] = -1
            line_head[m_dst] = dst_head_before

        # src 쪽으로 옮기기
        dict_next[dst_head] = -1
        dict_before[dst_head] = -1
        line_head[m_src] = dst_head
        line_tail[m_src] = dst_head

        # 개수 조정
        line_count[m_dst] -= 1
        line_count[m_src] += 1
    # 양 쪽 모두 물건이 있는 상태임
    else:
        src_head_before = dict_before[src_head]
        dst_head_before = dict_before[dst_head]

        # 각 라인의 헤드 값 교체
        line_head[m_src] = dst_head
        line_head[m_dst] = src_head

        # 헤드 위에 아무것도 없으면 /
        if src_head_before == -1:
            line_tail[m_src] = dst_head
        else:
            dict_next[src_head_before] = dst_head

        if dst_head_before == -1:
            line_tail[m_dst] = src_head
        else:
            dict_next[dst_head_before] = src_head
        # 각 노드의 before 변경 해주기
        dict_before[src_head] = dst_head_before
        dict_before[dst_head] = src_head_before


    return line_count[m_dst]

# 400  물건 나누기
def divide_box(m_src, m_dst):
    move_count = line_count[m_src] // 2
    # 옮길게 없는 경우
    if move_count == 0:
        return line_count[m_dst]
    else:
        # 옮길 라인 정리
        move_head = line_head[m_src]
        move_tail = move_head
        if move_count != 1:
            count = 1
            while 1:
                count += 1
                move_tail = dict_before[move_tail]
                if count == move_count:
                    break
        # src 자리 처리
        src_new_head = dict_before[move_tail]
        dict_next[src_new_head] = -1
        line_head[m_src] = src_new_head
        line_count[m_src] -= move_count
        # 옮기기
        dst_head = line_head[m_dst]
        # 옮기는 곳에 아무것도 없다면
        if dst_head == -1:
            line_head[m_dst] = move_head
            line_tail[m_dst] = move_tail
            dict_before[move_tail] = -1
        # 다른 물건이 있다면
        else:
            # 연결지어 주기
            dict_before[move_tail] = dst_head
            dict_next[dst_head] = move_tail
            line_head[m_dst] = move_head
        line_count[m_dst] += move_count
        return line_count[m_dst]

# 500 선물 정보 얻기
def get_box_info(p_num):
    a = dict_next[p_num]
    b = dict_before[p_num]
    return a + 2*b

# 600 벨트 정보 얻기
def get_belt_info(b_num):
    a = line_head[b_num]
    b = line_tail[b_num]
    c = line_count[b_num]
    return a + 2*b + 3*c

def show_info(turn, order):
    print("===========================")
    print("순서 : ", turn, "명령 : ", order)
    print("다음 : ", dict(dict_next))
    print("이전 : ", dict(dict_before))
    print("머리 : ", dict(line_head))
    print("꼬리 : ", dict(line_tail))
    print("개수 : ", dict(line_count))

dict_next = defaultdict(lambda : -1)
dict_before = defaultdict(lambda : -1)

line_head = defaultdict(lambda : -1)
line_tail = defaultdict(lambda : -1)
line_count = defaultdict(lambda : 0)


n = int(sys.stdin.readline().rstrip())
for turn in range(1,n+1):
    input_info = list(map(int,sys.stdin.readline().rstrip().split()))
    order = input_info[0]
    if order == 100:
        n,m,b_num_list = input_info[1],input_info[2],input_info[3:]
        make_fac(n,m,b_num_list)

    elif order == 200:
        m_src, m_dst = input_info[1], input_info[2]
        result = move_all_box(m_src, m_dst)
        print(result)

    elif order == 300:
        m_src, m_dst = input_info[1], input_info[2]
        result = switch_front(m_src, m_dst)
        print(result)

    elif order == 400:
        m_src, m_dst = input_info[1], input_info[2]
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
    # show_info(turn, order)

"""
2
100 3 4 1 1 2 2 
300 1 2


"""