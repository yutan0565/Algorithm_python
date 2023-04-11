from collections import deque
import sys

"""
내가 가는 곳이 아직 방문을 안했거나,
이미 방문한 곳이면(-1이 아닌경우면) , 같은 방식으로 도달한 곳이기 때문에, 똑같은 
시간으로 업데이트 해주기 
-- 근데 들렸던, 모든 수  1 4  인 경우,  2와 4는 2번 갱신 가능함
"""

def bfs():
    q = deque()
    q.append(n)
    visisted[n] = 0

    count = 0
    while q:
        a = q.popleft()
        if a == k:
            count += 1
        for nx in [2*a, a+1, a-1]:
            if 0<=nx<100001:
                if visisted[nx] == -1 or visisted[nx] == visisted[a] + 1:
                    visisted[nx] = visisted[a] + 1
                    q.append(nx)
    return visisted[k], count

n,k = map(int,sys.stdin.readline().rstrip().split())
visisted = [-1 for _ in range(100001)]


result_min, result_count = bfs()
print(result_min)
print(result_count)