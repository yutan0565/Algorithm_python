from collections import deque
import sys

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0
    count = 0
    while q:
        a = q.popleft()
        if visited[a] == 1 or visited[a] == 2:
            count +=1
        for nx in graph[a]:
            if visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[a] + 1
    return count

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for _ in range(m):
    a,b  = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

result = bfs(1)
print(result)



import sys
from collections import deque

input = sys.stdin.readline

'''
아이디어

start와 거리가 1인 것과 거리가 2인 노드들의 개수를 파악

visited[x, y] : x = 방문 여부, y = 1과의 거리
'''

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for i in range(n + 1)]
visited = [-1 for i in range(n + 1)]

for i in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    count = 0
    now_len = 0
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if visited[node] == 1 or visited[node] == 2:
                count += 1
            for u in graph[node]:
                if visited[u] == -1:
                    visited[u] = visited[node] + 1
                    queue.append(u)
        now_len += 1
        if now_len == 2:
            break
    return count

start = 1
result = bfs(start)
print(result)

