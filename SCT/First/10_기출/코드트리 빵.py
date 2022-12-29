import copy
from collections import deque
import sys

# 가까운 베이스 캠프를 차고
# 그다음에 마트를 찾아 가기

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def fine_base_camp(t):
    q = deque()
    x = want_mart[t][0]
    y = want_mart[t][1]
    q.append([x,y])
    visited_dict[t][x][y] = 1
    cand_camp = []
    while q:
        for _ in range(len(q)):
            a,b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if visited_dict[t][nx][ny] == -1:
                        if graph[nx][ny] == 0:
                            q.append([nx,ny])
                            visited_dict[t][nx][ny] = 1
                        elif graph[nx][ny] == 1:
                            if [nx,ny] in camp_list:
                                cand_camp.append([nx,ny])
        if len(cand_camp) != 0:
            cand_camp.sort(key = lambda x: (x[0], x[1]))
            start_camp = cand_camp[0]
            start_dict[t] = start_camp
            camp_list.remove(start_camp)
            visited_dict[t] = copy.deepcopy(reset_visited)
            break

def bfs():
    q = deque()
    time = 1
    fine_base_camp(time)
    x = start_dict[time][0]
    y = start_dict[time][1]
    visited_dict[time][x][y] = 1
    graph[x][y] = 2
    in_people.append(time)

    # x,y,.  people name
    q.append([x,y,1])

    end_list = []

    while q:
        if time <= m :
            if time not in in_people:
                fine_base_camp(time)
                x = start_dict[time][0]
                y = start_dict[time][1]
                visited_dict[time][x][y] = 1
                graph[x][y] = 2
                in_people.append(time)
                q.append([x, y, time])

        for _ in range(len(q)):
            a,b, peo= q.popleft()
            if a == want_mart[peo][0] and b == want_mart[peo][1]:
                end_list.append([a,b])
                graph[a][b] = 2
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if visited_dict[peo][nx][ny] == -1:
                        if graph[nx][ny] == 0 or graph[nx][ny] == 1:
                            q.append([nx,ny,peo])
                            visited_dict[peo][nx][ny] = 1

        if len(end_list) == m:
            break
        time += 1
    return time

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
camp_list = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if graph[i][j] == 1:
            camp_list.append([i,j])
reset_visited = [[-1 for _ in range(n)] for _ in range(n)]

want_mart = {}
visited_dict = {}
start_dict = {}
in_people = []
for i in range(1, m+1):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    want_mart[i] = [a-1,b-1]
    visited_dict[i] = copy.deepcopy(reset_visited)


result = bfs()
print(result)