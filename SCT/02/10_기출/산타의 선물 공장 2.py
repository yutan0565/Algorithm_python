import sys

# 공장 설립
def make_factory(n,m,b_num_list):
    # 라인의 헤드, 테일, 초기화
    for line in range(1, n + 1):
        line_head[line] = -1
        line_tail[line] = -1
        line_count[line] = 0

    for box_num in range(1, len(b_num_list) + 1):
        # 라인 지정
        line_number = b_num_list[box_num-1]

        # 박스 올려주기
        # 라인에 아무것도 없는 경우
        if line_count[line_number] == 0:
            # 박스의 앞 뒤 넣어주기
            dict_front[box_num] = -1
            dict_back[box_num] = -1

            # line의 head tail 수정
            line_head[line_number] = box_num
            line_tail[line_number] = box_num
            line_count[line_number] += 1
        # 라인에 다른 박스가 있는 경우 // tail에 다 붙여주기
        else:
            # 새로 붙이는거 앞 뒤 설정 / 이어 붙인 부분 수정
            dict_front[box_num] = line_tail[line_number]
            dict_back[line_tail[line_number]] = box_num
            dict_back[box_num] = -1
            # line의 tail 수정
            line_tail[line_number] = box_num
            # 개수 증가
            line_count[line_number] += 1

# 물건 모두 옮기기
def move_all(m_src,m_dst):
    # m_src 에서   m_dst 의 뒤로 보두 이동
    # m_src가 비어 있으면 끝
    if line_count[m_src] == 0:
        pass
    else:

        # 옮기는 것의,  head, tail 추출
        m_src_head = line_head[m_src]
        m_src_tail = line_tail[m_src]

        # msrc head / tail 초기화
        line_head[m_src] = -1
        line_tail[m_src] = -1

        # m_src의 head를 m_dst의 tail에 붙이기
        # m_dst에 아무것도 없는 경우
        if line_count[m_dst] == 0:
            line_head[m_dst] = m_src_head
            line_tail[m_dst] = m_src_tail
        else:
            dict_front[line_head[m_dst]] = m_src_tail
            dict_back[m_src_tail] = line_head[m_dst]
            line_head[m_dst] = m_src_head

        # msrc 개수 옮기고 초기화
        line_count[m_dst] += line_count[m_src]
        line_count[m_src] = 0
    return line_count[m_dst]

# 앞 물건만 교체하기
def swap_front(m_src,m_dst):
    # 두 벨트 아무것도 없는 경우
    if line_count[m_src] == 0 and line_count[m_dst] == 0:
        pass
    # m_src 쪽에만 물건이 있는 경우
    elif line_count[m_src] != 0 and line_count[m_dst] == 0:
        # 맨 앞 박스의 정보 수정
        now_box = line_head[m_src]
        back_box = dict_back[now_box]

        # 옾기는 박스 정보 수정
        dict_front[now_box] = -1
        dict_back[now_box] = -1

        # 원래 있던 곳
        # 박스가 있다 면
        if back_box != -1:
            dict_front[back_box] = -1
            line_head[m_src] = back_box
        # 박스가 없다면
        elif back_box == -1:
            line_head[m_src] = back_box
        # 라인 정보 수정
        line_head[m_dst] = now_box
        line_tail[m_dst] = now_box
        line_count[m_dst] += 1
        line_count[m_src] -= 1
        # m_src 에 아무 것도 없으면   head = tail = 0
        if line_count[m_src] == 0:
            line_head[m_src] = -1
            line_tail[m_src] = -1

    # m_dst 쪽에만 물건이 있는 경우
    elif line_count[m_src] == 0 and line_count[m_dst] != 0:
        # 맨 앞 박스의 정보 수정
        now_box = line_head[m_dst]
        back_box = dict_back[now_box]

        # 옾기는 박스 정보 수정
        dict_front[now_box] = -1
        dict_back[now_box] = -1

        # 원래 있던 곳
        # 박스가 있다 면
        if back_box != -1:
            dict_front[back_box] = -1
            line_head[m_dst] = back_box
        # 박스가 없다면
        elif back_box == -1:
            line_head[m_dst] = back_box

        # 라인 정보 수정
        line_head[m_src] = now_box
        line_tail[m_src] = now_box
        line_count[m_src] += 1
        line_count[m_dst] -= 1
        # m_src 에 아무 것도 없으면   head = tail = 0
        if line_count[m_dst] == 0:
            line_head[m_dst] = -1
            line_tail[m_dst] = -1

    # 양쪽 모두 물건이 있음
    elif line_count[m_src] != 0 and line_count[m_dst] != 0:
        # 맨 앞 박스의 정보
        m_src_now_box = line_head[m_src]
        m_dst_now_box = line_head[m_dst]

        m_src_back_box = dict_back[m_src_now_box]
        m_dst_back_box = dict_back[m_dst_now_box]

        # 옾기는 박스 정보 수정
        dict_back[m_src_now_box] = m_dst_back_box
        dict_back[m_dst_now_box] = m_src_back_box

        if m_dst_back_box != -1:
            dict_front[m_dst_back_box] = m_src_now_box

        if m_src_now_box != -1:
            dict_front[m_src_back_box] = m_dst_now_box


        # 라인 정보 수정
        line_head[m_src] = m_dst_now_box
        if line_count[m_src] == 1:
            line_tail[m_src] = line_head[m_src]

        line_head[m_dst] = m_src_now_box
        if line_count[m_dst] == 1:
            line_tail[m_dst] = line_head[m_dst]
    return line_count[m_dst]

# 물건 나누기
def divide_box(m_src, m_dst):
    # m_src 의   n/2 개 만큼, m_dst 앞으로 이동
    move_box_number = line_count[m_src] // 2
    if move_box_number == 0:
        pass
    else:
        # 옮겨야 하는 박스의 앞,뒤 박스 정보 구하기 / 옮길 박스의 line 정보 변경
        move_head = line_head[m_src]
        move_tail = move_head

        count = 1
        while 1:
            if count == move_box_number:
                break
            move_tail = dict_back[move_tail]
            count += 1
        back_tail = dict_back[move_tail]
        # 옮기는 박스의 앞뒤 정보 변경

        dict_front[move_head] = -1
        dict_back[move_tail] = line_head[m_dst]
        dict_front[back_tail] = -1
        # m_dst에 다른 물제가 있는 경우에
        if line_count[m_dst] != 0:
            dict_front[line_head[m_dst]] = move_tail
        else:
            dict_back[move_tail] = -1
        # 라인 개수 변경
        line_count[m_src] -= move_box_number
        line_count[m_dst] += move_box_number

        # 정보 변경
        line_head[m_src]  = back_tail
        line_head[m_dst] = move_head
        # 옮겨간 곳에, tail이 없었다면
        if line_tail[m_dst] == -1:
            line_tail[m_dst] = move_tail
        if line_count[m_dst] == 1:
            line_tail[m_dst] = line_head[m_dst]
    return line_count[m_dst]

# 선물 정보 얻기
def get_box_info(p_num):
    a = dict_front[p_num]
    b = dict_back[p_num]
    result = a + 2*b
    return result

# 벨트 정보 얻기
def get_belt_info(b_num):
    a = line_head[b_num]
    b = line_tail[b_num]
    c = line_count[b_num]
    result = a + 2*b + 3*c
    return result

def show_info():
    print("박스")

    print("앞 : ", dict_front)
    print("뒤 : ", dict_back)
    print("라인")
    print("헤드 : ", line_head)
    print("꼬리 : ", line_tail)
    print("개수 : ", line_count)
    print("-------------------------------------------------------------------")


dict_front = {}
dict_back = {}

line_head = {}
line_tail = {}
line_count = {}

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    all_order = list(map(int,sys.stdin.readline().rstrip().split()))
    order = all_order[0]
    # print("명령 : ", order)
    if order == 100: # 공장 설립
        n,m,b_num_list = all_order[1], all_order[2], all_order[3:]
        make_factory(n,m,b_num_list)

    elif order == 200: # 물건 모두 옮기기
        m_src,m_dst = all_order[1], all_order[2]
        result = move_all(m_src,m_dst)
        print(result)

    elif order == 300: # 앞 물건만 교체하기
        m_src, m_dst = all_order[1], all_order[2]
        result = swap_front(m_src,m_dst)
        print(result)

    elif order == 400: # 물건 나누기
        m_src, m_dst = all_order[1], all_order[2]
        result = divide_box(m_src, m_dst)
        print(result)

    elif order == 500: # 선물 정보 얻기
        p_num = all_order[1]
        result = get_box_info(p_num)
        print(result)

    elif order == 600: # 벨트 정보 얻기
        b_num = all_order[1]
        result = get_belt_info(b_num)
        print(result)


"""
4
100 4 6 1 2 2 2 1 4
200 2 4
200 1 4
400 1 4
# 400 4 2
# 300 2 4
# 500 6
# 500 5
# 600 1
# 600 3

2
100 2 5 1 1 1 1 1
400 1 2
"""