import sys
from collections import deque


def select_attacker_best(now_time):
    max_value = -1
    min_value = 2e10
    # find min_value, max_value
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                min_value = min(min_value, graph[i][j])
                max_value = max(max_value, graph[i][j])
    # find candi
    min_candi_list = []
    max_candi_list = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == min_value:
                # 공격력, -(공격 시간), -(행+열), -(열)
                min_candi_list.append([graph[i][j], -graph_attack_time[i][j], -(i + j), -(j), i, j])
            if graph[i][j] == max_value:
                max_candi_list.append([graph[i][j], -graph_attack_time[i][j], -(i + j), -(j), i, j])

    attack_x, attack_y = 0, 0
    best_x, best_y = 0, 0
    # min candi가 있는 경우
    if min_candi_list != []:
        min_candi_list.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
        attack_x, attack_y = min_candi_list[0][-2], min_candi_list[0][-1]
        # max candi가 있는 경우
    if max_candi_list != []:
        max_candi_list.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
        best_x, best_y = max_candi_list[-1][-2], max_candi_list[-1][-1]

    if [attack_x, attack_y] != [best_x, best_y]:
        # 공격력 상승
        graph[attack_x][attack_y] += (n + m)
        # 공격 시간 = 지금
        graph_attack_time[attack_x][attack_y] = now_time
        return attack_x, attack_y, best_x, best_y
    else:
        return [-1, -1, -1, -1]


def find_layzer_load(start_x, start_y, end_x, end_y):
    q = deque()
    q.append([start_x, start_y, []])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[start_x][start_y] = 1

    while q:
        a, b, now_load = q.popleft()
        if [a, b] == [end_x, end_y]:
            return now_load
        for d in range(4):
            nx = (a + dx[d]) % n
            ny = (b + dy[d]) % m
            if graph[nx][ny] != 0:
                if visited[nx][ny] == -1:
                    new_load = now_load + [[nx, ny]]
                    q.append([nx, ny, new_load])
                    visited[nx][ny] = 1
    return []


def start_attack(attack_x, attack_y, best_x, best_y, now_time):
    graph_relation = [[0 for _ in range(m)] for _ in range(n)]
    graph_relation[attack_x][attack_y] = 1
    graph_relation[best_x][best_y] = 1

    # 레이저 공격 우선 시도
    layzer_attack_load = find_layzer_load(attack_x, attack_y, best_x, best_y)
    # 길이 있는 경우
    now_stat = graph[attack_x][attack_y]
    half_stat = now_stat // 2
    if layzer_attack_load != []:
        # 해당 경로 공격 진행
        for a, b in layzer_attack_load:
            graph_relation[a][b] = 1
            # 목적지 아닌 경우
            if [a, b] != [best_x, best_y]:
                graph[a][b] -= half_stat
            # 목적지인 경우
            else:
                graph[a][b] -= now_stat
            # 0으로 만들기
            graph[a][b] = max(0, graph[a][b])
    # 레이저 공격, 실패한 경우 폭탄 공격
    else:
        # 중심지
        graph[best_x][best_y] -= now_stat
        graph[best_x][best_y] = max(0, graph[best_x][best_y])

        # 주변
        for d in range(8):
            nx = (best_x + dx_cross[d]) % n
            ny = (best_y + dy_cross[d]) % m
            # 공격자가 아니어야함
            if [nx, ny] != [attack_x, attack_y]:
                if graph[nx][ny] != 0:
                    graph_relation[nx][ny] = 1
                    graph[nx][ny] -= half_stat
                    graph[nx][ny] = max(0, graph[nx][ny])

    return graph_relation


def rebuild_tower(graph_relation):
    for i in range(n):
        for j in range(m):
            if graph_relation[i][j] == 0 and graph[i][j] != 0:
                graph[i][j] += 1


def show_graph():
    for g in graph:
        print(g)


def cal_max():
    max_vaule = 0
    for i in range(n):
        for j in range(m):
            max_vaule = max(graph[i][j], max_vaule)
    return max_vaule


def simulation():
    for now_time in range(1, k + 1):
        # print("================", now_time)
        # show_graph()
        # print()
        # select attacker
        attack_x, attack_y, best_x, best_y = select_attacker_best(now_time)
        if [attack_x, attack_y, best_x, best_y] == [-1, -1, -1, -1]:
            return
        # print(attack_x, attack_y, best_x, best_y,now_time)
        # attack / # destroy_tower
        graph_relation = start_attack(attack_x, attack_y, best_x, best_y, now_time)
        # show_graph()
        # rebuild tower
        rebuild_tower(graph_relation)


n, m, k = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
graph_attack_time = [[0 for _ in range(m)] for _ in range(n)]

# 우/하/좌/상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dx_cross = [-1, -1, 0, 1, 1, 1, 0, -1]
dy_cross = [0, 1, 1, 1, 0, -1, -1, -1]

simulation()
result = cal_max()
print(result)

"""
5 10 704
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 2186
0 0 0 0 4346 0 0 0 0 0
0 0 0 0 3889 3148 1500 0 0 0
0 3440 0 0 17 0 0 0 0 0


36

5 10 200
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 2186
0 0 0 0 4346 0 0 0 0 0
0 0 0 0 3889 3148 1500 0 0 0
0 3440 0 0 17 0 0 0 0 0

4 4 5
0 1 4 4
8 0 10 13
8 0 11 26
0 0 0 0


"""