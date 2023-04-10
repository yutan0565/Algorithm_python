from collections import deque
import sys

def bfs():
    q = deque()
    q.append(x)
    visited[x] = 0
    while q:
        a = q.popleft()
        if visited[a] == k:
            result.append(a)
        for nx in graph[a]:
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[a] + 1


n,m,k,x = map(int ,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
result = []


for _ in range(m):
    a,b = map(int ,sys.stdin.readline().rstrip().split())
    graph[a].append(b)

bfs()
result.sort()

if len(result) == 0:
    print(-1)
elif len(result) > 0:
    for r in result:
        print(r)



import sys
from collections import deque

input = sys.stdin.readline

'''
아이디어

특정노드(출발도시)에서 거리가 K인 모든 노드를 출력하는 문제

1. visited에 거리 정보(start부터의 거리)를 넣는다

2. while 문 안에서 visited[node] 값이 K 이면 저장
'''

N, M, K, start = map(int, input().rstrip().split())
graph = [[] for i in range(N + 1)]
visited = [-1 for i in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    temp_result = []

    while queue:
        a = queue.popleft()
        if visited[a] == K:
            temp_result.append(a)
        for nx in graph[a]:
            if visited[nx] == -1:
                queue.append(nx)
                visited[nx] = visited[a] + 1
    return temp_result

result = bfs(start)
if result:
    print(*sorted(result), sep='\n')
else:
    print(-1)
