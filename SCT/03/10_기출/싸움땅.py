import sys

def get_gun(x,y,num):
    # 자리에 총이 없음
    if graph_gun[x][y] == []:
        pass
    else:
        now_gun = dict_gun[num]
        gun_list = graph_gun[x][y]
        gun_list.sort()
        new_gun = gun_list[-1]

        # 지금 총이 더 좋음
        if now_gun >= new_gun:
            pass
        # 새로운게 더 좋음 / 내꺼랑 바꾸기
        else:
            if now_gun != 0:
                new_gun_list = gun_list[:-1] + [now_gun]
            else:
                new_gun_list = gun_list[:-1]
            graph_gun[x][y] = new_gun_list
            # 그 사람 초 정보 업데이트 / total 스텟 업데이트
            dict_gun[num] = new_gun
            dict_total_stat[num] = new_gun + dict_first_stat[num]

def fight_start(first, second):
    winner, loser = 0,0
    if dict_total_stat[first] > dict_total_stat[second]:
        winner = first
        loser = second
    elif dict_total_stat[first] < dict_total_stat[second]:
        winner = second
        loser = first
    elif dict_total_stat[first] == dict_total_stat[second]:
        # 초기 스탯 비교
        if dict_first_stat[first] > dict_first_stat[second]:
            winner = first
            loser = second
        elif dict_first_stat[first] < dict_first_stat[second]:
            winner = second
            loser = first
    return winner, loser

def drop_gun(x,y,num):
    now_gun = dict_gun[num]
    graph_gun[x][y].append(now_gun)
    dict_gun[num] = 0
    dict_total_stat[num] = dict_first_stat[num]

def  loser_find_new_way(x,y,num):
    now_direct = dict_direct[num]
    for plus in range(4):
        new_direct = (now_direct + plus)%4
        nx = x + dx[new_direct]
        ny = y + dy[new_direct]
        if 0<=nx<n and 0<=ny<n:
            if [nx,ny] not in list(dict_pos.values()):
                dict_direct[num] = new_direct
                dict_pos[num] = [nx,ny]
                get_gun(nx,ny,num)
                break

def move_people(num):
    # 현재 사람의 정보
    now_x, now_y = dict_pos[num]
    now_direct = dict_direct[num]

    # 이동 할 곳
    nx = now_x + dx[now_direct]
    ny = now_y + dy[now_direct]
    # 벽이면 방향 바꾸기
    if not(0<=nx<n and 0<=ny<n):
        dict_direct[num] = (now_direct + 2)%4
        now_direct = dict_direct[num]
        nx = now_x + dx[now_direct]
        ny = now_y + dy[now_direct]

    fight_flag = 0
    # 위치 변환 / 총 줍기
    dict_pos[num] = [nx,ny]
    for other_num in range(1, m+1):
        if other_num != num: # 나 자신이 아님
            if [nx,ny] == dict_pos[other_num]: # 위치가 겹친다면
                # 싸움 시작
                winner, loser = fight_start(num, other_num)
                gap = dict_total_stat[winner] - dict_total_stat[loser]
                # loser 가 총을 버리고 / 새로운 길을 찾아 떠남
                drop_gun(nx,ny,loser)
                loser_find_new_way(nx,ny,loser)
                # winner 가 총을 새로 주움 / 점수 획득
                get_gun(nx,ny,winner)
                dict_score[winner] += gap
                fight_flag = 1
    if fight_flag == 0:
        get_gun(nx, ny, num)

n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph_gun = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if temp[j] != 0:
            graph_gun[i][j].append(temp[j])

dx = [-1,0,1,0]
dy = [0,1,0,-1]

dict_pos = {}
dict_first_stat = {}
dict_total_stat = {}
dict_gun = {}
dict_direct = {}
dict_score = {}

def show_info():
    print("===================")
    print("위치 : ",dict_pos)
    print("방향 : ",dict_direct)
    print("총 : ",dict_gun)
    print("스탯 :",dict_total_stat)
    print("점수 : ",dict_score)

for num in range(1, m+1):
    x,y,d,s = map(int,sys.stdin.readline().rstrip().split())
    x,y = x-1,y-1
    dict_pos[num] = [x,y]
    dict_direct[num] = d
    dict_first_stat[num] = s
    dict_total_stat[num] = s
    dict_gun[num] = 0
    dict_score[num] = 0

# show_info()
for round in range(1, k+1):
    # print("============================================================")
    # print("round : ", round)
    # 1번 부터 이동하기
    for num in range(1, m+1):
        move_people(num)
        # show_info()
    # for g in graph_gun:
    #     print(g)

for score in dict_score.values():
    print(score, end = " ")

# 첫번재 플레이어 부터 순차적으로 이동

    # 플레이어 없음 / 총 비교 후 줍기

    # 플레이어 있음 / 스탯 비교 / 초기 능력치 비교

        # 이긴 애 : 점수차만큼 점수 획득

        # 진 애 : 총 내려놓고, 원래 있던 방향으로 이동 / 다른 플레/격자 밖이면 90도 회전
