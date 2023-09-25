import sys
from collections import deque, defaultdict


def check_other(num,x,y):
    for check_num in range(1, m + 1):
        if check_num != num:
            if dict_pos[check_num] == [x,y]:
                return check_num
    return -1


def get_gun(num, x, y):
    global dict_pos, dict_gun, dict_stat, dict_score
    now_gun = dict_gun[num]
    now_stat = dict_stat[num]
    now_first_stat = dict_first_stat[num]

    new_gun_list = graph_gun[x][y]
    # no gun
    if new_gun_list == []:
        pass
    else:
        new_gun_list.sort()
        new_gun = new_gun_list[-1]
        new_gun_list = new_gun_list[:-1]
        # change gun
        if new_gun > now_gun:
            # update graph
            if now_gun != 0:
                new_gun_list = new_gun_list + [now_gun]
            graph_gun[x][y] = new_gun_list
            dict_gun[num] = new_gun
            dict_stat[num] = now_first_stat + new_gun
        else:
            pass


def start_fight(first, second):
    global dict_pos, dict_gun, dict_stat, dict_score
    winner, loser = -1, -1
    first_total_stat = dict_stat[first]
    first_first_stat = dict_first_stat[first]
    second_total_stat = dict_stat[second]
    second_first_stat = dict_first_stat[second]
    if first_total_stat > second_total_stat:
        winner = first
        loser = second
    elif first_total_stat < second_total_stat:
        winner = second
        loser = first
    else:
        if first_first_stat > second_first_stat:
            winner = first
            loser = second
        elif first_first_stat < second_first_stat:
            winner = second
            loser = first
    # get socre
    dict_score[winner] += abs(first_total_stat - second_total_stat)
    return winner, loser

def drop_gun(num,x,y):
    now_gun = dict_gun[num]
    dict_gun[num] = 0
    dict_stat[num] = dict_first_stat[num]
    if now_gun != 0:
        graph_gun[x][y] = graph_gun[x][y]+[now_gun]

def move_loser(num):
    global dict_pos, dict_gun, dict_stat, dict_score
    now_x, now_y = dict_pos[num]
    now_direct = dict_direct[num]
    for i in range(4):
        new_direct = (now_direct + i) % 4
        nx = now_x + dx[new_direct]
        ny = now_y + dy[new_direct]
        if 0 <= nx < n and 0 <= ny < n:
            if check_other(num,nx,ny) == -1:
                dict_direct[num] = new_direct
                dict_pos[num] = [nx, ny]
                get_gun(num, nx, ny)
                return


def move_people(num):
    global dict_pos, dict_gun, dict_stat, dict_score
    now_x, now_y = dict_pos[num]
    now_direct = dict_direct[num]
    nx = now_x + dx[now_direct]
    ny = now_y + dy[now_direct]
    if not (0 <= nx < n and 0 <= ny < n):
        # change direct
        new_direct = (now_direct + 2) % 4
        dict_direct[num] = new_direct
        now_direct = new_direct
        nx = now_x + dx[now_direct]
        ny = now_y + dy[now_direct]
    dict_pos[num] = [nx, ny]
    # check other people
    other_num = check_other(num,nx,ny)
    # only me
    if other_num == -1:
        get_gun(num, nx, ny)
    # need fight
    else:
        winner, loser = start_fight(num, other_num)
        # drop gun -loser
        drop_gun(loser,nx,ny)
        # move_loser
        move_loser(loser)
        # winner get gun
        get_gun(winner, nx, ny)

def show_info():
    for g in graph_gun:
        print(g)
    print("dict_pos: ", dict(dict_pos))
    print("dict_stat: ", dict(dict_stat))
    print("dict_gun: ", dict(dict_gun))
    print("dict_score: ", dict(dict_score))

def simulation():
    global dict_pos, dict_gun, dict_stat, dict_score
    for turn in range(1, k + 1):
        # move p
        for num in range(1, m + 1):
            move_people(num)



n, m, k = map(int, sys.stdin.readline().rstrip().split())
graph_gun = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if temp[j] != 0:
            graph_gun[i][j].append(temp[j])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dict_pos = defaultdict(lambda: [-1, -1])
dict_direct = defaultdict(lambda: 0)
dict_first_stat = defaultdict(lambda: 0)
dict_stat = defaultdict(lambda: 0)
dict_gun = defaultdict(lambda: 0)
dict_score = defaultdict(lambda: 0)

for num in range(1, m + 1):
    x, y, d, s = map(int, sys.stdin.readline().rstrip().split())
    x -= 1
    y -= 1
    dict_pos[num] = [x, y]
    dict_direct[num] = d
    dict_first_stat[num] = s
    dict_stat[num] = s
    dict_gun[num] = 0
    dict_score[num] = 0

simulation()
for num in range(1, m + 1):
    print(dict_score[num], end=" ")

    """
5 4 1
1 2 0 1 2
1 0 3 3 1
1 3 0 2 3
2 1 2 4 5
0 1 3 2 0
1 3 2 3
2 2 1 5
3 3 2 2
5 1 3 4
    """