import sys
from collections import deque

def bfs(left_cut,right_cut) :
    q = deque()
    visited = [[max_num for _ in range(n)] for _ in range(n)]
    if left_cut <= height_graph[e_x][e_y] <= right_cut :
        q.append((e_x, e_y, 0))
        visited[e_x][e_y] = 0
    while q :
        a,b, count = q.popleft()
        new_count = count + 1
        for d in range(8) :
            nx = a + dx[d]
            ny = b + dy[d]
            if 0<= nx < n and 0<= ny< n :
                if  left_cut <= height_graph[nx][ny] <= right_cut:
                    if visited[nx][ny] > new_count :
                        visited[nx][ny] = new_count
                        q.append((nx, ny, new_count))
    for x,y in home_list :
        if visited[x][y] == max_num :
            return -1
    return 1

def find_min_value():
    left_index, right_index = 0, 0
    result = max_num

    while left_index <= len(height_list) - 1 and right_index <= len(height_list) - 1:
        left_cut = height_list[left_index]
        right_cut = height_list[right_index]
        if right_index == len(height_list) - 1:
            flag = bfs(left_cut, right_cut)
            if flag == True:
                left_index += 1
                result = min(result, right_cut - left_cut)
            else:
                break
        else:
            flag = bfs(left_cut, right_cut)
            if flag == True:
                left_index += 1
                result = min(result, right_cut - left_cut)
            else:
                right_index += 1
    return result

n = int(sys.stdin.readline().rstrip())
e_x,e_y = -1,-1
home_list = []
graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))
    for j in range(n):
        if graph[i][j] == "P":
            e_x,e_y  = i,j
        elif graph[i][j] == "K":
            home_list.append([i,j])

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

height_graph = []
height_list = []
for i in range(n) :
    height_graph.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n) :
        height_list.append(height_graph[i][j])
height_list.sort()
max_num = 2e10

result = find_min_value()
print(result)