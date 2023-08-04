import sys
from collections import deque

def count_zero_stat():
    zero_count = 0
    for i in range(2*n):
        if q_stat[i] == 0:
            zero_count += 1
    return zero_count

def down_people():
    if q_people[down_point] == 1:
        q_people[down_point] = 0

def rotaion_rail():
    q_stat.rotate(1)
    q_people.rotate(1)
    down_people()

def move_people():
    # 내리는 위치 전 부터 확인
    for index in range(n-2, -1, -1):
        # 사람이 있음
        if q_people[index] == 1:
            # 다음 칸에 사람이 없음
            if q_people[index+1] == 0:
                #다음 칸 안전성이 0이 아님
                if q_stat[index+1] != 0:
                    q_people[index] = 0
                    q_people[index+1] = 1
                    q_stat[index+1] -= 1
    down_people()

def put_people():
    # 첫칸에 사람이 없음
    if q_people[put_point] == 0:
        # stat이 0 이 아님
        if q_stat[put_point] != 0:
            q_people[put_point] = 1
            q_stat[put_point] -= 1
    down_people()

n, k = map(int,sys.stdin.readline().rstrip().split())
list_stat = list(map(int,sys.stdin.readline().rstrip().split()))

q_stat = deque(list_stat)
q_people = deque([0 for _ in range(2*n)])

put_point = 0
down_point = n-1

result = 0
while 1:
    result += 1
    # 레일이 한바퀴 회전
    rotaion_rail()
    # 오른쪽 끝부터 / 이동 가능하면, 움직이기
    move_people()
    # 사람을 올림
    put_people()
    # 종료 조건 확인
    zero_stat = count_zero_stat()
    if zero_stat >= k:
        break
print(result)