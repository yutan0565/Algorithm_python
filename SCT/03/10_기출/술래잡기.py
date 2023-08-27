import sys

def make_sul_dirct_list():
    front_sul_direct_list = []
    back_sul_direct_list = []
    max_move = n*n-1
    # 술래 움직임 만들어 주기

    direct = 0
    count = 1
    while 1:
        for _ in range(2):
            for _ in range(count):
                front_sul_direct_list.append(direct)
            direct = (direct+1)%4
        count += 1
        if len(front_sul_direct_list) > max_move:
            break
    front_sul_direct_list = front_sul_direct_list[:max_move]

    for index in range(max_move-1,-1,-1):
        back_sul_direct_list.append((front_sul_direct_list[index]+2)%4)
    sul_direct_list = front_sul_direct_list + back_sul_direct_list

    while 1:
       if len(sul_direct_list) > k:
           return sul_direct_list[:k+1]
       else:
           sul_direct_list = sul_direct_list + sul_direct_list

def find_candi_theif():
    candi_move = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != []:
                if abs(sul_x-i) + abs(sul_y-j) <= 3:
                    candi_move.append([i,j])
    return candi_move


def move_theif(candi_move):
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if [i,j] in candi_move:
                if graph[i][j] != []:
                    for d in graph[i][j]:
                        new_d  = d
                        nx = i + dx[new_d]
                        ny = j + dy[new_d]
                        if not(0<=nx<n and 0<=ny<n):
                            new_d  = (new_d+2)%4
                            nx = i + dx[new_d]
                            ny = j + dy[new_d]
                        if [nx,ny] != [sul_x,sul_y]:
                            new_graph[nx][ny].append(new_d)
                        else:
                            new_graph[i][j].append(new_d)
            else:
                new_graph[i][j] = new_graph[i][j] + graph[i][j]
    return new_graph

def move_sull(sul_d):
    global sul_x, sul_y
    sul_x = sul_x + dx_sul[sul_d]
    sul_y = sul_y + dy_sul[sul_d]

def find_theif(sul_see_direct):
    see_list = []
    x,y = sul_x,sul_y
    count = 0
    # 보는 곳 체크
    for _ in range(3):
        if tree[x][y] != 1:
            see_list.append([x,y])
        x = x + dx_sul[sul_see_direct]
        y = y + dy_sul[sul_see_direct]
        if not(0<=x<n and 0<=y<n):
            break

    for x,y in see_list:
        count += len(graph[x][y])
        graph[x][y] = []
    return count

# 격자크기 / 도망자 수 / 나무의 개수 / 반복수
n,m,h,k = map(int,sys.stdin.readline().rstrip().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
tree = [[0 for _ in range(n)] for _ in range(n)]

dx_sul = [-1,0,1,0]
dy_sul = [0,1,0,-1]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
for _ in range(m):
    x,y,type = map(int,sys.stdin.readline().rstrip().split())
    # 우 좌
    if type == 1:
        graph[x-1][y-1].append(0)
    # 아 상
    elif type == 2:
        graph[x-1][y-1].append(1)

for _ in range(h):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    tree[x-1][y-1] = 1

# 술래 임직임 만들기
sul_direct_list = make_sul_dirct_list()

sul_x, sul_y = n//2,n//2
sul_see_direct = 0

total_score = 0
for turn in range(1, k+1):
    # 움직일 도둑 찾기
    candi_move = find_candi_theif()

    # 도둑 움직이기
    graph = move_theif(candi_move)

    # 술래 움직임
    sul_d = sul_direct_list[turn - 1]
    sul_see_direct = sul_direct_list[turn]
    move_sull(sul_d)

    # 도둑 찾기
    find_count = find_theif(sul_see_direct)
    total_score += find_count*turn

print(total_score)
"""
5 3 1 2
2 4 1
1 4 2
4 2 1
2 4
"""