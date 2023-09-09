import sys, copy
import heapq
from collections import defaultdict


def make_machine(n, u0):
    for num in range(1, n + 1):
        dict_machine_domain[num] = None
        heapq.heappush(avail_machine_q, num)

    domain, id = u0.split("/")
    time = 0
    pri = 1
    if not (dict_waiting_q.get(domain)):
        dict_waiting_q[domain] = []
    heapq.heappush(dict_waiting_q[domain], [pri, time, u0])
    use_url.add(u0)


def start_check(t, p, u):
    domain, id = u.split("/")
    if u not in use_url:
        use_url.add(u)
        if not (dict_waiting_q.get(domain)):
            dict_waiting_q[domain] = []
        heapq.heappush(dict_waiting_q[domain], [p, t, u])


def try_check(t):
    # 사용 가능한 기계가 없는 경우 / 대기큐에 아무것도 없는 경우 (use_url에 없는경우)
    if len(avail_machine_q) == 0 or len(use_url) == 0:
        return

    min_wait = [float("inf"), float("inf"), None, None]

    for now_domain in dict_waiting_q.keys():
        if dict_waiting_q[now_domain] == []:
            continue
        # 지금 대기 domain별 대기줄에 있는 것중 전번째
        now_p, now_t, now_u = dict_waiting_q[now_domain][0]
        if now_domain in use_domain:
            continue
        if not (dict_domain_time.get(now_domain)):
            dict_domain_time[now_domain] = [0, 0]
        start, gap = dict_domain_time[now_domain]
        if t < start + 3 * gap:
            continue
        min_wait = min(min_wait, [now_p, now_t, now_domain, now_u])

    # min_wait으로 선정된게 아무것도 없는 경우
    if min_wait[2] == None:
        return
    try_p, try_t, try_domain, try_u = min_wait
    machine_num = heapq.heappop(avail_machine_q)
    dict_machine_domain[machine_num] = try_domain
    use_domain.add(try_domain)
    use_url.remove(try_u)
    # root가 최소값인것은 맞음 / 하지만 heappop을 사용해야지 재 정렬이 됨
    heapq.heappop(dict_waiting_q[try_domain])
   # del dict_waiting_q[try_domain][0] # 정렬이 안됨
    dict_domain_time[try_domain][0] = t

def end_check(t, j_id):
    if dict_machine_domain[j_id] == None:
        return
    heapq.heappush(avail_machine_q, j_id)
    now_domain = dict_machine_domain[j_id]
    dict_machine_domain[j_id] = None
    dict_domain_time[now_domain][1] = t - dict_domain_time[now_domain][0]
    use_domain.remove(now_domain)


def waiting_q_info():
    return len(use_url)

Q = int(sys.stdin.readline().rstrip())

avail_machine_q = []

dict_machine_domain = {}
dict_domain_time = {}

use_domain = set()
use_url = set()

dict_waiting_q = {}
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
        result = waiting_q_info()
        result_list.append(result)

    # print("====================")
    # print("order : ", order)
    # print("기계 도메인 : ",dict_machine_domain)
    # print("기계 시간 : ",dict_domain_time)
    # print("대기 : ",dict_waiting_q)
    # print("사용 domain : ", use_domain)
    # print("사용 url : ", use_url)
    # print()

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