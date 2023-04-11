import sys

def put_people(num):
    max_x,max_y = 0,0
    max_friend = -1
    max_empty = -1
    friend_list = dict_friend[num]
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
                        elif graph[nx][ny] in friend_list:
                            friend += 1
                if friend > max_friend:
                    max_friend = friend
                    max_empty = empty
                    max_x = i
                    max_y = j
                elif friend == max_friend:
                    if empty > max_empty:
                        max_friend = friend
                        max_empty = empty
                        max_x = i
                        max_y = j
    graph[max_x][max_y] = num

def cal_score():
    score = 0
    score_list = [0,1,10,100,100]
    for i in range(n):
        for j in range(n):
            num = graph[i][j]
            friend = 0
            friend_list = dict_friend[num]
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] in friend_list:
                        friend += 1
            score += score_list[friend]
    return score

n = int(sys.stdin.readline().rstrip())
graph = [[0 for _ in range(n)] for _ in range(n)]
dict_friend = {}

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(n*n):
    num,b,c,d,e = map(int,sys.stdin.readline().rstrip().split())
    dict_friend[num] = [b,c,d,e]
    put_people(num)

result = cal_score()
print(result)