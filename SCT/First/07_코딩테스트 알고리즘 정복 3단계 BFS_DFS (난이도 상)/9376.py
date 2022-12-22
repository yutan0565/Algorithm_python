import copy
from collections import deque
import sys

def bfs():
    q = deque()
    open_door = []
    q.append([[f_x,f_y],[s_x,s_y],open_door])

    first = 0
    second = 1
    # x, y, 연 문 개수, 사람 번호
    visited[f_x][f_y][0][first] = 1
    visited[s_x][s_y][0][second] = 1

    dx = [0,0,0,1,-1]
    dy = [0,1,-1,0,0]



    while q:
        a,b,open_d = q.popleft()
        d_count = len(open_d)
        f_a,f_b = map(int, a)
        s_a, s_b = map(int, b)
        if [f_a, f_b] == [s_a, s_b]:
            continue
        temp_graph = copy.deepcopy(graph)
        two_graph = copy.deepcopy(temp_graph)

        print(open_d)
        for i in range(h):
            for j in range(w):
                if two_graph[i][j] == '#' and [i,j] in open_d:
                    two_graph[i][j] = '.'
                if [i,j] == [f_a, f_b] or [i,j] == [s_a, s_b]:
                    two_graph[i][j] = '$'
        for g in two_graph:
            print(g)


        print()

        for i in range(h):
            for j in range(w):
                if temp_graph[i][j] == '#' and [i,j] in open_d:
                    temp_graph[i][j] = '.'

        if (f_a == 0 or f_a == h-1 or f_b == 0 or f_b == w-1) and (s_a == 0 or s_a == h-1 or s_b == 0 or s_b == w-1):
            return d_count

        next_list = []
        for i in range(5):
            f_nx = f_a + dx[i]
            f_ny = f_b + dy[i]
            for i in range(5):
                s_nx = s_a + dx[i]
                s_ny = s_b + dy[i]
                next_list.append([[f_nx,f_ny],[s_nx,s_ny]])


        for n_a,n_b in next_list:
            f_nx = n_a[0]
            f_ny = n_a[1]
            s_nx = n_b[0]
            s_ny = n_b[1]
            if 0<=f_nx<h and 0<=f_ny<w and 0<=s_nx<h and 0<=s_ny<w:
                if visited[f_nx][f_ny][d_count][first] == -1 and visited[s_nx][s_ny][d_count][second] == -1:
                    if temp_graph[f_nx][f_ny] == '*' or temp_graph[s_nx][s_ny] == '*':
                        continue
                    temp_d = copy.deepcopy(open_d)
                    if temp_graph[f_nx][f_ny] == '.':
                        visited[f_nx][f_ny][d_count][first] = 1
                    elif temp_graph[f_nx][f_ny] == '#':
                        if [f_nx,f_ny] not in open_d:
                            temp_d.append([f_nx,f_ny])
                            visited[f_nx][f_ny][d_count+ 1][first] = 1

                    if temp_graph[s_nx][s_ny] == '.':
                        visited[s_nx][s_ny][d_count][second] = 1
                    elif temp_graph[s_nx][s_ny] == '#':
                        if [s_nx,s_ny] not in open_d:
                            temp_d.append([s_nx,s_ny])
                            visited[s_nx][s_ny][d_count+ 1][second] = 1
                    q.append([[f_nx,f_ny],[s_nx,s_ny], temp_d])
                    if len(open_d) - len(temp_d) == 2:
                        visited[f_nx][f_ny][d_count + 2][first] = 1
                        visited[s_nx][s_ny][d_count + 2][second] = 1




t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    h,w = map(int, sys.stdin.readline().rstrip().split())
    graph = []
    p_list = []
    door_count = 0
    for i in range(h):
        graph.append(list(sys.stdin.readline().rstrip()))
        for j in range(w):
            if graph[i][j] == '$':
                p_list.append([i,j])
                graph[i][j] = '.'

            if graph[i][j] == '#':
                door_count += 1
    f_x = p_list[0][0]
    f_y = p_list[0][1]
    s_x = p_list[1][0]
    s_y = p_list[1][1]

    visited = [[[[-1,-1] for _ in range(door_count+1)] for _ in range(w)] for _ in range(h)]

    result = bfs()
    print(result)