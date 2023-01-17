import sys


dx = [-1,0,0,1]
dy = [0,-1,1,0]

def find_like(x,y,number):
    like_list = dict_like[number]
    like_count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] in like_list:
                like_count += 1
    return like_count

def find_empty(x,y):
    empty_count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny]  == 0:
                empty_count += 1
    return empty_count

def cal_score():
    score = 0
    for i in range(n):
        for j in range(n):
            count = find_like(i,j,graph[i][j])
            if count == 0:
                continue
            elif count == 1:
                score += 1
            elif count == 2:
                score += 10
            elif count == 3:
                score += 100
            elif count == 4:
                score += 1000
    return score

def find_position():
    for number in order_list:

        max_like_count = -1
        max_empty_count = -1
        max_x = -1
        max_y = -1
        # 친구 있는 곳 먼저 찾기
        for i in range(n):
            for j in range(n):
                if graph[i][j] != 0:
                    continue
                temp_like = find_like(i, j, number)
                temp_empty = find_empty(i, j)
                if temp_like > max_like_count:
                    max_like_count = temp_like
                    max_empty_count = temp_empty
                    max_x = i
                    max_y = j
                elif temp_like == max_like_count:
                    if temp_empty > max_empty_count:
                        max_empty_count = temp_empty
                        max_x = i
                        max_y = j

        graph[max_x][max_y] = number


n = int(sys.stdin.readline().rstrip())
graph = [[0 for _ in range(n)] for _ in range(n)]

dict_like = {}
order_list = []
for _ in range(1, n**2 + 1):
    a,b,c,d,e = map(int, sys.stdin.readline().rstrip().split())
    dict_like[a] = [b,c,d,e]
    order_list.append(a)

find_position()
result = cal_score()


print(result)

# 가자의 좌석 배치

"""
1. 좋아하는 학생이 가장 많은 곳 앉기
     없으면은, 비어있는 칸
     행, 열 번호가 가장 작은 칸
"""