import sys
from collections import deque

def bfs():
    q = deque()
    x = n
    time = 0
    q.append((n, time))
    visited[x][0] = 0
    while q:
        for _ in range(len(q)):
            a, time = q.popleft()
            for type in range(3):
                if type == 0:
                    nx = a + 1
                elif type == 1:
                    nx = a - 1
                elif type == 2:
                    nx = 2 * a
                if 0 <= nx < max_point+1:
                    if visited[nx][(time + 1) % 2] == -1:
                        q.append((nx, time + 1))
                        visited[nx][(time + 1) % 2] = time + 1

def cal_time():
    global k
    result = -1
    time = 0
    for i in range(max_point+1):
        k += i
        if k > max_point:
            break
        if visited[k][time % 2] <= time:
            result = time
            break
        time += 1
    return result

n,k = map(int, sys.stdin.readline().rstrip().split())

max_point = 500000

visited = [[-1, -1] for _ in range(max_point+1)]

bfs()
result = cal_time()
print(result)