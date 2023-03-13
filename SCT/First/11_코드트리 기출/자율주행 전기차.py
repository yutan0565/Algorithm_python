import sys
from collections import deque

def find_people(x,y):
    global q, result
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 0
    if graph[x][y] >= 2:
        end_point = end_dict[graph[x][y]]
        graph[x][y] = 0
        return end_point
    while q:
        candi_list = []
        for _ in range(len(q)):
            a,b,now_c = q.popleft()
            if now_c == 0:
                return [-1,-1]
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny] == -1:
                        if graph[nx][ny] == 0:
                            q.append([nx,ny,now_c-1])
                            visited[nx][ny] = 1
                        elif graph[nx][ny] >= 2: # 특정 사람이 있는 경우
                            candi_list.append([nx,ny, now_c-1])
                            visited[nx][ny] = 1
        if len(candi_list) != 0:
            candi_list.sort(key = lambda x: (x[0], x[1]))
            nx = candi_list[0][0]
            ny = candi_list[0][1]
            new_b = candi_list[0][2]
            q = deque()
            q.append([nx, ny, new_b])
            result = new_b
            end_point = end_dict[graph[nx][ny]]
            graph[nx][ny] = 0
            return end_point
    return [-1,-1]

def find_end(end_point):
    global q, result
    x,y = q[0][0], q[0][1]
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 0
    move = 0
    while q:
        for _ in range(len(q)):
            a, b, now_c = q.popleft()
            if now_c == 0:
                return -1
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if visited[nx][ny] == -1:
                        if [nx,ny] == end_point:  # 특정 사람이 있는 경우
                            q = deque()
                            new_c = (now_c-1) + (move +1)*2
                            q.append([nx, ny, new_c])
                            result = new_c
                            return result
                        elif graph[nx][ny] != 1:
                            q.append([nx, ny, now_c - 1])
                            visited[nx][ny] = 1

        move += 1
    return -1


n,m,c = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
start = list(map(int,sys.stdin.readline().rstrip().split()))
start = [start[0]-1, start[1]-1]
people_pos = []
clear_people_count = 0

dx = [-1,0,0,1]
dy = [0,-1,1,0]

end_dict = {}

for count in range(2,m+2):
    s_x,s_y,e_x,e_y = map(int,sys.stdin.readline().rstrip().split())
    s_x,s_y,e_x,e_y = s_x-1,s_y-1,e_x-1,e_y-1
    graph[s_x][s_y] = count
    end_dict[count] = [e_x, e_y]

result = 0
q = deque()
q.append([start[0], start[1], c])
def show_graph():
    print("-"*20)
    for g in graph:
        print(g)

while 1:
    # 사람 찾기
    start = find_people(start[0], start[1])
    if start == [-1,-1]:
        result= - 1
        break
    # 그 위치에서, 도착지점 찾기
    flag = find_end(start)
    if flag == -1:
        result = - 1
        break
    clear_people_count += 1
    if clear_people_count == m:
        break

print(result)