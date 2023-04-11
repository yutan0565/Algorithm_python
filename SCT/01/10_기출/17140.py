import sys

def rotation_90_right(graph):
    row_len = len(graph)
    col_len = len(graph[0])
    new_graph = [[0 for _ in range(row_len)] for _ in range(col_len)]
    for i in range(row_len):
        for j in range(col_len):
            new_graph[j][row_len - 1 - i] = graph[i][j]
    return new_graph

def rotation_90_left(graph):
    row_len = len(graph)
    col_len = len(graph[0])
    new_graph = [[0 for _ in range(row_len)] for _ in range(col_len)]
    for i in range(row_len):
        for j in range(col_len):
            new_graph[col_len-1-j][i] = graph[i][j]
    return new_graph

def change(graph):
    row_len = len(graph)
    max_len =    -1
    new_graph = []
    for i in range(row_len):
        temp = graph[i]
        count_list = []
        for j in range(1, max(temp)+1):
            if temp.count(j) >= 1:
                count_list.append([j,temp.count(j)])
        count_list.sort(key= lambda x : (x[1],x[0]))
        new_line = []
        for l in count_list:
            new_line += l
        new_graph.append(new_line)
        max_len = max(max_len, len(new_line))

    for i in range(row_len):
        zero_len = max_len - len(new_graph[i])
        new_graph[i] = new_graph[i] + [0 for _ in range(zero_len)]
    return new_graph

def up_down_graph(graph):
    new_graph = []
    for i in range(len(graph)-1, -1 ,-1):
        new_graph.append(graph[i])
    return new_graph

n,m,k = map(int,sys.stdin.readline().rstrip().split())
graph = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(3)]

result = 0
while 1:
    row_len = len(graph)
    col_len = len(graph[0])

    if row_len >= n and col_len >= m:
        if graph[n-1][m-1] == k:
            break

    if row_len >= col_len:
        graph = change(graph)
    else:
        graph = rotation_90_right(graph)
        graph = change(graph)
        graph = rotation_90_left(graph)
        graph = up_down_graph(graph)
    result += 1
    if result == 101:
        result = -1
        break

print(result)

