import sys
from collections import defaultdict
import heapq

def start_race(k,s):
    global score_sum
    max_sum_x_y = -1
    max_x = -1
    max_y = -1
    max_id = -1

    for _ in range(k):
        now_jump_count,now_sum_x_y,now_x,now_y,now_id = heapq.heappop(q_min)
        now_distance = dict_distance[now_id]
        new_x, new_y,new_sum_x_y = -1,-1,-1
        for d in range(4):
            x,y = now_x,now_y
            # 오, 아, 왼, 위
            if d == 0:
                new_distance = now_distance % (2 * (m-1))
                index = y + 2*(m-1) + new_distance
                y = m_index[index]
            elif d == 2:
                new_distance = now_distance % (2 * (m-1))
                index = y + 2 * (m - 1) - new_distance
                y = m_index[index]
            elif d == 1:
                new_distance = now_distance % (2 *  (n-1))
                index = x + 2 * (n - 1) + new_distance
                x = n_index[index]
            elif d == 3:
                new_distance = now_distance % (2 * (n-1))
                index = x + 2 * (n - 1) - new_distance
                x = n_index[index]
            change_flag = 0
            if x+y > new_sum_x_y:
                change_flag = 1
            elif x+y == new_sum_x_y:
                if x > new_x:
                    change_flag = 1
                elif x == new_x:
                    if y > new_y:
                        change_flag = 1
            if change_flag == 1:
                new_sum_x_y = x + y
                new_x = x
                new_y = y
        score_sum += (new_x+new_y+2)
        dict_score[now_id] -= (new_x+new_y+2)
        heapq.heappush(q_min,[now_jump_count+1,new_sum_x_y,new_x,new_y,now_id])
        change_flag = 0
        if new_sum_x_y > max_sum_x_y:
            change_flag = 1
        elif new_sum_x_y == max_sum_x_y:
            if new_x > max_x:
                change_flag = 1
            elif new_x == max_x:
                if new_y > max_y:
                    change_flag = 1
                elif new_y == max_y:
                    if now_id > max_id:
                        change_flag = 1
        if change_flag == 1:
            max_sum_x_y = new_sum_x_y
            max_x = new_x
            max_y = new_y
            max_id = now_id
    dict_score[max_id] += s

def change_distance(pid_t,l):
    dict_distance[pid_t] = dict_distance[pid_t]*l

def find_best():
    max_score = max(dict_score.values()) + score_sum
    return max_score

dict_distance = {}
dict_score = {}
score_sum = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
q_min = []
n_index, m_index = [], []

Q = int(sys.stdin.readline().rstrip())
for turn in range(1, Q+1):
    order_list = list(map(int,sys.stdin.readline().rstrip().split()))
    order = order_list[0]
    if order == 100:
        n,m,p = order_list[1], order_list[2], order_list[3]
        n_index = [i for i in range(n)] + [i for i in range(n - 2, -1, -1)] + [i for i in range(1, n)] + [i for i in range(n - 2, -1, -1)] + [i for i in range(1, n)]
        m_index = [i for i in range(m)] + [i for i in range(m - 2, -1, -1)] + [i for i in range(1, m)] + [i for i in range(m - 2, -1, -1)] + [i for i in range(1, m)]
        for index in range(p):
            id = order_list[4+index*2]
            distance = order_list[4+index*2+1]
            dict_distance[id] = distance
            dict_score[id] = 0
            jump_count = 0
            sum_x_y = 0
            x = 0
            y = 0
            heapq.heappush(q_min, [jump_count,sum_x_y,x,y,id])
    elif order == 200:
        k,s = order_list[1], order_list[2]
        start_race(k,s)
    elif order == 300:
        pid_t,l = order_list[1], order_list[2]
        change_distance(pid_t,l)
    elif order == 400:
        result = find_best()
        print(result)
    # if order != 400:
    #     print("================")
    #     print("점수 : ", dict(dict_score))
    #     print("거리 : ", dict(dict_distance))
