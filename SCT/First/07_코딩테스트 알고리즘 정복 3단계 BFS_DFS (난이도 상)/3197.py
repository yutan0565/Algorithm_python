from collections import deque
import sys

def bfs_melt_ice():
    q_temp = deque()
    while q_melt:
        a,b = q_melt.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if visited_melt[nx][ny] == -1:
                    if graph[nx][ny] == 'X':
                        q_temp.append([nx,ny])
                        graph[nx][ny] = '.'
                        visited_melt[nx][ny] = 1
                    else:
                        q_melt.append([nx,ny])
                        visited_melt[nx][ny] = 1
    return q_temp


def bfs_is_met():
    q_temp = deque()
    while q_baek:
        a,b = q_baek.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<r and 0<=ny<c:
                if visited_baek[nx][ny] == -1:
                    if graph[nx][ny] == '.':
                        q_baek.append([nx,ny])
                        visited_baek[nx][ny] = 1
                    else:
                        q_temp.append([nx,ny])
                        visited_baek[nx][ny] = 1
                    if [nx, ny] == end:
                        return 1, q_temp

    return -1, q_temp

r,c = map(int ,sys.stdin.readline().rstrip().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

graph = []
baekjo = []

q_baek = deque()
visited_baek = [[-1 for _ in range(c)] for j in range(r)]

q_melt = deque()
visited_melt = [[-1 for _ in range(c)] for j in range(r)]


for i in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))
    for j in range(c):
        if graph[i][j] == 'L':
            baekjo.append([i,j])
            q_melt.append([i, j])
        if graph[i][j] == '.':
            q_melt.append([i, j])
            visited_melt[i][j] = 1
start = baekjo[0]
end = baekjo[1] 

q_baek.append(start)
visited_baek[start[0]][start[1]] = 1

result = 0

while 1:
    is_met, q_baek = bfs_is_met()
    if is_met == 1:
        break
    q_melt = bfs_melt_ice()
    result += 1
print(result)