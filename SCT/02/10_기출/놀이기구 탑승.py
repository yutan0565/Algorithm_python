import sys
from collections import defaultdict

def seat_student(number):
    x,y = -1,-1
    max_friend_count = -1
    max_empty_count = -1
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                friend = 0
                empty = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] == 0:
                            empty += 1
                        elif graph[nx][ny] in dict_like[number]:
                            friend += 1

                # 지금 친구가 더 많으면
                if friend > max_friend_count:
                    x,y = i,j
                    max_friend_count = friend
                    max_empty_count = empty
                # 친구 수가 같으면
                elif friend == max_friend_count:
                    # 지금 empty가 가장 많으 곳
                    if empty > max_empty_count:
                        x, y = i, j
                        max_friend_count = friend
                        max_empty_count = empty
                    # 친구 수가 같으면  // 시작을, 행 / 열 작은거에서 시작 헀으니, 업데이트 안해도됨
                    elif empty == max_empty_count:
                        pass
    graph[x][y] = number

def cal_score():
    total_score = 0
    for i in range(n):
        for j in range(n):
            number = graph[i][j]
            count = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] in dict_like[number]:
                        count += 1
            total_score += score_list[count]
    return total_score

n = int(sys.stdin.readline().rstrip())
graph = [[0 for _ in range(n)] for _ in range(n)]
dict_like = defaultdict(lambda  : -1)

dx = [0,0,-1,1]
dy = [1,-1,0,0]
score_list = [0,1,10,100,1000]

for _ in range(1, n*n+1):
    info = list(map(int, sys.stdin.readline().rstrip().split()))
    num = info[0]
    dict_like[num] = info[1:]
    # 학생 앉히기 시작
    seat_student(num)

result = cal_score()
print(result)
