from collections import deque
import sys

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    ice_count = 1

    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<graph_size and 0<=ny<graph_size:
                if graph[nx][ny] != 0:
                    if visited[nx][ny] == -1:
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        ice_count += 1
    return ice_count


def fire(x,y):
    for i in range(b_size):
        for j in range(b_size):
            fire_graph[x+j][y+b_size-i-1] = graph[x+i][y+j]

def tornado():
    for i in range(graph_size):
        for j in range(graph_size):
            ice_count = 0
            if 0<=i-1 and fire_graph[i-1][j] >=1:
                ice_count+=1
            if 0<=j-1 and fire_graph[i][j-1] >=1:
                ice_count+=1
            if i+1< graph_size and fire_graph[i+1][j] >=1:
                ice_count += 1
            if j + 1 < graph_size and fire_graph[i][j+1] >= 1:
                ice_count += 1

            if ice_count >= 3 or fire_graph[i][j] == 0 :
                tornado_graph[i][j] = fire_graph[i][j]
            else:
                tornado_graph[i][j] = fire_graph[i][j] - 1



    """
    2  4
    
    2+0 4+0   0 b_size -1           i  j    ///   j  size-i-1
    2+0 4+1   1 b_size -1 
    
    1 0   0 b_size-2
    1 2   1 b_size -2 
    
    
    b_size-1 0         1  b_size - bsize
    b_szie-1 b_size-1  b_size-1   0
    """


def sum_2d(list_2d):
    sum = 0
    for i in range(graph_size):
        for j in range(graph_size):
            sum += graph[i][j]
    return sum

n,q = map(int,sys.stdin.readline().rstrip().split())
graph_size = 2**n
graph = [ list(map(int ,sys.stdin.readline().rstrip().split())) for _ in range(graph_size)]
visited = [[-1 for _ in range(graph_size)] for _ in range(graph_size)]



magic_list = list(map(int,sys.stdin.readline().rstrip().split()))

for level in magic_list:
    fire_graph = [ [0 for _ in range(graph_size)] for _ in range(graph_size)]
    b_size = 2**level

    for i in range(0,graph_size, b_size):
        for j in range(0, graph_size, b_size):
            # 시작 점들만 모아둠
            fire(i,j)
    # rotation 끝난거에서, 줄이기
    tornado_graph = [ [0 for _ in range(graph_size)] for _ in range(graph_size)]
    tornado()
    graph = tornado_graph

sum_result = sum_2d(graph)
bfs_result = 0

for i in range(graph_size):
    for j in range(graph_size):
        if graph[i][j] != 0:
            if visited[i][j] == -1:
                temp = bfs(i,j)
                bfs_result = max(temp, bfs_result)



print(sum_result)
print(bfs_result)
