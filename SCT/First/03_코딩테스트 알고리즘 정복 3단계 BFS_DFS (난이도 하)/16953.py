from collections import deque
import sys

"""
1. 숫자를 찾아가는 과정에서, 모든것을 list로 만든다면 memory 초과 발생
2. 증가하는 부분에 대해서 모니터링 안해도 되는건가?
"""

def bfs(x, y):
    q = deque()
    count = 1
    q.append([x, count])

    while q:
        a, n_count = q.popleft()
        if a == y:
            return n_count
        for nx in [2*a, 10*a + 1]:
            if nx <= y:
                q.append([nx, n_count+1])
    return -1


a,b = map(int, sys.stdin.readline().rstrip().split())
result = bfs(a,b)
print(result)