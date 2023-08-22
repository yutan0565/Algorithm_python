import sys
from collections import defaultdict

def put_people(num):
    max_x, max_y = n+1,n+1
    max_friend = -1
    max_empty = -1
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
                        elif graph[nx][ny] in dict_friend[num]:
                            friend += 1
                if friend > max_friend:
                    max_x,max_y = i,j
                    max_friend = friend
                    max_empty = empty
                elif friend == max_friend:
                    if empty > max_empty:
                        max_x, max_y = i, j
                        max_friend = friend
                        max_empty = empty
                    elif empty == max_empty:
                        if i < max_x:
                            max_x, max_y = i, j
                            max_friend = friend
                            max_empty = empty
                        elif i == max_x:
                            if j < max_y:
                                max_x, max_y = i, j
                                max_friend = friend
                                max_empty = empty
    graph[max_x][max_y] = num

def cal_score():
    score = 0
    score_list = [0,1,10,100,1000]
    for i in range(n):
        for j in range(n):
            friend = 0
            num = graph[i][j]
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] in dict_friend[num]:
                        friend += 1
            score += score_list[friend]
    return score

n = int(sys.stdin.readline().rstrip())
graph = [[0 for _ in range(n)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

dict_friend = defaultdict(lambda : [])
for _ in range(n*n):
    a,b,c,d,e = map(int,sys.stdin.readline().rstrip().split())
    dict_friend[a] = [b,c,d,e]
    put_people(a)

result = cal_score()
print(result)


