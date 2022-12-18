from collections import deque
import sys

"""
1. q 의 길이만큼 돌려주기 !! (시간 당 그래프가 변하는 경우 고고)

2. graph update 방식 !!! 저거 기억해두기

3. visited를 초기화 해주는 시점.... !   
    -- graph가 변할 때 마다, 최적 경로가 바뀌기 때문에, graph 바꾼 이후에, 
    visited 초기화 해주기
"""

def bfs():
    global graph
    q = deque()
    q.append([start[0], start[1]])

    dx = [0,0,0,1,-1, 1, 1, -1, -1]
    dy = [0,1,-1,0,0, 1, -1 , 1, -1]

    while q:
        visited = [[-1 for _ in range(8)] for _ in range(8)]
        for _ in range(len(q)):
            a,b = q.popleft()
            if a == end[0] and b == end[1]:
                return 1
            if graph[a][b] == '#':
                continue
            for i in range(9):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0<=nx<8 and 0<=ny<8:
                    if graph[nx][ny] != '#':
                        if visited[nx][ny] == -1:
                            q.append([nx,ny])
                            visited[nx][ny] = 1
        graph = new_line + graph
        graph = graph[:8][:]
    return 0

graph = [ list(sys.stdin.readline().rstrip()) for _ in range(8) ]
new_line = [['.' for _ in range(8)]]

start = [7, 0]
end = [0, 7]

result = bfs()
print(result)

