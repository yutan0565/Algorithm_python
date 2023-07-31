import sys

def down_who():
    for i in range(n):
        for j in range(n):
            if graph_who[i][j] != [-1,-1]:
                number = graph_who[i][j][0]
                count = graph_who[i][j][1]
                count -= 1
                if count != -1:
                    graph_who[i][j] = [number, count]
                else:
                    graph_who[i][j] = [-1,-1]


def move_player():
    new_graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                num = graph[i][j]
                now_direct = dict_direct[num]
                nx = i + dx[now_direct]
                ny = j + dy[now_direct]
                # 다음 칸이 그냥 빈칸이면
                if new_graph[nx][ny] == 0:
                    new_graph[nx][ny] = num
                    graph_who[nx][ny] = [num, k]
                # 다른 사람이 있으면
                else:
                    # 기존에 있던거
                    other_num = new_graph[nx][ny]
                    # 새로운거 번호가 더 작으면
                    if other_num > num:
                        new_graph[nx][ny] = num
                        graph_who[nx][ny] = [num, k]
                        # 기존에 있던 사람은 죽은
                        list_arrive[other_num] = 0
                    # 기존꺼가 더 작으면
                    elif other_num < num:
                        # 새로운 사람은 죽음
                        list_arrive[num] = 0
    return new_graph

def make_new_direct():
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                num = graph[i][j]
                now_direct = dict_direct[num]
                candi_direct = dict_direct_candi[num][now_direct]

                # 빈칸 찾기
                stop_flag = 0
                for new_direct in candi_direct:
                    nx = i + dx[new_direct]
                    ny = j + dy[new_direct]
                    if 0<=nx<n and 0<=ny<n:
                        if graph_who[nx][ny] == [-1,-1]:
                            dict_direct[num] = new_direct
                            stop_flag = 1
                            break
                if stop_flag == 1:
                    continue
                # 내가 독점한 칸 찾기
                for new_direct in candi_direct:
                    nx = i + dx[new_direct]
                    ny = j + dy[new_direct]
                    if 0<=nx<n and 0<=ny<n:
                        if graph_who[nx][ny][0] == num:
                            dict_direct[num] = new_direct
                            break

n,m,k = map(int,sys.stdin.readline().rstrip().split())
dict_direct = {}
dict_direct_candi = {}
list_arrive = [0]
graph = [[0 for _ in range(n)] for _ in range(n)]
graph_who = [[[-1,-1] for _ in range(n)] for _ in range(n)]

for i in range(n):
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if temp[j] != 0:
            number = temp[j]
            list_arrive.append(1)
            # 첫 시작칸도 독점 계약
            graph[i][j] = number
            graph_who[i][j] = [number, k]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

start_direct = list(map(int,sys.stdin.readline().rstrip().split()))
for num in range(1, len(start_direct)+1):
    d = start_direct[num-1] - 1
    dict_direct[num] = d

# 후보 방향 선정
for num in range(1, len(start_direct)+1):
    dict_direct_candi[num] = []
    for _ in range(4):
        a,b,c,d = list(map(int,sys.stdin.readline().rstrip().split()))
        dict_direct_candi[num].append([a-1,b-1,c-1,d-1])


result = 1
while 1:
    # 새로운 턴이니까 / 소유지 내리기
    down_who()
    # 방향 확정 짓기
    make_new_direct()
    # 한칸씩 이동 / 각각의 땅을 계약
    graph = move_player()

    # 1번만 남으면 끝
    if sum(list_arrive) == 1 and list_arrive[1] == 1:
        break
    result += 1
    if result == 1001:
        result = -1
        break
print(result)