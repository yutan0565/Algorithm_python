from collections import deque
import sys

def bfs(t_left, t_right):
    q = deque()
    q.append([0,0])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[0][0] = 1
    while q:
        a,b = q.popleft()
        if [a,b] == [n-1, n-1]:
            return 1
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1:
                    if t_left <= graph[nx][ny] <= t_right:
                        visited[nx][ny] = 1
                        q.append([nx, ny])
    return 0

def check_bfs(mid):
    for i in range(min_value, max_value + 1):
        if i <= start_value <= i + mid and i <= end_value <= i + mid:
            bfs_flag = bfs(i, i + mid)
            if bfs_flag == 1:
                return 1
    return 0

def bin_search(left, right):
    result = 0
    while 1:
        if left > right:
            break
        mid = (left + right) // 2
        check_flag = check_bfs(mid)
        # 최소 값이 왼쪽에 있는 경우
        if check_flag == 1:
            result = mid
            right = mid - 1
        # 최소 값이 오른쪽에 있는 경우
        elif check_flag == 0:
            left = mid + 1
    return result


n = int(sys.stdin.readline().rstrip())
graph = []

min_value, max_value = 201, -1

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))
    for j in range(n):
        now_value = graph[i][j]
        min_value = min(min_value, now_value)
        max_value = max(max_value, now_value)

start_value, end_value = graph[0][0], graph[n-1][n-1]

# 위 우 아 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = bin_search(0, max_value)
print(result)
