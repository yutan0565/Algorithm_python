from collections import deque
import sys

def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1
    dx = [1,2,3,4,5,6]

    while q:
        a= q.popleft()
        if a == 100:
            return graph[100]
        for i in range(6):
            nx = a + dx[i]
            if 0<=nx<101:
                if nx in sad.keys():
                    nx = sad[nx]
                if nx in bam.keys():
                    nx = bam[nx]
                if visited[nx]== -1:
                    q.append(nx)
                    visited[nx] = 1
                    graph[nx] = graph[a] + 1




n,m = map(int, sys.stdin.readline().rstrip().split())
graph =[0]*101
visited = [1] +  [-1]*100
sad = {}
bam = {}

for i in range(n):
    x,y = map(int, sys.stdin.readline().rstrip().split())
    sad[x] = y
    # 1은 사다리

for i in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    bam[u] = v
    # 2는 뱀

result = bfs()
print(result)