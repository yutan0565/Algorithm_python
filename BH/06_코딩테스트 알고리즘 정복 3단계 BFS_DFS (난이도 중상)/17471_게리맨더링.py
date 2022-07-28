import sys
from collections import deque
from itertools import combinations

## 다시


def bfs(ggg):
    start = ggg[0]
    q = deque()
    q.append(start)
    visited = [False for _ in range(n)]

    visited[start] = True
    sum = pp[start]

    while q:
        a = q.popleft()
        for nx in graph[a]:
            if visited[nx] == False:
                if nx in ggg:
                    q.append(nx)
                    visited[nx] = True
                    sum += pp[nx]
    count = 0
    for v in visited:
        if v == True:
            count +=1

    return sum, count


n = int(sys.stdin.readline().rstrip())
pp = list(map(int,sys.stdin.readline().rstrip().split()))
graph = [ [] for _ in range(n) ]
result = float('inf')

for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(1, temp[0]+1):
        graph[i].append(temp[j]-1)

node_list = [i for i in range(n)]

for i in range(1, n//2 + 1):
    group = list(combinations(node_list, i))
    for gro in group:
        other_gro = [i for i in range(n) if i not in gro]
        sum1, count1 = bfs(gro)
        sum2, count2 = bfs(other_gro)
        if count1 + count2 == n:
            result = min(result, abs(sum1 -sum2))

if result != float('inf'):
    print(result)
else:
    print(-1)




