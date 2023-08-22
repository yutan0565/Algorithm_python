import copy
import sys

def make_mon_full():
    global mon_line
    now_len = len(mon_line)
    mon_line = mon_line + [0 for _ in range(n*n-1-now_len)]

def make_line_pos():
    direct = 0
    count = 1
    d_list = []
    while 1:
        for _ in range(2):
            for _ in range(count):
                d_list.append(direct)
            direct = (direct + 1) %4
        count += 1
        if len(d_list) >= n * n - 1:
            break
    d_list = d_list[:n*n-1]
    x,y = center_x,center_y
    mon_line = []
    graph_index[x][y] = -1
    index = 0
    for d in d_list:
        x = x + dx_line[d]
        y = y + dy_line[d]
        mon_line.append(graph[x][y])
        graph_index[x][y] = index
        index += 1
    return mon_line

def attack_monster(attack_direct, p):
    global total_score
    attack_index = []
    x,y = center_x,center_y
    for plus in range(1,p+1):
        x = x + dx[attack_direct]
        y = y + dy[attack_direct]
        if 0<=x<n and 0<=y<n:
            attack_index.append(graph_index[x][y])
    new_mon_line = []
    for index in range(len(mon_line)):
        if index not in attack_index:
            new_mon_line.append(mon_line[index])
        else:
            total_score += mon_line[index]
    return new_mon_line

def del_same_mon():
    global total_score
    new_mon_line = []
    temp = []
    del_flag = 0
    for index in range(n*n-1):
        now_mon = mon_line[index]
        # 아무것도 없는 경우
        if len(temp) == 0:
            temp.append(now_mon)
            continue
        # 지울거 다 지운 경우 (0은 끝임) - 마지막 temp만 처리 해주기
        elif now_mon == 0:
            if len(temp) >= 4:
                total_score += sum(temp)
                del_flag = 1
                break
            else:
                new_mon_line = new_mon_line + temp
                break
        else:
            # temp에 있는거랑 같음
            if now_mon == temp[0]:
                temp.append(now_mon)
            # temp에 있는거랑 다름
            else:
                # temp가 4 이상이면
                if len(temp) >= 4:
                    total_score += sum(temp)
                    temp = []
                    temp.append(now_mon)
                    del_flag = 1
                else:
                    new_mon_line = new_mon_line + temp
                    temp = []
                    temp.append(now_mon)
    return new_mon_line, del_flag

def remap_mon():
    new_mon_line = []
    temp = []
    for index in range(n*n-1):
        now_mon = mon_line[index]
        # 아무것도 없는 경우
        if len(temp) == 0:
            temp.append(now_mon)
            continue
        # 지울거 다 지운 경우 (0은 끝임) - 마지막 temp만 처리 해주기
        elif now_mon == 0:
            count = len(temp)
            num = temp[0]
            new_mon_line = new_mon_line + [count, num]
            break
        else:
            # temp에 있는거랑 같음
            if now_mon == temp[0]:
                temp.append(now_mon)
            # temp에 있는거랑 다름
            else:
                count = len(temp)
                num = temp[0]
                new_mon_line = new_mon_line + [count, num]
                temp = []
                temp.append(now_mon)
    if len(new_mon_line) > n*n-1:
        new_mon_line = new_mon_line[:n*n-1]
    return new_mon_line

n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_index = [[0 for _ in range(n)] for _ in range(n)]

center_x, center_y = n//2, n//2

dx_line = [0,1,0,-1]
dy_line = [-1,0,1,0]
mon_line = make_line_pos()

dx = [0,1,0,-1]
dy = [1,0,-1,0]

total_score = 0
for round in range(1, m+1):
    attack_direct, p = map(int,sys.stdin.readline().rstrip().split())
    # 몬스터 공격
    mon_line = attack_monster(attack_direct, p)
    make_mon_full()
    # 중복되는 목스터 제거
    while 1:
        mon_line, del_flag = del_same_mon()
        make_mon_full()
        if del_flag == 0:
            break
    # 재 배열 해주기
    mon_line = remap_mon()
    make_mon_full()
print(total_score)

"""
7 7
0 0 0 0 0 0 0 
0 0 0 0 0 0 0 
0 3 2 2 1 3 0 
0 3 3 0 2 3 0 
0 1 3 3 3 1 0 
0 2 3 2 2 2 0 
0 0 0 0 0 0 0 
0 3
2 3
2 3
3 1
2 2
1 1
2 3
"""