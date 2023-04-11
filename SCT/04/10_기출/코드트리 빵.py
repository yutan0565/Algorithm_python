import copy
import sys
from collections import deque
from collections import defaultdict

def find_base_camp(num):
    x,y = dict_mart[num]
    q = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    candi_load = [[x,y]]

    q.append([x,y,candi_load])
    visited[x][y] = 1

    while q:
        a,b,load = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] == 0:
                        new_load = copy.deepcopy(load)
                        new_load = [[nx,ny]] + new_load
                        q.append([nx,ny, new_load])
                        visited[nx][ny] = 1
                    elif graph[nx][ny] == 1:
                        dict_load[num] = load
                        dict_camp[num] = [nx,ny]
                        dict_pos[num] = [nx,ny]
                        graph[nx][ny] = -1
                        return

def find_new_load(num):
    x,y = dict_mart[num]
    q = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    candi_load = []

    q.append([x,y,candi_load])
    visited[x][y] = 1

    while q:
        a,b,load = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == -1:
                    if [nx,ny] == dict_mart[num]:
                        load = load + [[nx,ny]]
                        dict_load[num] = load
                        return
                    else:
                        new_load = copy.deepcopy(load)
                        new_load = new_load + [[nx,ny]]
                        q.append([nx, ny, new_load])
                        visited[nx][ny] = 1


def move_people(num):
    x,y = dict_pos[num]
    nx,ny = dict_load[num][0]
    del dict_load[num][0]

    # 목적지인 경우
    if [nx,ny] == dict_mart[num]:
        # num 지우고 초기화
        list_arrive[num] = 0
        dict_mart[num] = []
        dict_camp[num] = []
        dict_pos[num] = []
        dict_load[num] = []
        graph[nx][ny] = -1
    # 못가는 곳 -> 새로운 길 찾기
    elif graph[nx][ny] == -1:
        # 지금 기준으로 새로운 길 찾기
        find_new_load(num)
    # 갈 수 있는 곳
    else:
        dict_pos[num] = [nx,ny]


n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
dict_mart = defaultdict(lambda :[])
dict_camp = defaultdict(lambda :[])
dict_pos = defaultdict(lambda :[])
dict_load = defaultdict(lambda :[])
list_arrive = [0 for _ in range(m+1)]

dx = [-1,0,0,1]
dy = [0,-1,1,0]

for num in range(1,m+1):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    x,y = x-1,y-1
    dict_mart[num] = [x,y]
    list_arrive[num] = 1

def show_info():
    for g in graph:
        print(g)
    print("캠프 : ",dict(dict_camp))
    print("마트 : ",dict(dict_mart))
    print("로드 : ",dict(dict_load))
    print("위치 : ",dict(dict_pos))

time = 1
while 1:
    # 시간 안에 있는 사람이면
    if time <= m:
        # base camp 찾기
        find_base_camp(time)
    for num in range(1,m+1):
        if num <= time:
            # 살아 있는 사람
            if list_arrive[num] == 1:
                # 지금 막 배치된 사람 제외
                if num != time:
                    # 한칸 이동하기
                    move_people(num)
    if sum(list_arrive) == 0:
        break
    time += 1

print(time)