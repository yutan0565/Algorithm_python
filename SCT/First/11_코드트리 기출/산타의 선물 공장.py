import sys

def make_fac(n,m,list_id,list_w):
    line_max = n//m
    for i in range(n):
        weight[list_id[i]] = list_w[i]
    index = 0
    if line_max == 1:
        for i in range(n):
            now_line = i
            line[list_id[i]] = now_line
            line_state[now_line] = -1
            line_head[now_line] = list_id[i]
            line_tail[now_line] = list_id[i]
            next[list_id[i]] = -1
            before[list_id[i]] = -1
    else:
        for i in range(m):
            now_line = i
            line_state[now_line] = -1
            for j in range(line_max):
                line[list_id[index]] = now_line
                if j == 0:
                    line_head[now_line] = list_id[index]
                    next[list_id[index]] = -1
                    before[list_id[index]] = list_id[index + 1]
                elif j == line_max-1:
                    line_tail[now_line] = list_id[index]
                    next[list_id[index]] = list_id[index-1]
                    before[list_id[index]] = -1
                else:
                    before[list_id[index]] = list_id[index+1]
                    next[list_id[index]] = list_id[index-1]
                index += 1

def down_ob(w_max):
    temp_result = 0
    for i in range(m):
        if line_state[i] != -1:
            continue
        temp_id = line_head[i]
        if temp_id == -1:
            continue
        temp_weight = weight[temp_id]

        if temp_weight <= w_max: # 하차
            if line_tail[i] == temp_id:
                temp_result += temp_weight
                line[temp_id] = -1
                before[temp_id] = -1
                next[temp_id] = -1
                line_head[i] = -1
                line_tail[i] = -1
            else:
                temp_result += temp_weight
                line_head[i] = before[temp_id]
                next[before[temp_id]] = -1
                line[temp_id] = -1
                before[temp_id] = -1
                next[temp_id] = -1

        else: # 맨 뒤로 보냄
            if line_tail[i] == temp_id:
                continue
            new_head  = before[temp_id]
            new_tail = temp_id

            next[temp_id] = line_tail[i]
            before[line_tail[i]] = temp_id

            before[temp_id] = -1
            next[before[temp_id]] = -1

            line_head[i] = new_head
            line_tail[i] = new_tail
    return temp_result
def del_ob(r_id):
    if r_id not in line.keys():
        return -1
    if line[r_id] == -1:
        return -1
    del_line = line[r_id]
    if line_head[del_line] == line_tail[del_line]:
        line[r_id] = -1
        before[r_id] = -1
        next[r_id] = -1
        line_head[del_line] = -1
        line_tail[del_line] = -1
    elif line_head[del_line] == r_id:
        line_head[del_line] = before[r_id]
        line[r_id] = -1
        before[r_id] = -1
        next[r_id] = -1
    elif line_tail[del_line] == r_id:
        line_tail[del_line] = next[r_id]
        line[r_id] = -1
        before[r_id] = -1
        next[r_id] = -1
    else:
        before[next[r_id]] = before[r_id]
        next[before[r_id]] = next[r_id]
        line[r_id] = -1
        before[r_id] = -1
        next[r_id] = -1
    return r_id
def check_ob(f_id):
    if f_id not in line.keys():
        return -1
    if line[f_id] == -1:
        return -1
    now_line = line[f_id]

    if line_head[now_line] == line_tail[now_line]:
        return now_line+1
    else:
        new_tail = next[f_id]
        before[line_tail[now_line]] = line_head[now_line]
        next[line_head[now_line]] = line_tail[now_line]

        before[next[f_id]] = -1
        next[f_id] = -1

        line_head[now_line] = f_id
        line_tail[now_line] = new_tail

        return now_line+1

def broken_belt(b_num):
    brok_line = b_num-1
    move_line = brok_line
    if line_state[brok_line] != -1:
        return -1
    line_state[brok_line] = 1
    now_id = line_head[brok_line]
    if now_id == -1:
        return b_num
    for i in range(m):
        move_line = (move_line + 1)%m
        if line_state[move_line] != -1:
            continue
        else:
            new_tail = line_tail[brok_line]
            # 옮겨 붙이기
            next[line_head[brok_line]] = line_tail[move_line]
            before[line_tail[move_line]] = line_head[brok_line]

            line_tail[move_line] = line_tail[brok_line]
            if next[line_head[brok_line]] == -1:
                line_head[move_line] = line_head[brok_line]
            while 1:
                line[now_id] = move_line
                now_id = before[now_id]
                if now_id == -1:
                    line_head[brok_line] = -1
                    line_tail[brok_line] = -1
                    return b_num


n = int(sys.stdin.readline().rstrip())

weight = {}
before = {}
next = {}
line = {}

line_head = {}
line_tail = {}
line_state = {}

def show_info():
    # print("------------------------------")
    # print("무게 : ", weight)
    # print("다음 : ", next)
    # print("이전 : ", before)
    # print("라인 : ", line)
    # print("머리 : ", line_head)
    # print("꼬리 : ", line_tail)
    # print("상태 : ", line_state)
    # print("------------------------------")
    pass

# fr = open("C:/Users/yutan/Downloads/correct_output (1).txt", 'r')
result = 0
flag = 0
for count in range(n):
    input_info = list(map(int, sys.stdin.readline().rstrip().split()))
    order = input_info[0]
    if order == 100:
        n,m = input_info[1], input_info[2]
        list_id = input_info[3:3+n]
        list_w = input_info[3+n:]
        make_fac(n,m,list_id,list_w)
        show_info()
        continue
    elif order == 200:
        w_max = input_info[1]
        result = down_ob(w_max)
        print(result)
        show_info()
    elif order == 300:
        r_id = input_info[1]
        result = del_ob(r_id)
        print(result)
        show_info()
    elif order == 400:
        f_id = input_info[1]
        result = check_ob(f_id)
        print(result)
        show_info()
    elif order == 500:
        b_num = input_info[1]
        result = broken_belt(b_num)
        print(result)
        show_info()

    # if line_head[0] == -1 and flag == 0:
    #     print("헤드 -1 : ", order)
    #     temp = []
    #     for key in line.keys():
    #         if line[key] != -1:
    #             temp.append(weight[key])
    #     print(temp)
    #     flag = 1
    #
    # co = int(fr.readline())
    # if co != result:
    #     print("순번 : ",count + 1   , "정답 : ",co, "내꺼 : ",result, "명령 : ", order)





"""
7
100 12 3 10 12 20 15 14 19 22 25 16 17 21 18 30 30 20 20 10 18 17 15 25 11 14 17
200 25
300 22
300 999
400 14
400 21
500 3

10
100 6 1 1 2 3 4 5 6 10 20 30 40 50 60
200 100
300 3
400 4
400 2
200 60
200 60
200 60
200 60
200 60

4
100 3 3 10 7 8 7 3 8
200 10
500 1
500 1


4
100 3 3 10 7 8 7 3 8
400 10
500 1
500 1

"""
