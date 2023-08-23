from collections import deque
import sys

def find_zero_stat():
    count = 0
    for s in stat:
        if s == 0:
            count += 1
    return count

def check_down():
    if people[n-1] == 1:
        people[n-1] = 0

def move_line():
    stat.rotate(1)
    people.rotate(1)
    check_down()

def move_people():
    for index in range(n-2,-1,-1):
        next_index = index+1
        if people[index] == 1:
            if people[next_index] == 0:
                if stat[next_index] != 0:
                    people[next_index] = 1
                    stat[next_index] -= 1
                    people[index] = 0
    check_down()

def put_people():
    if people[0] == 0:
        if stat[0] != 0:
            people[0] = 1
            stat[0] -= 1
    check_down()

n,k = map(int,sys.stdin.readline().rstrip().split())
stat = deque(list(map(int,sys.stdin.readline().rstrip().split())))
people = deque([0 for _ in range(n*2)])

result = 0
while 1:
    result += 1
    # 무빙워크 한칸 회전
    move_line()
    # 앞 사람부터 이동
    move_people()
    # 한명더 올리기
    put_people()

    zero_count = find_zero_stat()
    if zero_count >= k:
        break
print(result)