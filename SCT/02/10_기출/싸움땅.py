import sys

def get_gun(x,y,number):
    if len(graph_gun[x][y]) != 0: # 총이 있는 경우에만
        gun_list = graph_gun[x][y]
        gun_list.sort()
        best_gun = gun_list[-1]
        now_gun = dict_gun[number]
        # 내가 가진게 더 큰 경우
        if now_gun > best_gun:
            pass
        # 줍는게 더 큰 경우
        elif now_gun < best_gun:
            dict_stat[number] -= now_gun
            dict_stat[number] += best_gun
            dict_gun[number] = best_gun

            new_gun_list = gun_list[:-1]
            if now_gun != 0:
                new_gun_list = new_gun_list + [now_gun]
            graph_gun[x][y] = new_gun_list

def fight(first, second):
    winer, loser = 0, 0
    if dict_stat[first] > dict_stat[second]:
        winer = first
        loser = second
    elif dict_stat[first] < dict_stat[second]:
        winer = second
        loser = first

    elif dict_stat[first] == dict_stat[second]:
        if dict_first_stat[first] > dict_first_stat[second]:
            winer = first
            loser = second
        elif dict_first_stat[first] < dict_first_stat[second]:
            winer = second
            loser = first
    return winer, loser

def loser_find_pos(number):
    now_x = dict_pos[number][0]
    now_y = dict_pos[number][1]

    now_direct = dict_direct[number]
    for new_d_plus in range(4):
        new_direct = (now_direct +new_d_plus) % 4
        nx = now_x + dx[new_direct]
        ny = now_y + dy[new_direct]
        if 0 <= nx < n and 0 <= ny < n:
            if [nx,ny] not in dict_pos.values():
                dict_direct[number] = new_direct
                dict_pos[number] = [nx,ny]
                get_gun(nx,ny,number)
                break

def get_score(winer, loser):
    gap = dict_stat[winer] - dict_stat[loser]
    dict_score[winer] += gap

def put_gun(number,x,y):
    now_gun = dict_gun[number]
    dict_stat[number] -= now_gun
    dict_gun[number] = 0
    if now_gun == 0:
        pass
    else:
        graph_gun[x][y].append(now_gun)

def move_people(number):
    now_x = dict_pos[number][0]
    now_y = dict_pos[number][1]

    now_direct = dict_direct[number]
    nx = now_x + dx[now_direct]
    ny = now_y + dy[now_direct]

    # 벽이 있으면
    if not(0<=nx<n and 0<=ny<n):
        now_direct = (now_direct+2)%4
        dict_direct[number] = now_direct
        nx = now_x + dx[now_direct]
        ny = now_y + dy[now_direct]
    # 일단은 새로운 장소로 이동
    dict_pos[number] = [nx,ny]

    # 이동한 곳에 사람이 있는지 체크 하기
    fight_flag = 0
    for other_number in range(1, m+1):
        if other_number != number: # 나 자신이 아니고
            # 만약 위치가 같은 사람이 있다면
            if dict_pos[other_number] == [nx,ny]:
                winer, loser = fight(number, other_number)
                # 승자 점수
                get_score(winer, loser)
                # 패자 이동
                put_gun(loser,nx,ny)
                loser_find_pos(loser)
                get_gun(nx,ny,winer)

                fight_flag = 1
                break
    # 아무도 없다면
    if fight_flag == 0:
        get_gun(nx,ny,number)

n,m,k = map(int,sys.stdin.readline().rstrip().split())
dict_pos = {}
dict_direct = {}
dict_stat = {}
dict_gun = {}

dict_first_stat = {}
dict_score = {}

dx = [-1,0,1,0]
dy = [0,1,0,-1]

graph_gun = []
for i in range(n):
    gun = list(map(int, sys.stdin.readline().rstrip().split()))
    temp_graph = []
    for j in range(n):
        if gun[j] == 0:
            temp_graph.append([])
        else:
            temp_graph.append([gun[j]])
    graph_gun.append(temp_graph)

graph_pos = [[[] for _ in range(n)] for _ in range(n)]
for number in range(1, m+1):
    x,y,d,s = map(int,sys.stdin.readline().rstrip().split())
    dict_pos[number] = [x-1, y-1]
    dict_direct[number] = d
    dict_first_stat[number] = s
    dict_stat[number] = s
    dict_score[number] = 0
    dict_gun[number] = 0 # 총이 없는 상태

def show_info(round):
    print(round)
    for g in graph_gun:
        print(g)
    temp_pos = [[0 for _ in range(n)] for _ in range(n)]
    for number in range(1,m+1):
        x,y = dict_pos[number][0], dict_pos[number][1]
        temp_pos[x][y] = number
    print("-----------")
    for g in temp_pos:
        print(g)
    print("-----------")
    print("처음",dict_first_stat)
    print("지금",dict_stat)
    print("총",dict_gun)

for round in range(1, k+1):
    # 본인이 향한 방향대로 한칸 이동 / 벽 만나면 반대로 이동
    for number in range(1, m+1):
        move_people(number)
        # show_info(round)

    # 플레이어 체크
        # 있다면 싸움 시작
            #  총 능력 비교 (같으면, 초기 스탯 비교)
                # 이긴 사람 : 총 능력치 차이만큼 포인트 획득 / 총 줍기
                # 진 사람 : 총 내려두고, 원래 방향으로 이동 / 플레이어 있으면 회전 / 총 줍기

        # 없다면
            # 총을 획득,  이미 총이 있으면, 더 큰거 가져감 / 나머지 버림


for number in range(1, m+1):
    print(dict_score[number], end = " ")

