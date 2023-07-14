import sys

def make_direct_string_to_int(order):
    if order == "R":
        return 0
    elif order == "D":
        return 1
    elif order == "L":
        return 2
    elif order == "U":
        return 3

def level_up():
    global total_hp, total_attack, total_defense, now_hp,steel, wapon
    total_hp += 5
    now_hp = total_hp
    total_attack += 2
    total_defense += 2

def update_exp_level(input_exp):
    global exp, level
    exp += int(input_exp*exp_ratio)
    if exp >= level*5:
        level += 1
        exp = 0
        level_up()

def healing_hp():
    global now_hp
    now_hp += 3
    if now_hp >= total_hp:
        now_hp = total_hp

def meet_boss(x,y,name):
    global now_hp, boss_kill_flag, output_string, dead_flag, hero_pos
    boss_attack = dict_attack[name]
    boss_defense = dict_defense[name]
    boss_hp = dict_hp[name]
    boss_exp = dict_exp[name]
    now_hero_attack = max(1, total_attack - boss_defense)
    now_boss_attack = max(1, boss_attack - total_defense)

    Courage_flag = 0
    if "CO" in ring_list:
        Courage_flag = 1
    Dexterity_flag = 0
    if "DX" in ring_list:
        Dexterity_flag =1
    Hunter_flag = 0
    if "HU" in ring_list:
        Hunter_flag = 1
        now_hp = total_hp
    while 1:
        if Courage_flag == 1 and Dexterity_flag == 1:
            boss_hp -= max(1, 3 * total_attack - boss_defense)
            Courage_flag = 0
            Dexterity_flag = 0
        elif Courage_flag == 1:
            boss_hp -= max(1, 2*total_attack - boss_defense)
            Courage_flag = 0
        else:
            boss_hp -= now_hero_attack
        # 보스가 죽음
        if boss_hp <= 0:
            boss_kill_flag = 1
            output_string = "YOU WIN!"
            graph[x][y] = "."
            update_exp_level(boss_exp)
            if "HR" in ring_list:
                healing_hp()
            break
        # HR 이 있으면, 공격 받지 않고 넘어가기
        if Hunter_flag == 1:
            Hunter_flag = 0
            continue
        else:
            now_hp -= now_boss_attack
        # hero가 죽음
        if now_hp <= 0:
            dead_flag = 1
            now_hp = 0
            output_string = "YOU HAVE BEEN KILLED BY "+name+".."
            hero_pos = [-1,-1]
            break
    return

def meet_mon(x,y,name):
    global now_hp, output_string, dead_flag, hero_pos
    mon_attack = dict_attack[name]
    mon_defense = dict_defense[name]
    mon_hp = dict_hp[name]
    mon_exp = dict_exp[name]
    now_hero_attack = max(1, total_attack - mon_defense)
    now_mon_attack = max(1, mon_attack - total_defense)

    Courage_flag = 0
    if "CO" in ring_list:
        Courage_flag = 1
    Dexterity_flag = 0
    if "DX" in ring_list:
        Dexterity_flag =1

    while 1:
        if Courage_flag == 1 and Dexterity_flag == 1:
            mon_hp -= max(1, 3 * total_attack - mon_defense)
            Courage_flag = 0
            Dexterity_flag = 0
        elif Courage_flag == 1:
            mon_hp -= max(1, 2*total_attack - mon_defense)
            Courage_flag = 0
        else:
            mon_hp -= now_hero_attack
        # 몬스터가 죽음
        if mon_hp <= 0:
            graph[x][y] = "."
            update_exp_level(mon_exp)
            if "HR" in ring_list:
                healing_hp()
            break
        now_hp -= now_mon_attack
        # hero가 죽음
        if now_hp <= 0:
            dead_flag = 1
            now_hp = 0
            output_string = "YOU HAVE BEEN KILLED BY "+name+".."
            hero_pos = [-1,-1]
            break
    return

def meet_spike(x,y):
    global now_hp, output_string, dead_flag, hero_pos
    now_hp -= spike_attack
    # hero가 죽음
    if now_hp <= 0:
        dead_flag = 1
        output_string = "YOU HAVE BEEN KILLED BY SPIKE TRAP.."
        hero_pos = [-1, -1]
    return

def reincarnation_hero():
    global hero_pos, now_hp,dead_flag
    ring_list.remove("RE")
    hero_pos = hero_start_pos
    now_hp = total_hp
    dead_flag = 0

def get_ring(type):
    global exp_ratio, spike_attack
    ring_list.append(type)
    if type == "EX":
        exp_ratio *= 1.2
    elif type == "DX":
        spike_attack = 1

def meet_box(x,y,num):
    global total_attack,wapon,total_defense,steel
    box_type = dict_box_info[num][0]
    # 무기인 경우
    if box_type == "W" :
        total_attack -= wapon
        wapon = dict_box_info[num][1]
        total_attack+= wapon
    # 방어구인 경우
    elif box_type == "A":
        total_defense -= steel
        steel = dict_box_info[num][1]
        total_defense+= steel
    elif box_type == "O":
        ring_type = dict_box_info[num][1]
        if len(ring_list) != 4:
            if ring_type not in ring_list:
                get_ring(ring_type)
    graph[x][y] = "."

def move_hero(direct):
    global hero_pos
    x = hero_pos[0] + dx[direct]
    y = hero_pos[1] + dy[direct]

    # 이동한 곳이 벽인 경우 / 못가는 곳인 경우
    h_x, h_y = hero_pos
    if not(0<=x<n and 0<=y<m):
        if graph[h_x][h_y] == "^":
            meet_spike(x, y)
        return
    if graph[x][y] == "#":
        if graph[h_x][h_y] == "^":
            meet_spike(x, y)
        return

    hero_pos = [x, y]
    # 이동한 곳에 아무것도 없는 경우
    if graph[x][y] == ".":
        pass
    # 이동한 곳에 보스가 있던 경우
    elif [x,y] == boss_pos:
        meet_boss(x,y,graph[x][y])
    # 이동한 곳에 가시가 있는 경우
    elif graph[x][y] == "^":
        meet_spike(x,y)
    # 이동한 곳에 상자가 있는 경우
    elif type(graph[x][y]) == type(1):
        meet_box(x,y,graph[x][y])
    # 이동한 곳에 일반 몬스터가 있는 경우
    else:
        meet_mon(x,y,graph[x][y])

n,m = map(int,sys.stdin.readline().rstrip().split())
hero_pos = []
graph = []
mon_count = 0
box_count = 0
for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if graph[i][j] == "M":
            boss_pos = [i,j]
            mon_count += 1
        elif graph[i][j] == "@":
            hero_pos = [i,j]
            graph[i][j] = "."
        elif graph[i][j] == "B":
            box_count += 1
        elif graph[i][j] == "&":
            mon_count += 1

hero_start_pos = hero_pos
order_list = list(sys.stdin.readline().rstrip())

graph_mon = [["" for _ in range(m)] for _ in range(n)]
dict_attack = {}
dict_defense = {}
dict_hp = {}
dict_exp = {}
for _ in range(mon_count):
    input_info = list(sys.stdin.readline().rstrip().split(" "))
    r,c,s,w,a,h,e = int(input_info[0]),int(input_info[1]),input_info[2],int(input_info[3]),int(input_info[4]),int(input_info[5]),int(input_info[6])
    r,c = r-1, c-1
    graph[r][c] = s
    dict_attack[s] = w
    dict_defense[s] = a
    dict_hp[s] = h
    dict_exp[s] = e

graph_box = [["" for _ in range(m)] for _ in range(n)]
dict_box_info = {}
for num in range(1,box_count+1):
    input_info = list(sys.stdin.readline().rstrip().split(" "))
    r,c,t,s = int(input_info[0]),int(input_info[1]),input_info[2],input_info[3]
    r,c = r-1, c-1
    graph[r][c] = num
    if t == "W" :
        dict_box_info[num] = [t, int(s)]
    elif t == "A":
        dict_box_info[num] = [t, int(s)]
    elif t == "O":
        dict_box_info[num] = [t,s]

hp,attack,defense = 20,2,2
now_hp, total_hp = hp,hp
wapon, total_attack = 0,attack
steel, total_defense = 0, defense
ring_list = []
level = 1
exp = 0
exp_ratio = 1
boss_kill_flag = 0
dead_flag = 0
output_string = ""

spike_attack = 5


dx = [0,1,0,-1]
dy = [1,0,-1,0]

turn = 0
for order in order_list:
    turn += 1
    direct = make_direct_string_to_int(order)
    move_hero(direct)
    if boss_kill_flag == 1:
        break
    if dead_flag == 1:
        if "RE" in ring_list:
            reincarnation_hero()
            continue
        break
    output_string = "Press any key to continue."

for i in range(n):
    for j in range(m):
        if [i,j] == hero_pos:
            print("@",end = "")
            continue
        elif [i, j] == boss_pos:
            print("M", end="")
        elif type(graph[i][j]) == type(1):
            print("B",end = "")
        elif graph[i][j] == "#":
            print("#",end = "")
        elif graph[i][j] == "^" or graph[i][j] == ".":
            print(graph[i][j],end = "")
        else:
            print("&", end="")
    print()

print("Passed Turns : {}".format(turn))
print("LV : {}".format(level))
print("HP : {}/{}".format(now_hp,total_hp))
print("ATT : {}+{}".format(total_attack-wapon, wapon))
print("DEF : {}+{}".format(total_defense-steel, steel))
print("EXP : {}/{}".format(exp, level*5))
print(output_string)