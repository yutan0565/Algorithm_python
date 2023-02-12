import copy
from collections import deque
import sys

def bfs(x, y):
    q = deque()
    q.append(x)
    visited[x] = 0

    while q:
        a = q.popleft()
        if a == y:
            return visited[a]
        for jump in range(1, graph[a]+1):
            nx = a + jump
            if nx <= y:
                if visited[nx] == -1:
                    visited[nx] = visited[a] + 1
                    q.append(nx)
    return -1


n = int(sys.stdin.readline().rstrip())
graph = list(map(int, sys.stdin.readline().rstrip().split()))
visited = [-1 for _ in range(n)]

result = bfs(0, n-1)
print(result)


import sys
from collections import deque

input = sys.stdin.readline

'''
아이디어

최소 점프이므로, visited에 원래 있던 값과 비교해서 작은 값을 넣어주면 됨
'''

N = int(input().strip())
reset_graph = list(map(int, input().rstrip().split()))
reset_visited = [-1 for i in range(N)]

start = 0
end = N - 1

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        node = queue.popleft()
        if node == end:
            return visited[end]
        if graph[node] == 0:   # ??
            continue
        for jump in range(1, graph[node]+1):
            new_node = node + jump
            if new_node <= N - 1:
                if visited[new_node] == -1:
                    visited[new_node] = visited[node] + 1
                    queue.append(new_node)

    return visited[end]

graph = copy.deepcopy(reset_graph)
visited = copy.deepcopy(reset_visited)
print(bfs(start))