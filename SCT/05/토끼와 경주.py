import sys
from collections import defaultdict
import heapq


def make_mirror_list():
    global x_mirror_list, y_mirror_list
    x_mirror_list = [i for i in range(n - 1)] + [n - 1] + [i for i in range(n - 2, 0, -1)]
    y_mirror_list = [i for i in range(m - 1)] + [m - 1] + [i for i in range(m - 2, 0, -1)]
    for _ in range(3):
        x_mirror_list += x_mirror_list
        y_mirror_list += y_mirror_list


def ready_race(n, m, p, distance_info):
    for idx in range(p):
        pid = distance_info[2 * idx]
        dis = distance_info[2 * idx + 1]
        dict_dis[pid] = dis
        dict_pos[pid] = [0, 0]
        dict_score[pid] = 0
        # 총 점프 횟수가 적은, (행+열) 작은, 행 작은, 열 작은, 고유번호 작은
        heapq.heappush(hq, [0, 0, 0, 0, pid])


def show_info():
    for i in range(len(hq)):
        jump, _, row, col, id = hq[i]
        print("id : {}, jump : {}, sum : {}  row : {} col : {} score : {}, dis : {}".format(id, jump, row+col,row, col, dict_score[id], dict_dis[id]))


def start_race(k, s):
    use_id = []
    # 우선 순위가 높은 토끼 보내기를 k 번 반복
    for _ in range(k):
        # print("-------")
        # show_info()
        # 우선순위 높은 토끼 선택
        now_jump, now_r_c, now_r, now_c, now_id = heapq.heappop(hq)
        use_id.append(now_id)
        temp_hq = []
        move_dis_x = dict_dis[now_id] % (2 * (n - 1))
        move_dis_y = dict_dis[now_id] % (2 * (m - 1))
        x_offset = (n - 1) * 4
        y_offset = (m - 1) * 4

        # 4개 방향중 고르기
        for d in range(4):
            nx_idx = now_r + x_offset + dx[d] * move_dis_x
            ny_idx = now_c + y_offset + dy[d] * move_dis_y
            nx = x_mirror_list[nx_idx]
            ny = y_mirror_list[ny_idx]
            heapq.heappush(temp_hq, [-(nx + ny), -nx, -ny, -now_id])
        # 옮길 위치 정하기
        _, nx, ny, _ = heapq.heappop(temp_hq)
        nx = -nx
        ny = -ny
        dict_pos[now_id] = [nx, ny]
        # now_id 빼고  점수 증가 (nx+ny+2)
        for id in dict_score.keys():
            if id != now_id:
                dict_score[id] += (nx + ny + 2)
        # hq에 다시 토끼 넣어주기
        # 총 점프 횟수가 적은, (행+열) 작은, 행 작은, 열 작은, 고유번호 작은
        heapq.heappush(hq, [now_jump + 1, nx + ny, nx, ny, now_id])
        # print(now_id)
    # show_info()

    score_hq = []
    for now_id in use_id:
        now_r = dict_pos[now_id][0]
        now_c = dict_pos[now_id][1]
        # (행+열) 큰, 행 큰, 열 큰, 고유 큰
        heapq.heappush(score_hq, [-(now_r+now_c), -now_r, -now_c, -now_id])

    # 우선 순위 높은 토끼 점수 + s
    _, _, _, id = heapq.heappop(score_hq)
    id = -id
    dict_score[id] += s
    # print("추가 점수 :", id)


def change_dis(pid_t, l):
    dict_dis[pid_t] *= l
    # show_info()


def cal_max_score():
    result = 0
    for id in dict_score.keys():
        result = max(result, dict_score[id])
    return result


# 이동해야 하는 거리
dict_dis = {}
dict_pos = {}
dict_score = {}
hq = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x_mirror_list = []
y_mirror_list = []

n, m = 0, 0
Q = int(sys.stdin.readline().rstrip())
for turn in range(1, Q + 1):
    # print("=========",turn,"==========")
    input_info = list(map(int, sys.stdin.readline().rstrip().split()))
    order = input_info[0]
    # 경주 시작 준지
    if order == 100:
        # n x m 의 격자 위에서 p 마리의 토끼가 경주 시작
        n, m, p = input_info[1], input_info[2], input_info[3]
        distance_info = input_info[4:]
        ready_race(n, m, p, distance_info)
        make_mirror_list()
    # 경주 진행
    elif order == 200:
        k, s = input_info[1], input_info[2]
        start_race(k, s)
    # 이동거리 변경
    elif order == 300:
        pid_t, l = input_info[1], input_info[2]
        change_dis(pid_t, l)
    # 최고의 토끼 선정
    elif order == 400:
        result = cal_max_score()
        print(result)

"""
5
100 3 5 2 10 2 20 5
200 6 100
300 10 2
200 3 20
400

5
100 3 5 2 10 1232 20 4321
200 5 100
300 10 2
200 2 20
400

"""