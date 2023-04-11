import copy
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def spread_smell():
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) != 0:
                visited[i][j] = [k, graph[i][j][0]]

def dell_smell():
    for i in range(n):
        for j in range(n):
            if visited[i][j][0] != 0:
                visited[i][j][0] -= 1
                if visited[i][j][0] == 0:
                    visited[i][j] = [0,0]
def move_shark():
    temp_graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) == 0:
                continue
            shark_num = graph[i][j][0]
            shark_direct = dict_direct[shark_num]
            shark_move_direct = dict_pri[shark_num][shark_direct]
            flag = 0
            for type in range(2):
                for go_direct in shark_move_direct:
                    nx = i + dx[go_direct]
                    ny = j + dy[go_direct]
                    if 0<=nx<n and 0<=ny<n:
                        if type == 0:
                            if visited[nx][ny][0] == 0:
                                temp_graph[nx][ny].append(shark_num)
                                dict_direct[shark_num] = go_direct
                                flag = 1
                                break
                        elif type == 1:
                            if visited[nx][ny][1] == shark_num:
                                temp_graph[nx][ny].append(shark_num)
                                dict_direct[shark_num] = go_direct
                                flag = 1
                                break
                if flag == 1:
                    break

    return temp_graph


def dell_shark():
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) >=2:
                temp = graph[i][j]
                temp.sort()
                for k in range(1, len(temp)):
                    enable_shark.remove(temp[k])
                graph[i][j] = [temp[0]]

n,m,k = map(int, sys.stdin.readline().rstrip().split())
graph = [[[]for i in range(n)]for i in range(n)]
for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if temp[j] != 0:
            graph[i][j].append(temp[j])

dict_direct = {}
direct = list(map(int,sys.stdin.readline().rstrip().split()))
for i in range(1, m+1):
    dict_direct[i] = direct[i-1]-1

dict_pri = {}
for number in range(1,m+1):
    temp = []
    for j in range(4):
        t_temp_pri = list(map(int,sys.stdin.readline().rstrip().split()))
        for i in range(len(t_temp_pri)):
            t_temp_pri[i] -= 1
        temp.append(t_temp_pri)
    dict_pri[number] = temp

enable_shark = [i for i in range(1, m+1)]

visited = [[[0, 0] for _ in range(n)] for _ in range(n)]

result = 0
while 1:
    #시간 증가
    result += 1
    if result > 1000:
        result = -1
        break
    # 자신의 위치에 냄새를 뿌림
    spread_smell()
    # 상어가 이동함
    graph = move_shark()
    #겹치는 상어 삭제
    dell_shark()
    #냄새가 줄어들음
    dell_smell()

    if len(enable_shark) == 1:
        break

print(result)

"""
상어는 1 - M  까지 번호가 붙어있음
1이 붙은 상어는 가장 강해서, 모두 쫓아낼 수 있음


def 우선순위 칸 찾기
    상어마다 특정 우선 순위 존재
    같은 상어라도, 현재 방향에 따라 우선순위가 달라짐

상어의 번호/위치/방향 주어짐


자신의 위치에 냄새 뿌림 ( k 번 이동하고 나면 사라짐 --  시작  4     3 2 1 0  (4번이동하면 0이 된다.))
동시에 상하좌우 인접한 칸중 하나로 이동
    1.냄새가 없는 칸
    2. 자신의 냄새가 있는 칸
        - 상어마다 특정 우선 순위를 따름
    
    한칸의 여러마리의 상어가 있으면,  가장 작은거 빼고 모두 쫓아냄

2 2 3
2 0
1 0
1 1
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4


"""