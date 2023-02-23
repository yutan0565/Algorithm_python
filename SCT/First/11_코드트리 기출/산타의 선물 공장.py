import sys
from collections import deque


def make_fac(n,m,list_id,list_w):
    graph = [[] for _ in range(m)]
    line_max = n // m
    for index in range(n):
        if index%line_max== 0 and index != 0:
            line += 1
        graph[line].append([list_id[index], list_w[index]])
        dict_info[list_id[index]] = list_w[index]
    return graph

def down_ob(w_max):
    # 하차된 상자 무게의 총합
    sum = 0
    for i in range(m):
        if belt_stat[i] != 1 and len(graph[i]) != 0:
            temp_id, temp_weight = graph[i][0]
            if temp_weight <= w_max:
                graph[i] = graph[i][1:]
                sum += temp_weight
                continue
            else:
                graph[i] = graph[i][1:]
                graph[i].append([temp_id, temp_weight])
    return sum

def del_ob(r_id):
    # 그러한 상타가 있는 경우 r_id,  없다면 -1
    for i in range(m):
        if belt_stat[i] != 1 and len(graph[i]) != 0:
            for j in range(len(graph[i])):
                if graph[i][j][0] == r_id:
                    graph[i].remove([graph[i][j][0], graph[i][j][1]])
                    return r_id
    return -1

def check_ob(f_id):
    # 그러한 상자가 있는 경우 f_id값을, 없다면 -1
    #  해당 고유 번호에 해당하는 상자가 놓여있는 벨트가 있다면 해당 벨트의 번호를 출력하고, 없다면 -1
    for i in range(m):
        if belt_stat[i] != 1 and len(graph[i]) != 0:
            for j in range(len(graph[i])):
                if graph[i][j][0] == f_id:
                    stop_ob = graph[i][:j]
                    move_ob = graph[i][j:]
                    graph[i] = move_ob + stop_ob
                    return i+1
    return  -1

def broken_belt(b_num):
    #약 b_num 벨트가 이미 망가져 있었다면 -1을, 그렇지 않았다면 정상적으로 고장을 처리했다는 뜻으로 b_num 값을 출력
    if belt_stat[b_num-1] == 1:
        return -1
    else:
        belt_stat[b_num-1] = 1
        move_ob = graph[b_num-1]
        graph[b_num - 1] = []
        check_line= b_num-1
        while 1:
            check_line = (check_line + 1)%m
            if belt_stat[check_line] != 1:
                graph[check_line] += move_ob
                break
        return b_num

n = int(sys.stdin.readline().rstrip())
dict_line = {}
dict_next = {}
dict_before = {}

def show_graph():
    print("graph")
    for g in graph:
        print(g)

for _ in range(n):
    input_info = list(map(int, sys.stdin.readline().rstrip().split()))
    order = input_info[0]
    if order == 100:
        n,m = input_info[1], input_info[2]
        list_id = input_info[3:3+n]
        list_w = input_info[3+n:]
        graph = make_fac(n,m,list_id,list_w)
    elif order == 200:
        w_max = input_info[1]
        result = down_ob(w_max)
        print(result)
    elif order == 300:
        r_id = input_info[1]
        result = del_ob(r_id)
        print(result)
    elif order == 400:
        f_id = input_info[1]
        result = check_ob(f_id)
        print(result)
    elif order == 500:
        b_num = input_info[1]
        result = broken_belt(b_num)
        print(result)
    # show_graph()
