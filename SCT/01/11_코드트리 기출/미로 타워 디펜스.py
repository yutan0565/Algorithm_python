import sys


def make_line():
    dx_line, dy_line = [], []
    direct = 0
    count = 1
    while 1:
        for _ in range(2):
            for _ in range(count):
                dx_line.append(dx[direct])
                dy_line.append(dy[direct])
                if len(dx_line) == n*n-1:
                    return dx_line, dy_line
            direct = (direct + 1)%4
        count += 1

def make_monster_list():
    x,y = tower_x, tower_y
    list_monster = []
    for i in range(len(dx_line)):
        x = x + dx_line[i]
        y = y + dy_line[i]
        if not(0<=x<n and 0<=y<n) or graph[x][y] == 0:
            return list_monster
        list_monster.append(graph[x][y])
    return list_monster

def make_pos_list():
    x,y = tower_x, tower_y
    list_pos = []
    for i in range(len(dx_line)):
        x = x + dx_line[i]
        y = y + dy_line[i]
        list_pos.append([x,y])
    return list_pos

def make_attack_list(d,p):
    x,y = tower_x, tower_y
    attack_list = []
    for _ in range(p):
        x = x + dx_attack[d]
        y = y + dy_attack[d]
        attack_list.append([x,y])
    return attack_list

def kill_monster(attack_list):
    global result
    list_temp_monster = []
    for i in range(len(list_monster)):
        check_pos = list_pos[i]
        if check_pos in attack_list:
            result += list_monster[i]
            continue
        else:
            list_temp_monster.append(list_monster[i])
    return list_temp_monster

def del_monster():
    global  list_monster, result
    list_monster += [-1]
    new_list_monster = []
    temp = [list_monster[0]]
    check_number = list_monster[0]
    flag = 0
    for i in range(1,len(list_monster)):
        now_number = list_monster[i]
        if now_number == check_number:
            temp.append(now_number)
        elif now_number != check_number:
            check_number = now_number
            if len(temp) < 4:
                new_list_monster += temp
            else:
                result += sum(temp)
                flag = 1
            temp = []
            temp.append(now_number)
    return new_list_monster, flag

def couple_monster():
    global  list_monster
    list_monster += [-1]
    new_list_monster = []
    check_number = list_monster[0]
    count = 1
    for i in range(1, len(list_monster)):
        now_number = list_monster[i]
        if now_number == check_number:
            count += 1
        elif now_number != check_number:
            new_list_monster.append(count)
            new_list_monster.append(check_number)
            if len(new_list_monster) >= n*n-1:
                break
            check_number = now_number
            count = 1
    return new_list_monster[:n*n-1]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

dx_attack = [0,1,0,-1]
dy_attack = [1,0,-1,0]

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
tower_x,tower_y = n//2, n//2

dx_line, dy_line = make_line()
list_monster = make_monster_list()
list_pos = make_pos_list()
result = 0

for _ in range(m):
    d,p = map(int, sys.stdin.readline().rstrip().split())
    attack_list = make_attack_list(d,p)

    list_monster = kill_monster(attack_list)
    while 1:
        list_monster, flag = del_monster()
        if flag == 0:
            break
    list_monster = couple_monster()
print(result)
