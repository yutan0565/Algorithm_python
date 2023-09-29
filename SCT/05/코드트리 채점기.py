import sys
from collections import defaultdict
import heapq

def make_judger(N,domain,id):
    # 채점기 생성
    for j_num in range(1, N+1):
        dict_judger[j_num] = []
    # 문제 생성
    # 시간, 우선순위, domain, id
    heapq.heappush(dict_waiting_hq[domain],[1,0,domain,id])

def add_new(t,p,now_domain, now_id):
    # t초, 우선순위 p,
    # waiting q에 추가
    # 이미 있는 id 인지 확인 / 이미 있으면 패스
    for _,_,_,id in dict_waiting_hq[now_domain]:
        if id == now_id:
            return
    heapq.heappush(dict_waiting_hq[domain], [p, t, now_domain, now_id])

def try_judge(now_time):
    # 우선 순위가 제일 높은 task 꺼내기

    # 사용가능한 채점기 찾기
    judger_num = -1
    for j_num in dict_judger.keys():
        if dict_judger[j_num] == []:
            judger_num = j_num
            break
    # 채점기 없으면 패스
    if judger_num == -1: return

    # 채점기가 있는 경우
    temp_hq = []
    # 각 도메인 별로 가장 빠른 / 채점 가능한 것 가져오기
    for now_domain in dict_waiting_hq.keys():
        # 채점하고 있지 않은 domain 주소여야함
        if dict_domain_judging[now_domain] == 0:
            # task가 있는 경우
            if len(dict_waiting_hq[now_domain]) != 0:
                prioriy, start_time, domain, id = dict_waiting_hq[now_domain][0]
                if now_time >= dict_judge_start[domain] + 3*dict_judge_gap[domain]:
                    heapq.heappush(temp_hq, [prioriy,start_time,domain,id])
    # 채점 시도할거 최종선정
    if len(temp_hq) != 0:
        pri, time, domain, id = temp_hq[0]
        # 해당 domain에서 1개 제거
        heapq.heappop(dict_waiting_hq[domain])
        # 채점기 사용 시작
        dict_judger[judger_num] = [ pri, time, domain, id]

        # 채점 중인 domain으로 변경
        dict_domain_judging[domain] = 1
        dict_judge_start[domain] = now_time



def end_judge(end_time,J_id):
    if dict_judger[J_id] != []:
        pri, time, domain, id =dict_judger[J_id]
        dict_judger[J_id] = []
        dict_domain_judging[domain] = 0
        dict_judge_gap[domain] = end_time - dict_judge_start[domain]

def check_waiting(t):
    result = 0
    for domain in dict_waiting_hq.keys():
        result += len(dict_waiting_hq[domain])
    return result

def show_info():
    print("dict_waiting_hq :", dict(dict_waiting_hq))
    print("dict_judger :", dict(dict_judger))
    print("dict_domain_judging :", dict(dict_domain_judging))
    print("dict_judge_start :", dict(dict_judge_start))
    print("dict_judge_gap :", dict(dict_judge_gap))

dict_waiting_hq = defaultdict(lambda  : [])
dict_judger = defaultdict(lambda  : []) # 지금 채점하고 있는거 정보

dict_domain_judging = defaultdict(lambda : 0) # 채점
dict_judge_start = defaultdict(lambda : 0) # 가장 최근 시작 시간
dict_judge_gap = defaultdict(lambda : 0) # 가장 최근 끝나는 시간

Q = int(sys.stdin.readline().rstrip())

for turn in range(1, Q+1):
    input_info = list(sys.stdin.readline().rstrip().split())
    order = int(input_info[0])
    #print(input_info)
    # 코드트리 채점기 준비
    if order == 100:
        N, u0 = int(input_info[1]), input_info[2]
        domain,id = u0.split("/")
        make_judger(N,domain,id)

    # 채점 요청
    elif order == 200:
        t,p,u = int(input_info[1]), int(input_info[2]), input_info[3]
        domain, id = u.split("/")
        add_new(t,p,domain, id)

    # 채점 시도
    elif order == 300:
        t = int(input_info[1])
        try_judge(t)

    # 채점 종료
    elif order == 400:
        t, J_id = int(input_info[1]), int(input_info[2])
        end_judge(t,J_id)

    # 채점 대기 큐 조회
    elif order == 500:
        t = int(input_info[1])
        result = check_waiting(t)
        print(result)
    # print("======",turn,"=========")
    # show_info()
    # print()