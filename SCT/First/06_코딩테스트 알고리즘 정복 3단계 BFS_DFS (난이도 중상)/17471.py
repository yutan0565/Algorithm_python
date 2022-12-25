from collections import deque
import sys
from itertools import combinations

def bfs(group, start):
    q = deque()
    q.append(start)
    visited = [-1 for _ in range(n+1)]
    visited[start] = 1

    count = p_list[start]

    while q:
        a = q.popleft()
        for nx in graph[a]:
            if nx in group:
                if visited[nx] == -1:
                    q.append(nx)
                    visited[nx] = 1
                    count += p_list[nx]
    return count


n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]

p_list = [0] + list(map(int,sys.stdin.readline().rstrip().split()))
p_sum = sum(p_list)

for i in range(1,n+1):
    info_list = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(1, len(info_list)):
        graph[i].append(info_list[j])

result = 100000

for i in range(1, n):
    g_case = list(combinations(range(1, n+1),i))

    for a_group in g_case:
        a_start = a_group[0]
        b_group = [ b for b in range(1,n+1) if b not in a_group]
        b_start = b_group[0]
        first = bfs(a_group, a_start)
        second = bfs(b_group, b_start)

        if first + second == p_sum:
            result = min(result, abs(first-second))

if result == 100000:
    print(-1)
else:
    print(result)


