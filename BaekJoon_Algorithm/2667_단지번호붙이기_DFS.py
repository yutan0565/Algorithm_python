import sys

n = int(sys.stdin.readline().rstrip())
graph = [ list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
result  = []


def dfs(x, y):
    global graph, n, visited, house_max
    dx = [0 ,1, 0, -1]
    dy = [1 ,0, -1, 0]
    visited[x][y] = True
    graph[x][y] = -1
    house_max += 1
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if visited[nx][ny] != True:
                if graph[nx][ny] == 1:
                    dfs(nx, ny)
    return house_max


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house_max = 0
            house_max = dfs(i,j)
            result.append(house_max)

result.sort()
print(len(result))

for i in result:
    print(i)


