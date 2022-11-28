from collections import deque
import sys
"""
1. leaf 가 중각에 있나 없나 체크를 하고 !!, 그다음에 count 해주기
"""
def bfs():
    q = deque()
    q.append(root)
    count = 0

    if root == del_node:
        return count

    while q:
        a = q.popleft()
        flag = 0
        for nx in graph[a]:
            if nx != del_node:
                q.append(nx)
                flag = 1
        if flag == 0:
            count += 1
    return count

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n)]
root = -1


node_input = list(map(int ,sys.stdin.readline().rstrip().split()))

for i in range(n):
    parent = node_input[i]
    if parent != -1:
        graph[parent].append(i)
    else:
        root = i
del_node = int(sys.stdin.readline().rstrip())

result = bfs()
print(result)
