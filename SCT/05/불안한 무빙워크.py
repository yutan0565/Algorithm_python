import sys
from collections import deque

def check_line():
    # 사람이 있는 경우
    if people_q[n-1] == 1:
        people_q[n-1] = 0


def rotate_line():
    # 사람 회전
    people_q.rotate(1)
    # 스탯 회전
    stat_q.rotate(1)
    # n-1 번칸 체크
    check_line()

def move_people():
    # n-2 번 부터 확인 진행 하기 ( n-1 칸은 항상 비어 있음)
    for i in range(n-1,-1,-1):
        # 현재칸에 사람이 있는 경우
        if people_q[i] == 1:
            # 다음 칸에 사람이 없음
            if people_q[i+1] == 0:
                # 다음 칸의 스탯이 남아 있는 경우
                if stat_q[i+1] != 0:
                    people_q[i] = 0
                    people_q[i+1] = 1
                    stat_q[i+1] -= 1
    # n-1 번칸 체크
    check_line()

def add_people():
    # 첫번째 칸에 사람이 없다면
    if people_q[0] == 0:
        # 첫번째칸의 stat이 0이 아니면
        if stat_q[0] != 0:
            people_q[0] = 1
            stat_q[0] -= 1

def zero_count():
    cnt = 0
    for i in range(len(stat_q)):
        if stat_q[i] == 0:
            cnt += 1
    return cnt

def show_info():
    # print("======people======")
    # print(people_q)
    # print("======stat_Q======")
    # print(stat_q)
    # print()
    return


def simulation():
    result = 0
    while 1:
        # print("==================================")
        result += 1
        # 무빙워크 한칸 회전
        rotate_line()
        show_info()
        # 사람 이동
        move_people()
        show_info()
        # 1번 칸에 사람이 없고 안정성이 0이 아니라면 사람을 한 명 더 올립니다.
        add_people()
        show_info()
        if zero_count() >= k:
            break

    return result


n,k = map(int,sys.stdin.readline().rstrip().split())
temp = list(map(int,sys.stdin.readline().rstrip().split()))
people_q = deque([0 for _ in range(2*n)])
stat_q = deque(temp)

result = simulation()
print(result)