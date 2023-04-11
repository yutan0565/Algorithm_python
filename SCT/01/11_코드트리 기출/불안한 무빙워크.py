import sys
from collections import deque

def rotate_rail():
    rail_stat.rotate(1)
    rail_pos.rotate(1)
    if rail_pos[down_pos] == 1:
        rail_pos[down_pos] = 0

def move_peopel():
    for index in range(n-1, 0, -1):
        check_index = index - 1
        # 이전에 사람이 있는 경우
        if rail_pos[check_index] == 1:
            # 지금 칸이 빈칸
            if rail_pos[index] == 0:
                # 지금 칸 안전성이 0 이 아님
                if rail_stat[index] != 0:
                    rail_pos[index] = 1
                    rail_pos[check_index] = 0
                    rail_stat[index] -= 1
    if rail_pos[down_pos] == 1:
        rail_pos[down_pos] = 0

def put_people():
    if rail_pos[0] == 0:
        if rail_stat[0] != 0:
            rail_pos[0] = 1
            rail_stat[0] -= 1

n, k = map(int,sys.stdin.readline().rstrip().split())
rail_stat = deque(list(map(int, sys.stdin.readline().rstrip().split())))
rail_pos = deque([0 for _ in range(2*n)])

on_pos = 0
down_pos = n-1
result = 1

def show_now():
    print("rail stat : ", rail_stat)
    print("rail pos  : ", rail_pos)

while 1:
    # 무빙워크 한칸 회전
    rotate_rail()
    # 가장 먼저 무빙 워크에 올라간 사람부터, 이동 가능하면 이동
    move_peopel()
    # 1번 칸에 사람 없고, 안전성이 0 이 아니면, 한명 더 올림
    put_people()
    # 종료 조건
    if rail_stat.count(0) >= k:
        break
    result += 1
print(result)