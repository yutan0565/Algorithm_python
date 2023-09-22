import sys
from collections import defaultdict


def make_graph_people():
    graph_people = [[[] for _ in range(n)] for _ in range(n)]
    for num in range(1, m+1):
        a,b = dict_pos[num]
        graph_people[a][b].append(num)
    return graph_people


def get_gun(num,x,y):
    now_gun = dict_gun[num]
    gun_list = graph_gun[x][y]
    if len(gun_list) != 0:
        gun_list.sort()
        top_gun = gun_list[-1]
        # 떨어진게 좋은 경우
        if now_gun < top_gun:
            dict_gun[num] = top_gun
            dict_total_stat[num] = dict_start_stat[num] + top_gun

            if now_gun != 0:
                gun_list =  gun_list[:-1] +[now_gun]
            else:
                gun_list = gun_list[:-1]
            graph_gun[x][y] = gun_list

def fight_people(first, second):
    winner = 0
    loser = 0

    first_total_stat = dict_total_stat[first]
    first_start_stat = dict_start_stat[first]

    second_total_stat = dict_total_stat[second]
    second_start_stat = dict_start_stat[second]

    gap = abs(first_total_stat - second_total_stat)

    if first_total_stat > second_total_stat:
        winner = first
        loser = second
    elif first_total_stat < second_total_stat:
        winner = second
        loser = first
    else:
        if first_start_stat > second_start_stat:
            winner = first
            loser = second
        elif first_start_stat < second_start_stat:
            winner = second
            loser = first

    return winner, loser , gap

def drop_gun(num,x,y):
    now_gun = dict_gun[num]
    dict_gun[num] = 0
    dict_total_stat[num] -= now_gun
    if now_gun != 0:
        graph_gun[x][y].append(now_gun)

def move_loser(num,x,y):
    now_direct = dict_direct[num]
    for d in range(4):
        new_direct = (now_direct + d)%4
        nx = x + dx[new_direct]
        ny = y + dy[new_direct]
        # 격자 안이고, 다른 사람이 없는 경우
        if 0<=nx<n and 0<=ny<n:
            if graph_people[nx][ny] == 0:
                # 위치, 방향, 총 줍기
                graph_people[nx][ny] = num
                dict_pos[num] = [nx,ny]
                dict_direct[num] = new_direct
                get_gun(num,nx,ny)
                break

def show_info():
    print("사람")
    for g in graph_people:
        print(g)
    print("총")
    for g in graph_gun:
        print(g)
    print("위치 : ", dict(dict_pos))
    print("총 : ", dict(dict_gun))
    print("방향 : ", dict(dict_direct))
    print("스탯 : ", dict(dict_total_stat))

def simulation():
    for round in range(1, k+1):

        # 첫번째 플레이어부터 순차적으로 이동
        for num in range(1, m+1):

            x, y = dict_pos[num]
            now_direct = dict_direct[num]
            new_direct = now_direct
            nx = x + dx[new_direct]
            ny = y + dy[new_direct]

            # 격자를 벗어나는 경우
            if not (0 <= nx < n and 0 <= ny < n):
                new_direct = (now_direct + 2) % 4
                nx = x + dx[new_direct]
                ny = y + dy[new_direct]
            dict_direct[num] = new_direct
            dict_pos[num] = [nx,ny]

            # 움직인 자리에 다른 사람 있는지 확인 하기
            # 사람이 없는 경우
            if graph_people[nx][ny] == 0:
                # 위치 변화, 총 줍기
                graph_people[x][y] = 0
                graph_people[nx][ny] = num
                dict_pos[num] = [nx,ny]
                get_gun(num, nx,ny)
            # 사람이 있는 경우
            else:
                other_num = graph_people[nx][ny]
                other_x,other_y = dict_pos[other_num]

                # 둘다 기존위치 지우기
                graph_people[x][y] = 0
                graph_people[other_x][other_y] = 0

                winner, loser, gap = fight_people(num, other_num)
                # 승자는 포인트를 얻음
                score_list[winner] += gap

                # 진 플레이어
                # 총 내려두고, 이동
                drop_gun(loser,nx,ny)
                move_loser(loser, nx,ny)

                # 이긴 사람
                graph_people[nx][ny] = winner
                dict_pos[winner] = [nx,ny]
                get_gun(winner,nx,ny)



# 격자 크기, 플레이어수, 라운드 수
n,m,k = map(int,sys.stdin.readline().rstrip().split())

graph_people = [[0 for _ in range(n)] for _ in range(n)]
graph_gun = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if temp[j] >= 1:
            graph_gun[i][j].append(temp[j])

dx = [-1,0,1,0]
dy = [0,1,0,-1]

dict_pos = defaultdict(lambda : [-1,-1])
dict_direct = defaultdict(lambda : 0)
dict_start_stat = defaultdict(lambda : 0)
dict_gun = defaultdict(lambda : 0)
dict_total_stat = defaultdict(lambda : 0)

score_list = [0 for _ in range(m+1)]
live_list = [1 for _ in range(m+1)]
live_list[0] = 0

for num in range(1, m+1):
    x,y,d,s = map(int,sys.stdin.readline().rstrip().split())
    graph_people[x-1][y-1] = num
    dict_pos[num] = [x-1,y-1]
    dict_direct[num] = d
    dict_start_stat[num] = s
    dict_gun[num] = 0
    dict_total_stat[num] = dict_start_stat[num] + dict_gun[num]

simulation()

for num in range(1,m+1):
    print(score_list[num], end = " ")


"""
5 4 6
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