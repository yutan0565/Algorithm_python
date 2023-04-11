import sys
from collections import defaultdict

def get_gun(x,y,num):
    now_gun  = dict_gun[num]
    gun_list = graph_gun[x][y]
    if len(gun_list) != 0:
        gun_list.sort()
        other_gun = gun_list[-1]
        if other_gun > now_gun:
            dict_gun[num] = other_gun
            dict_stat[num] = dict_first_stat[num] + other_gun
            if now_gun != 0:
                gun_list = gun_list[:-1] + [now_gun]
            else:
                gun_list = gun_list[:-1]
            graph_gun[x][y] = gun_list

def fight(first,second):
    winner,loser = 0,0
    if dict_stat[first] > dict_stat[second]:
        winner = first
        loser = second
    elif dict_stat[first] < dict_stat[second]:
        winner = second
        loser = first
    elif dict_stat[first] == dict_stat[second]:
        if dict_first_stat[first] > dict_first_stat[second]:
            winner = first
            loser = second
        elif dict_first_stat[first] < dict_first_stat[second]:
            winner = second
            loser = first
    return winner, loser

def put_gun(x,y,num):
    now_gun  = dict_gun[num]
    gun_list = graph_gun[x][y]
    if now_gun != 0:
        gun_list = gun_list + [now_gun]
        dict_gun[num] = 0
        dict_stat[num] = dict_first_stat[num]
        graph_gun[x][y] = gun_list

def loser_move(num):
    # 총 내려두기, 원래 방향으로 이동(다른 사람 있으면, 90 도 돌면서 빈칸 보이면 이동), 총줍기
    now_direct = dict_direct[num]
    x,y = dict_pos[num]
    put_gun(x, y, num)
    for plus in range(4):
        new_direct = (now_direct + plus) % 4
        nx = x + dx[new_direct]
        ny = y + dy[new_direct]
        if 0 <= nx < n and 0 <= ny < n:
            if graph_pos[nx][ny] == 0:
                graph_pos[nx][ny] = num
                dict_pos[num] = [nx, ny]
                dict_direct[num] = new_direct
                get_gun(nx, ny, num)
                break

def move_people():
    for num in range(1,m+1):
        x,y = dict_pos[num]
        now_direct = dict_direct[num]

        nx = x + dx[now_direct]
        ny = y + dy[now_direct]
        if not(0<=nx<n and 0<=ny<n):
            now_direct = (now_direct+2)%4
            dict_direct[num] = now_direct
            nx = x + dx[now_direct]
            ny = y + dy[now_direct]
        graph_pos[x][y] = 0
        dict_pos[num] = [nx,ny]
        # 이동하는 곳에 아무도 없는 경우
        if graph_pos[nx][ny] == 0:
            graph_pos[nx][ny] = num
            get_gun(nx,ny,num)
        # 다른 사람이 있으면 싸우기
        else:
            other_num = graph_pos[nx][ny]
            winner, loser = fight(num,other_num)
            dict_score[winner] += (dict_stat[winner] - dict_stat[loser])
            # 진사람
            loser_move(loser)
            # 이긴 사람
            # 총 획득 / 점수 획득
            if winner == num:
                graph_pos[nx][ny] = num
            get_gun(nx,ny,winner)

n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph_pos = [[0 for _ in range(n)] for _ in range(n)]
graph_gun = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    temp = list( map(int,sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if temp[j] != 0:
            graph_gun[i][j].append(temp[j])

dx = [-1,0,1,0]
dy = [0,1,0,-1]


dict_pos = defaultdict(lambda :[])
dict_direct = defaultdict(lambda :-1)
dict_first_stat = defaultdict(lambda :-1)
dict_gun = defaultdict(lambda :-1)
dict_stat = defaultdict(lambda :-1)

dict_score = defaultdict(lambda :0)

for num in range(1,m+1):
    x,y,d,s =  map(int,sys.stdin.readline().rstrip().split())
    x,y,d = x-1,y-1,d
    dict_pos[num] = [x,y]
    graph_pos[x][y] = num
    dict_direct[num] = d
    dict_first_stat[num] = s
    dict_gun[num] = 0
    dict_stat[num] = s
    dict_score[num] = 0

for round in range(1,k+1):
    # 사람 움직임
    move_people()

for c in dict_score.values():
    print(c,end=" ")