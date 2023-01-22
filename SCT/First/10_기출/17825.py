import copy

graph = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]
score_list = [0, 2, 4, 6, 8, 10,
         12, 14, 16, 18, 20,
         22, 24, 26, 28, 30,
         32, 34, 36, 38, 40,
         13, 16, 19, 25, 22,
         24, 28, 27, 26, 30,
         35, 0]

dice_list = list(map(int, input().split()))
result = 0

def dfs(turn, score, pos_list):
    global result
    if turn >= 10:
        result = max(result, score)
        return
    for i in range(4):
        x = pos_list[i]  # 현재 위치
        if len(graph[x]) == 2: # 갈 곳이 두개
            x = graph[x][1]      # 파란 방향 우선
        else:
            x = graph[x][0]  # 일반 적인 전진
        # 나온 점수 만큼 이동 (계쏙 타고 들어감 , 처음 이동 뺴고)
        for j in range(1, dice_list[turn]):
            x = graph[x][0]
        if x == 32 or (x < 32 and x not in pos_list):   # 도착점 or 말이 있는곳이 아님
            temp_pos_list = copy.deepcopy(pos_list)
            temp_pos_list[i] = x
            dfs(turn + 1, score+score_list[x],temp_pos_list)

dfs(0, 0, [0,0,0,0])
print(result)
