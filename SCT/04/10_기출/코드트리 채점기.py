import sys, copy
import heapq
from collections import defaultdict

def make_machine(n, u0):
    for num in range(1,n+1):
        dict_machine_domain[num] = ""
        dict_machine_url[num] = ""
        heapq.heappush(avail_machine_q, num)

    domain, id = u0.split("/")
    time = 0
    pri = 1
    dict_waiting_q[domain] = []
    dict_waiting_q[domain].append([pri, time, u0])

def start_check(t, p, u):
    domain, id = u.split("/")
    if u not in use_url:
        use_url.append(u)
        if not(dict_waiting_q.get(domain)):
            dict_waiting_q[domain] = []
        dict_waiting_q[domain].append([p, t, u])


def try_check(t):
    if len(avail_machine_q) == 0:
        return

    for now_domain in dict_waiting_q.keys():
        if dict_waiting_q[now_domain] == []:
            continue
        now_p, now_t, now_u = dict_waiting_q[now_domain][0]
        if now_domain in use_domain:
            print(t)
            print("이미 진행중인 domain : ", now_domain)
            print(use_domain)
            continue
        if history_q != []:
            continue_flag = 0
            new_history_q = copy.deepcopy(history_q)
            for i in range(len(history_q)):
                pri,his_start, his_end, his_u, his_domain =min(new_history_q)
                print("?")
                if now_domain == his_domain:
                    gap = his_end - his_start
                    print("gap : ", gap)
                    if t < his_start + 3 * gap:
                        continue_flag = 1
                        print("조건에 맞지 않는 domain: ", now_domain)
                        break
                new_history_q.remove([pri,his_start, his_end, his_u, his_domain])
            if continue_flag == 1:
                continue
        machine_num = heapq.heappop(avail_machine_q)
        dict_machine_domain[machine_num] = now_domain
        dict_machine_url[machine_num] = now_domain
        use_domain.append(now_domain)
        dict_waiting_q[now_domain].remove([ now_p, now_t, now_u])
        judging_q.append([t, now_u, now_domain])
        print("시작")

def end_check(t, j_id):
    if dict_machine_url[j_id] == "":
        return
    heapq.heappush(avail_machine_q, j_id)
    now_u = dict_machine_url[j_id]
    dict_machine_domain[j_id] = ""
    dict_machine_url[j_id] = ""
    for i in range(len(judging_q)):
        jud_t, jud_u, jud_domain = judging_q[i]
        if now_u == jud_u:
            judging_q.remove([jud_t, jud_u, jud_domain])
            use_domain.remove(jud_domain)
            use_url.remove(jud_u)
            history_q.append([-t, jud_t, t, jud_u, jud_domain])
            break


def waiting_q_info(t):
    count = 0
    for domain in dict_waiting_q.keys():
        count += len(dict_waiting_q[domain])
    return count

Q = int(sys.stdin.readline().rstrip())


avail_machine_q = []

dict_machine_domain = {}
dict_machine_url = {}
use_domain = []
use_url = []

dict_waiting_q = {}
judging_q = []
history_q = []

result_list = []

for round in range(1, Q + 1):
    order_info = list(sys.stdin.readline().rstrip().split())
    order = int(order_info[0])
    if order == 100:
        n = int(order_info[1])
        u0 = order_info[2]
        make_machine(n, u0)

    elif order == 200:
        t = int(order_info[1])
        p = int(order_info[2])
        u = order_info[3]
        start_check(t, p, u)

    elif order == 300:
        t = int(order_info[1])
        try_check(t)

    elif order == 400:
        t = int(order_info[1])
        j_id = int(order_info[2])
        end_check(t, j_id)

    elif order == 500:
        t = int(order_info[1])
        result = waiting_q_info(t)
        result_list.append(result)

for r in result_list:
    print(r)



"""
19
100 3 codetree.ai/16
300 1
400 4 1
200 5 1 codetree.ai/17
200 6 1 codetree.ai/17
500 7
300 8
500 9
300 11
400 12 1
500 13
200 14 3 codetree.ai/18
200 15 2 codetree.ai/20
200 16 2 tree.ai/1
500 17
300 18
500 19
200 20 1 codetree.ai/20
500 21
"""