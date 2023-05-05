from collections import deque
import sys

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def move(peo):
    x = dict_pos[peo][0]
    y = dict_pos[peo][1]
    direct = dict_direct[peo]

    nx = x + dx[direct]
    ny = y + dy[direct]

    if not(0<=nx<n and 0<=ny<n):
        dict_direct[peo] = (direct + 2)%4
        direct = dict_direct[peo]
        nx = x + dx[direct]
        ny = y + dy[direct]

    visited[x][y] = -1
    dict_pos[peo] = [nx,ny]


def drop_gun(peo):
    x = dict_pos[peo][0]
    y = dict_pos[peo][1]
    now_gun = dict_now_gun[peo]

    dict_now_gun[peo] = 0
    gun_list = graph[x][y]
    gun_list.append(now_gun)
    graph[x][y] = gun_list
    dict_stat[peo] = dict_first_stat[peo]

def get_gun(peo):
    x = dict_pos[peo][0]
    y = dict_pos[peo][1]
    now_gun = dict_now_gun[peo]

    gun_list = graph[x][y]
    gun_list.sort()
    max_gun = gun_list[-1]
    if now_gun < max_gun:
        dict_now_gun[peo] = max_gun
        gun_list[-1] = now_gun
        graph[x][y] = gun_list
    dict_stat[peo] = dict_first_stat[peo] + dict_now_gun[peo]
    visited[x][y] = peo


def compare(first, second):
    winner = 0
    losser = 0
    if dict_stat[first] < dict_stat[second]:
        winner = second
        losser = first
    elif dict_stat[first] > dict_stat[second]:
        winner = first
        losser = second
    else:
        if dict_first_stat[first] < dict_first_stat[second]:
            winner = second
            losser = first
        elif dict_first_stat[first] > dict_first_stat[second]:
            winner = first
            losser = second
    return winner, losser

def move_losser(peo):
    x = dict_pos[peo][0]
    y = dict_pos[peo][1]

    for i in range(4):
        direct = (dict_direct[peo] + i) % 4
        nx = x + dx[direct]
        ny = y + dy[direct]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == -1:
                visited[x][y] = -1
                dict_direct[peo] = direct
                dict_pos[peo] = [nx, ny]
                break


def find_result():
    for round in range(1, k+1):
        # 한명 씩 모두 이동
        for peo in range(1, m+1):
            #총 줍기
            move(peo)
            # 이동한 곳이 빈 칸
            if visited[dict_pos[peo][0]][dict_pos[peo][1]] == -1:
                #총 줍기
                get_gun(peo)
            # 이동한 곳에 다른거 존재
            elif visited[dict_pos[peo][0]][dict_pos[peo][1]] != -1:
                # 싸움
                winner, losser = compare(peo, visited[dict_pos[peo][0]][dict_pos[peo][1]])
                # 점수 올리기
                score_list[winner-1] += (dict_stat[winner] - dict_stat[losser])
                # 진사람
                drop_gun(losser)
                move_losser(losser)
                get_gun(losser)

                # 이긴 사람
                get_gun(winner)

n,m,k = map(int, sys.stdin.readline().rstrip().split())
graph = [[[0] for _ in range(n)] for _ in range(n) ]
for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(n):
        graph[i][j].append(temp[j])

visited = [[-1 for _ in range(n)] for _ in range(n)]
dict_pos = {}
dict_direct = {}
dict_first_stat = {}
dict_stat = {}
dict_now_gun = {}


score_list = [0 for _ in range(m)]
for i in range(1,m+1):
    a,b,c,d = map(int,sys.stdin.readline().rstrip().split())
    visited[a-1][b-1] = i
    dict_pos[i] = [a-1,b-1]
    dict_direct[i] = c
    dict_first_stat[i] = d
    dict_stat[i] = d
    dict_now_gun[i] = 0

find_result()
for s in score_list:
    print(s, end = " ")


"""
2 3 8
0 0
0 0
1 2 0 3
2 2 3 5
1 1 3 2
"""