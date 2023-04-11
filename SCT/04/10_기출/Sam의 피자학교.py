import copy
import sys

def make_info():
    end, height, width = [],[],[]

    for w in range(1,n):
        width.append(w)
        width.append(w)

    height = width[1:]

    point = 0
    for h in height:
        end.append(point)
        point += h
    return end, height, width


def add_mil():
    min_value = min(graph[-1])
    for i in range(n):
        if graph[-1][i] == min_value:
            graph[-1][i] += 1

def rotation_right(now_height, now_width, now_block):
    new_width, new_height = now_height, now_width
    new_block =  [[0 for _ in range(new_width)] for _ in range(new_height)]
    for i in range(now_height):
        for j in range(now_width):
            new_block[j][new_width-1-i] = now_block[i][j]
    return new_block, new_width, new_height

def rotation_180(now_height, now_width, now_block):
    new_block =  [[0 for _ in range(now_width)] for _ in range(now_height)]
    for i in range(now_height):
        for j in range(now_width):
            new_block[now_height-1-i][now_width-1-j] = now_block[i][j]
    return new_block

def roll_dow():
    for index in range(n):
        now_end = end[index]
        next_end = end[index+1]
        if next_end > n-1:
            break
        else:
            if index == 0:
                graph[n-1][0], graph[n-2][1] = graph[n-2][1], graph[n-1][0]
            else:
                now_height = height[index]
                now_width = width[index]
                now_block = [[0 for _ in range(now_width)] for _ in range(now_height)]

                for i in range(n):
                    for j in range(n):
                        if n-now_height<=i<n and now_end+1-now_width<=j<now_end+1:
                            nx = i-n+now_height
                            ny = j-now_end-1+now_width
                            now_block[nx][ny] = graph[i][j]
                            graph[i][j] = 0
                # 블럭 오른쪽 돌리기
                new_block, new_width, new_height = rotation_right(now_height, now_width, now_block)
                next_height = height[index+1]
                for i in range(new_height):
                    for j in range(new_width):
                        nx = n-next_height+i
                        ny = now_end+1+j
                        graph[nx][ny] = new_block[i][j]

def fold_dow():
    for i in range(2):
        if i == 0:
            block = graph[-1]
            block = block[:n//2]
            new_block = []
            for b in block:
                new_block = [b] + new_block

            for i in range(n//2):
                graph[-1][i] = 0
                graph[n - 2][n // 2 + i] = new_block[i]

        elif i == 1:
            now_end = n//2 + n//4-1
            now_height = 2
            now_width = n//4
            now_block = [[0 for _ in range(now_width)] for _ in range(now_height)]

            for i in range(n):
                for j in range(n):
                    if n - now_height <= i < n and now_end + 1 - now_width <= j < now_end + 1:
                        nx = i - n + now_height
                        ny = j - now_end - 1 + now_width
                        now_block[nx][ny] = graph[i][j]
                        graph[i][j] = 0

            # 블럭 180 돌리기
            new_block = rotation_180(now_height, now_width, now_block)
            next_height = 4
            for i in range(now_height):
                for j in range(now_width):
                    nx = n - next_height + i
                    ny = now_end + 1 + j
                    graph[nx][ny] = new_block[i][j]


def push_dow():
    new_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 1:
                now_mil = graph[i][j]
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] >= 1:
                            other_mil = graph[nx][ny]
                            gap = abs(now_mil - other_mil)//5
                            if now_mil > other_mil:
                                new_graph[i][j] -= gap
                            elif now_mil < other_mil:
                                new_graph[i][j] += gap

    new_line = []
    for j in range(n):
        for i in range(n-1,-1,-1):
            if new_graph[i][j] >= 1:
                new_line.append(new_graph[i][j])

    new_graph = [[0 for _ in range(n)] for _ in range(n-1)] + [new_line]
    return new_graph

n,k = map(int,sys.stdin.readline().rstrip().split())
graph = [[0 for _ in range(n)] for _ in range(n-1)] + [list(map(int,sys.stdin.readline().rstrip().split()))]

end,height,width = make_info()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

result = 0
while 1:
    if max(graph[-1]) - min(graph[-1]) <= k:
        break
    # 밀가루 추가
    add_mil()
    # 도우 말기
    roll_dow()
    # 도우 누르기
    graph = push_dow()
    # 반 반 접기
    fold_dow()
    # 도우 누르기
    graph = push_dow()

    result += 1
print(result)