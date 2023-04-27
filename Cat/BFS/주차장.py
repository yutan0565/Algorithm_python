from collections import deque,defaultdict
import sys

def bfs(car_num):
    s_x,s_y = dict_car[car_num]
    q = deque()
    q.append([s_x,s_y])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visited[s_x][s_y] = 0
    total_park = park_count
    while q:
        a,b = q.popleft()
        if type(graph[a][b]) == type(1):
            dict_dis[car_num][graph[a][b]] = visited[a][b]
            total_park -= 1
            if total_park == 0:
                break
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == -1:
                    if graph[nx][ny] != "X":
                        q.append([nx,ny])
                        visited[nx][ny] = visited[a][b] + 1

# https://velog.io/@ashooozzz/Python-%EC%9D%B4%EB%B6%84-%EB%A7%A4%EC%B9%ADfeat.-DFS
def bin_match(now_car,park_list,visited, mid):
    for park_num in range(park_count):
        if visited[park_num] == -1:
            now_dis = dict_dis[now_car][park_num]
            if now_dis < mid:
                visited[park_num] = 1
                if park_list[park_num] == - 1 or bin_match(park_list[park_num],park_list,visited, mid):
                    park_list[park_num] = now_car
                    return 1
    return 0

def find_max_dis(park_list):
    max_dis = 0
    for i in range(park_count):
        now_park_car = park_list[i]
        if now_park_car != -1:
            max_dis = max(max_dis, dict_dis[now_park_car][i])
    return max_dis

def bin_search():
    left,right = 0,2500
    result = 2e10
    while 1:
        if left == right:
            break
        # 시간 기준을 정하기
        mid = (left + right)//2
        park_list = [-1 for _ in range(park_count)]
        fail_flag = 0
        # 주차 시도는 다 해보기
        for car_num in range(car_count):
            visited = [-1 for _ in range(park_count)]
            park_flag = bin_match(car_num,park_list,visited, mid)
            # 주차 성공 // 다음 차 주차
            if park_flag == 1:
                continue
            # 추차 실패
            else:
                fail_flag = 1
                break
        # 모든 차가 주차된 경우
        if fail_flag != 1:
            max_dis = find_max_dis(park_list)
            result = min(max_dis, result)
            right = mid
        # 주차못한 차가 남은 경우
        else:
            left = mid + 1

    if result == 2e10:
        result = -1
    return result


n,m = map(int,sys.stdin.readline().rstrip().split())
graph = []
dict_car = {}
car_count = 0
park_count = 0
for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if graph[i][j] == "C":
            dict_car[car_count] = [i,j]
            graph[i][j] = "."
            car_count+= 1
        elif graph[i][j] == "P":
            graph[i][j] = park_count
            park_count+= 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]
max_time = n*m+1
# 차가 없느 경우
if car_count == 0:
    print(0)
# 주차 자리 < 차의 개수
elif park_count < car_count:
    print(-1)
else:
    # 각 차와 주차장 사이의 거리
    dict_dis = {}
    for car_num in range(car_count):
        dict_dis[car_num] = [2e10 for _ in range(park_count)]
        bfs(car_num)
    # for key in dict_dis.keys():
    #     print(key, dict_dis[key])
    # 최소 시간 -> 시간별 탐색
    result = bin_search()
    print(result)

"""
4 7
.....CP
......X
.C....P
......P


"""

