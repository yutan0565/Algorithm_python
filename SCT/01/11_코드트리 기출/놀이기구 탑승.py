import sys

def check_friend_empty():
    max_count = -1
    max_empty = -1
    candi_list = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == -1:
                count = 0
                empty = 0
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0<=x<n and 0<=y<n:
                        if graph[x][y] in friends:
                            count += 1
                        elif graph[x][y] == -1:
                            empty += 1
                if count > max_count:
                    max_count = count
                    max_empty = empty
                    candi_list = [[i,j]]
                elif count == max_count:
                    if empty > max_empty:
                        max_count = count
                        max_empty = empty
                        candi_list = [[i, j]]
                    elif empty == max_empty:
                        candi_list.append([i,j])
    return candi_list

def cal_score():
    score = 0
    for i in range(n):
        for j in range(n):
            temp_id = graph[i][j]
            count = 0

            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < n and 0 <= y < n:
                    if graph[x][y] in dict_info[temp_id]:
                        count += 1

            if count == 0:
                continue
            else:
                score = score + 10**(count-1)
    return score

def show_graph():
    for g in graph:
        print(g)

n = int(sys.stdin.readline())
graph = [[-1 for _ in range(n)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
dict_info = {}

for id in range(1, n*n+1):
    info = list(map(int,sys.stdin.readline().rstrip().split()))
    id = info[0]
    friends = info[1:]
    dict_info[id] = friends
    candi_list = check_friend_empty()
    candi_list.sort(key = lambda x: (x[0],x[1]))
    a,b = candi_list[0]
    graph[a][b] = id
result = cal_score()
print(result)