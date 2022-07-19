import sys
from collections import deque

def bfs(visited, x, k, max):
    q = deque()
    q.append(x)
    visited[x] = 0
    if x == k:
        return 0

    while q:
        a = q.popleft()
        if a ==k:
            return visited[a]
        nx_list = [a-1, a+1, 2*a]
        for nx in nx_list:
            if 0 <= nx <= max:
                if visited[nx] == -1:
                    q.append(nx)
                    visited[nx] = visited[a]+ 1

n, k = map(int, sys.stdin.readline().rstrip().split())
max = 100000

if n > k:
    print(n-k)
else:
    visited = [-1] * (max+1)
    result = bfs(visited, n, k, max)
    print(result)