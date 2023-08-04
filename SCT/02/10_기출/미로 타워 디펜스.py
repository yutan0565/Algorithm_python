import sys

def make_d_line():
    d_line = []
    count = 1
    index = 0
    while 1:
        for _ in range(2):
            for _ in range(count):
                d_line.append(index)
                if len(d_line) == max_len:
                    return d_line
            index  = (index + 1)%4
        count += 1

def make_pos_line():
    x,y = center_x, center_y
    pos_line, number_line = [], []
    index = 0
    for d in d_line:
        x = x + dx_line[d]
        y = y + dy_line[d]
        index_graph[x][y] = index
        index += 1
        number_line.append(graph[x][y])
    return number_line

def del_zero():
    new_number_line = []
    zero_count = 0
    for num in number_line:
        if num != 0:
            new_number_line.append(num)
        else:
            zero_count += 1
    new_number_line = new_number_line + [0 for _ in range(zero_count)]
    return new_number_line


def attack_tower(attack_d, p):
    global total_score
    x,y = center_x, center_y
    for _ in range(p):
        x = x + dx_attack[attack_d]
        y = y + dy_attack[attack_d]
        del_index = index_graph[x][y]
        total_score += number_line[del_index]
        number_line[del_index] = 0

def del_four_num():
    global total_score
    end_flag = 0
    new_number_line = []
    temp = [number_line[0]] # new에 넣기 전 임시 공간
    for i in range(1, len(number_line)):
        now_num = number_line[i]
        # 끝이 보이면, 그만
        if now_num == 0:
            if len(temp) >= 4:
                total_score += (len(temp)*temp[0])
                end_flag = 1
                break
            else:
                new_number_line = new_number_line + temp
                break
        # 지금 번호가, 원래 들어가 있는거랑 같으면
        if now_num == temp[0]:
            temp.append(now_num)
        # temp에 있는거랑 다르면
        else:
            # 4개 이상 쌓여 있었으면 / 그냥 지워주기
            if len(temp) >= 4:
                total_score += (len(temp) * temp[0])
                temp = [now_num]
                end_flag = 1
            else: # 4개 미만으로 쌓여 있으면
                new_number_line = new_number_line + temp
                temp = [now_num]
    return end_flag, new_number_line

def make_set_number():
    new_number_line = []
    temp = [number_line[0]]
    for i in range(1, len(number_line)):
        now_num = number_line[i]
        # 끝이 보이면, 그만
        if now_num == 0:
            new_number_line.append(len(temp))
            new_number_line.append(temp[0])
            break
        # 지금 번호가, 원래 들어가 있는거랑 같으면
        if now_num == temp[0]:
            temp.append(now_num)
        # temp에 있는거랑 다르면 / 새로운 값 넣어주기
        else:
            # 4개 이상 쌓여 있었으면 / 그냥 지워주기
            new_number_line.append(len(temp))
            new_number_line.append(temp[0])
            temp = [now_num]
    return new_number_line[:max_len]

dx_attack = [0,1,0,-1]
dy_attack = [1,0,-1,0]

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
index_graph = [[0 for _ in range(n)] for _ in range(n)]

center_x, center_y = n // 2, n // 2
index_graph[center_x][center_y] = -1
max_len = n*n - 1

dx_line = [0,1,0,-1]
dy_line = [-1,0,1,0]

d_line = make_d_line()
number_line = make_pos_line()

total_score = 0
for _ in range(m):
    attack_d, p = map(int,sys.stdin.readline().rstrip().split())
    # 주어진 방향으로 공격
    attack_tower(attack_d, p)
    # 빈공간 채우기
    number_line = del_zero()
    # 4번 이상 반복 나오면, 삭제 (반복)
    while 1:
        end_flag, number_line = del_four_num()
        number_line = number_line + [0 for _ in range(max_len-len(number_line))]
        # 더이상 바꾼게 없다면
        if end_flag == 0:
            break
    # 숫자 끼리 짝 지어주고, 넣어주기
    number_line =  make_set_number()
    number_line = number_line + [0 for _ in range(max_len - len(number_line))]

print(total_score)


