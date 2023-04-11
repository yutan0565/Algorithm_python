import sys
from collections import defaultdict
import heapq

def start_race(k,s):
    global head
    move_id_list = []
    for _ in range(k):
        now_jump_count,now_sum_x_y,now_x,now_y,now_id = heapq.heappop(q_min)
        q_max.remove([-now_sum_x_y,-now_x,-now_y,-now_id])
        move_id_list.append(now_id)
        candi_pos = []
        now_distance = dict_distance[now_id]
        for d in range(4):
            now_d = d
            x,y = now_x,now_y
            for _ in range(now_distance):
                nx = x + dx[now_d]
                ny = y + dy[now_d]
                if not(0<=nx<n and 0<=ny<m):
                    now_d = (now_d + 2)%4
                    nx = x + dx[now_d]
                    ny = y + dy[now_d]
                x,y= nx,ny
            candi_pos.append([x+y,x,y])
        candi_pos.sort(key = lambda x:(x[0],x[1],x[2]))
        new_x = candi_pos[-1][1]
        new_y = candi_pos[-1][2]
        for id in dict_score.keys():
            if id != now_id:
                dict_score[id] += (new_x+new_y+2)
        new_sum_x_y = new_x+new_y
        heapq.heappush(q_min,[now_jump_count+1,new_sum_x_y,new_x,new_y,now_id])
        heapq.heappush(q_max, [-new_sum_x_y, -new_x, -new_y, -now_id])

    for i in range(len(q_max)-1,-1,-1):
        now_id = -q_max[0][-1]
        if now_id in move_id_list:
            dict_score[now_id] += s
            break

def change_distance(pid_t,l):
    dict_distance[pid_t] = dict_distance[pid_t]*l

def find_best():
    max_score = max(dict_score.values())
    return max_score


dict_distance = {}
dict_score = {}

dx = [0,1,0,-1]
dy = [1,0,-1,0]
q_min = []
q_max = []

Q = int(sys.stdin.readline().rstrip())
for tun in range(1, Q+1):
    order_list = list(map(int,sys.stdin.readline().rstrip().split()))
    order = order_list[0]
    if order == 100:
        n,m,p = order_list[1], order_list[2], order_list[3]
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
            heapq.heappush(q_max, [-sum_x_y, -x, -y, -id])
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
