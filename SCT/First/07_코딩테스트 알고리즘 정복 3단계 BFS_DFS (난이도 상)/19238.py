from collections import deque
import sys
import copy

""""
1. 최적경로를 쓰는 경우가 다르면, 각가의 bfs 만들어서 사용 해주기 !!
2. 결과를 확인 해주는 if 문 위치 제대로 확인 해주기 !! q 가 끝나버리면 if문도 돌지 못해버림 
"""

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs_find_people():
    global gas
    q = deque()
    q.append(taxi_point)
    visited = copy.deepcopy(reset_visited)
    visited[taxi_point[0]][taxi_point[1]] = gas

    start_list = []
    while q:
        for _ in range(len(q)):
            a,b = q.popleft()
            if visited[a][b] < 0:
                return [-1,-1], [-1,-1]
            for p in p_info:
                if [a,b] == p[0]:
                    start_list.append([p[0], p[1], visited[a][b]])
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if graph[nx][ny] != 1:
                        if visited[nx][ny] == -1:
                            q.append([nx,ny])
                            visited[nx][ny] = visited[a][b] - 1
        if len(start_list)!= 0:  # 이게 앞에 있으면은, 구석에 있는 칸에 대해서 조사 불가능 ! ㅠ
            start_list.sort(key = lambda x: (x[0][0], x[0][1]))
            gas = start_list[0][2]
            return start_list[0][0], start_list[0][1]

    return [-1, -1], [-1, -1]


def bfs_go_des():
    global gas
    q = deque()
    q.append(start_point+[0])
    visited = copy.deepcopy(reset_visited)
    visited[start_point[0]][start_point[1]] = gas
    while q:
        a,b, km = q.popleft()
        if visited[a][b] < 0:
            return [-1,-1]
        if [a,b] == end_point:
            gas = visited[a][b]
            gas += (km*2)
            p_info.remove([start_point, end_point])
            return end_point
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] != 1:
                    if visited[nx][ny] == -1:
                        q.append([nx,ny, km +1])
                        visited[nx][ny] = visited[a][b] - 1
    return [-1,-1]

n,m,gas = map(int, sys.stdin.readline().rstrip().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

taxi_start = list(map(int, sys.stdin.readline().rstrip().split()))
reset_visited = [[-1 for _ in range(n)] for _ in range(n)]

p_info = []
for _ in range(m):
    a,b,c,d = map(int, sys.stdin.readline().rstrip().split())
    p_info.append([[a-1,b-1],[c-1,d-1]])

taxi_point = [ i-1 for i in taxi_start]
end_point = []
result = 0

for _ in range(m):
    start_point, end_point = bfs_find_people()
    if start_point == [-1,-1] and end_point == [-1,-1]:
        result = -1
        break
    taxi_point = bfs_go_des()
    if taxi_point == [-1,-1]:
        result = -1
        break

if result == -1:
    print(result)
else:
    print(gas)


