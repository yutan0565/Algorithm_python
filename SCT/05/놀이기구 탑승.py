import sys
from collections import defaultdict


def simulation():
    for num in input_line:
        now_friend_list = friend_dict[num]
        # 친구수 많, 빈칸 많, 행 작, 열 작
        info_list = []
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 0:
                    friend_cnt = 0
                    empty_cnt = 0
                    for d in range(4):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if 0<=nx<n and 0<=ny<n:
                            if graph[nx][ny] == 0:
                                empty_cnt += 1
                            elif graph[nx][ny] in now_friend_list:
                                friend_cnt += 1
                    info_list.append([-friend_cnt,-empty_cnt,i,j])
        info_list.sort(key = lambda x : (x[0],x[1],x[2],x[3]))
        x,y = info_list[0][2], info_list[0][3]
        graph[x][y] = num


def cal_score():
    result = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0<=nx<n and 0<=ny<n:
                    if graph[nx][ny] in friend_dict[graph[i][j]]:
                        cnt += 1
            result += score_list[cnt]
    return result

n = int(sys.stdin.readline().rstrip())
dx = [-1,0,0,1]
dy = [0,-1,1,0]
friend_dict = defaultdict(lambda : [0,0,0,0])
graph = [[0 for _ in range(n)] for _ in range(n)]
score_list = [0,1,10,100,1000]
input_line = []

for i in range(1, n*n+1):
    num, a,b,c,d = map(int,sys.stdin.readline().rstrip().split())
    friend_dict[num] = [a,b,c,d]
    input_line.append(num)

simulation()
result = cal_score()
print(result)