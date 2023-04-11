import sys
from collections import deque

def rotation_line():
    stance_line.rotate(1)  #양, 오른쪽
    robot.rotate(1)
    robot[-1] = 0

def move_robot():
    for i in range(n - 2, -1, -1):
        if robot[i] == 1 and robot[i + 1] == 0:
            if stance_line[i + 1] != 0:
                robot[i + 1] = 1
                robot[i] = 0
                stance_line[i + 1] -= 1
    robot[-1] = 0

def on_robot():
    if robot[0] == 0 and stance_line[0] >= 1:
        robot[0] = 1
        stance_line[0] -= 1

def check_line():
    if stance_line.count(0) >= k:  #하나의 리스트에서, 해당 숫자 개수 측정
        return 1
    else:
        return -1

n, k = map(int, sys.stdin.readline().split())
stance_line = deque(list(map(int, input().split())))
robot = deque([0] * n)
result = 0

while 1:
    rotation_line()
    move_robot()
    on_robot()

    result += 1
    if check_line() == 1:
        break

print(result)