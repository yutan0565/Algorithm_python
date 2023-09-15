import sys

def make_direct_list():
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    now_direct = 0
    direct_list = []
    cnt = 1
    while 1:
        for _ in range(2):
            for _ in range(cnt):
                direct_list.append(now_direct)
                if len(direct_list) == n*n - 1:
                    return direct_list
            now_direct = (now_direct + 1)%4
        cnt += 1


def make_graph_index_line(direct_list):
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    x = center_x
    y = center_y
    graph_index[x][y] = -1
    num = 0
    for d in direct_list:
        x = x + dx[d]
        y = y + dy[d]
        graph_index[x][y] = num
        line_list.append(graph[x][y])
        num += 1

def del_tower():
    global line_list
    new_line_list = []
    temp = []
    for i in range(n*n-1):
        if line_list[i] == -1:
            temp.append(0)
        else:
            new_line_list.append(line_list[i])
    line_list = new_line_list + temp

def attack_tower(direct, speed):
    global score
    dx_attack = [0,1,0,-1]
    dy_attack = [1,0,-1,0]
    x,y = center_x, center_y

    for _ in range(speed):
        x = x + dx_attack[direct]
        y = y + dy_attack[direct]
        idx = graph_index[x][y]
        if line_list[idx] == 0:
            break
        score += line_list[idx]
        line_list[idx] = -1
    del_tower()

def resize_line_list():
    global line_list
    if len(line_list) >= n*n:
        line_list = line_list[:n*n-1]
    else:
        now_len = len(line_list)
        gap = n*n-1 - now_len
        for _ in range(gap):
            line_list.append(0)

def del_monster():
    global line_list, score
    del_flag = False
    new_lise_list = []

    temp = [line_list[0]]
    for i in range(1, n*n):
        now_num = line_list[i]
        # 마지막인 경우
        if now_num == 0:
            break
        # 기존 번호랑 같은 경우
        if now_num == temp[0]:
            temp.append(now_num)

        # 다른 번호가 나온 경우
        if now_num != temp[0]:
            # 4개 이상 쌓인 경우
            if len(temp) >= 4:
                score = score + len(temp)*temp[0]
                temp = [now_num]
                del_flag = True
            else:
                new_lise_list += temp
                temp = [now_num]
    # 마지막에 남은거 추가
    # 4개 이상 쌓인 경우
    if len(temp) >= 4:
        score = score + len(temp) * temp[0]
    else:
        new_lise_list += temp

    line_list = new_lise_list
    # 크기 맞춰 주기
    resize_line_list()
    return del_flag

def make_new_line():
    global line_list

    new_lise_list = []
    temp = [line_list[0]]
    for i in range(1, n*n):
        now_num = line_list[i]
        # 마지막인 경우
        if now_num == 0:
            break
        # 기존 번호랑 같은 경우
        if now_num == temp[0]:
            temp.append(now_num)
        # 다른 번호가 나온 경우
        if now_num != temp[0]:
            total_cnt = len(temp)
            new_num = temp[0]
            new_lise_list += [total_cnt, new_num]
            temp = [now_num]
    # 마지막에 남은거 추가
    total_cnt = len(temp)
    new_num = temp[0]
    new_lise_list += [total_cnt, new_num]

    line_list = new_lise_list
    # 크기 맞춰 주기
    resize_line_list()



def simulation():
    for turn in range(1, m+1):
        direct, speed = map(int,sys.stdin.readline().rstrip().split())

        attack_tower(direct, speed)

        while 1:
            if del_monster():

                continue
            else:
                break
        make_new_line()



n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
line_list = []
graph_index = [[0 for _ in range(n)] for _ in range(n)]
center_x = n//2
center_y = n//2
direct_list = make_direct_list()
make_graph_index_line(direct_list)

score = 0

simulation()
print(score)