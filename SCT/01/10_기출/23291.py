import copy
import sys

def add_fish():
    min_value  = 10001
    for i in range(n):
        if graph[-1][i] <= min_value:
            min_value = graph[-1][i]
    for i in range(n):
        if graph[-1][i] == min_value:
            graph[-1][i] += 1

def rotaion_block(block):
    w = len(block[0])
    h = len(block)
    new_block = [[0 for _ in range(h)] for _ in range(w)]
    for i in range(h):
        for j in range(w):
            new_block[j][h-i-1] = block[i][j]
    return new_block

def move_box_01():
    round = 1
    now_c = 0
    while 1:
        now_c += (round// 2)
        now_w = (round+1) // 2
        now_h = (round+2) // 2
        next_c = now_c + now_w
        next_h = (round+2+1) // 2
        if next_c + now_h > n:
            break

        now_block = []
        now_block_row = graph[n-now_h:n]
        for b in now_block_row:
            now_block.append(b[now_c:now_c+now_w])
        ro_block = rotaion_block(now_block)
        for i in range(n-now_h,n):
            for j in range(now_c,now_c+now_w):
                graph[i][j] = 0

        for i in range(len(ro_block)):
            for j in range(len(ro_block[0])):
                graph[n-next_h+i][next_c+j] = ro_block[i][j]
        round += 1

def move_fish():
    temp_graph = copy.deepcopy(graph)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] != 0 :
                            cha = abs(graph[i][j] - graph[nx][ny])//5
                            if cha > 0:
                                if graph[i][j] > graph[nx][ny]:
                                    temp_graph[i][j] -= cha
                                    temp_graph[nx][ny] += cha
    return temp_graph

def sorting_box():
    temp_graph = copy.deepcopy(reset_graph)
    fish_line = []
    for i in range(n):
        for j in range(n-1, -1, -1):
            if graph[j][i] != 0:
                fish_line.append(graph[j][i])

    temp_graph = temp_graph[1:] + [fish_line]
    return temp_graph

n,k = map(int, sys.stdin.readline().rstrip().split())
reset_graph = [[0 for _ in range(n)] for _ in range(n)]
input_fish = list(map(int, sys.stdin.readline().rstrip().split()))

graph = (copy.deepcopy(reset_graph)+[input_fish])[1:]

def move_box_02():
    for round in range(1,3):
        now_w = n//(round*2)
        now_h = 2**(round-1)
        if round == 1:
            now_c = 0
            next_c = n//2
        else:
            now_c = n//2
            next_c = n//2 + n//4
        next_h =  2**(round)

        now_block = []
        now_block_row = graph[n-now_h:n]
        for b in now_block_row:
            now_block.append(b[now_c:now_c+now_w])
        ro_block =  rotaion_block(rotaion_block(now_block))
        for i in range(n-now_h,n):
            for j in range(now_c,now_c+now_w):
                graph[i][j] = 0

        for i in range(len(ro_block)):
            for j in range(len(ro_block[0])):
                graph[n-next_h+i][next_c+j] = ro_block[i][j]
result = 0
while 1:
    last_line = graph[-1]
    if max(last_line) - min(last_line) <= k:
        break
    add_fish()
    move_box_01()
    graph = move_fish()
    graph = sorting_box()

    move_box_02()
    graph = move_fish()
    graph = sorting_box()

    result += 1
print(result)
"""
- 물고기가 가장 적은 어항에 1마리씩 추가 (같으면 중복 추가)

반복 ( 그 위에 얹지 못할때 까지)
    - (처음에는 그냥 1개 짜리 바로 오른쪽에 올리기)
    - 2개 이상 쌓인 어항을 오른쪽으로 돌림 (90 도)
    - 돌린 것을 오른쪽에 올림

물고기 이동
    - 어항간의 물고기 차이를 구하고  5로 나눈 몪이 d
    - d가 0보다 크면,  많은쪽에서 d 마리를 적은쪽으로 보냄 ( 모든 칸에서 동시 발생)

- 일렬
    - 맨 왼쪽 / 맨 아래   있는 것부터 순서대로 정렬하기


2번 반복
        - n//2 개를 선택
        - 오른쪽으로 180도 회전
        - 오른 쪽 위에 올려둠

물고기 이동 수행

- 일렬

종료 조건 =  물고기가 가장 많은곳 - 적은곳 <= k

"""