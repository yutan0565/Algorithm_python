import sys

def make_load(start_row, now_col,dict_col):
    for now_row in range(start_row,n):
        next_row = now_row + 1
        # 가장 마지막 줄인 경우
        if now_row == n-1:
            dict_load[dict_col].append([now_row,now_col])
            break
        # 다음 행이 X 인 경우
        if graph[next_row][now_col] == "X":
            dict_load[dict_col].append([now_row,now_col])
            break
        # 다음 행에 아무것도 없는 경우
        if graph[next_row][now_col] == ".":
            dict_load[dict_col].append([now_row,now_col])
            continue
        # 다음 행에 돌이 있는 경우
        if graph[next_row][now_col] == "O":
            dict_load[dict_col].append([now_row, now_col])
            # 왼쪽 아래가 비어 있음
            if 0<=now_col-1:
                if graph[next_row][now_col-1] == ".":
                    if graph[now_row][now_col-1] == ".":
                        now_col = now_col-1
                        continue
            #오른쪽 아래가 비어 있음
            if now_col+1<m:
                if graph[next_row][now_col+1] == ".":
                    if graph[now_row][now_col+1] == ".":
                        now_col = now_col+1
                        continue
            break

def put_stone(throw_col):
    while 1:
        if len(dict_load[throw_col]) == 0:
            break
        x, y = dict_load[throw_col].pop()
        # 다른 돌이 들어와 있는 경우
        if graph[x][y] == "O":
            continue
        # 다른 돌이 없는 경우
        elif graph[x][y] == ".":
            # 지금 위치에서 새로운 경로 계산
            make_load(x,y,throw_col)
            x, y = dict_load[throw_col].pop()
            # 새로운 돌 올려두기
            graph[x][y] = "O"
            break


n,m = map(int,sys.stdin.readline().rstrip().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dict_load = {}

throw_count = int(sys.stdin.readline().rstrip())
for round in range(1, throw_count+1):
    throw_col = int(sys.stdin.readline().rstrip()) - 1
    # 빈칸이 아니면 패스 / X 여도 패스
    if graph[0][throw_col] != "." or graph[0][throw_col] == "X":
        continue
    # 처음 등장하는 col인 경우
    if not(dict_load.get(throw_col)):
        dict_load[throw_col] = []
        make_load(0,throw_col,throw_col)
    put_stone(throw_col)
    # print("=================")
    # print(throw_col+1)
    # for g in graph:
    #     print(g)


for i in range(n):
    for j in range(m):
        print(graph[i][j],end = "")
    print()


"""
5 4
....
....
X...
....
....
20
1
2
3
4
1
2
3
4
1
2
3
4
1
2
3
4
1
2
3
4




"""