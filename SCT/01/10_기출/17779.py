import sys

def make_area_mask(x,y):
    mask = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    for d1 in range(0, d_1 + 1):
        for d2 in range(0, d_2 + 1):
            mask[x + d1][y - d1] = 5
            mask[x + d2][y + d2] = 5
            mask[x + d_1 + d2][y - d_1 + d2] = 5
            mask[x + d_2 + d1][y + d_2 - d1] = 5
    for i in range(1,n+1):
        if mask[i][1:].count(5) == 1 or mask[i][1:].count(5) == 0:
            continue
        cont_flag = 0
        for j in range(1, n+1):
            if mask[i][j] == 5 and cont_flag == 0:
                cont_flag = 1
            elif mask[i][j] == 5 and cont_flag == 1:
                cont_flag = 0
                break
            elif cont_flag == 1:
                mask[i][j] = 5

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if mask[i][j] != 5:
                if 1 <= i < x+d_1 and 1 <= j <= y:
                    mask[i][j] = 1
                elif 1 <= i <= x+d_2 and y < j <= n:
                    mask[i][j] = 2
                elif x+d_1 <= i <= n and 1 <= j < y-d_1+d_2:
                    mask[i][j] = 3
                elif x+d_2 < i <= n and y-d_1+d_2 <= j <=n:
                    mask[i][j] = 4

    new_mask = []
    for i in range(1, n+1):
        new_mask.append(mask[i][1:])
    return new_mask

def cal_area_score(mask):
    score_list = [0,0,0,0,0]
    for i in range(n):
        for j in range(n):
            score_list[mask[i][j]-1] += graph_popul[i][j]
    return score_list

n = int(sys.stdin.readline().rstrip())
graph_popul = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

min_result = float("inf")
for i in range(1,n+1):
    for j in range(1, n+1):
        for d_1 in range(1, n):
            for d_2 in range(1, n):
                if  1 <= i < i+d_1+d_2 and  i+d_1+d_2 <= n:
                    if 1<= j-d_1 < j  and j < j+d_2  <= n:
                        # 구역 나눈 마스크 만들기
                        area_mask = make_area_mask(i,j)
                        # 구역 별로, 점수 총합 리스트 만들기
                        score_list = cal_area_score(area_mask)
                        # 모든 구역이 포함되는 경우에만
                        if 0 not in score_list:
                            # 최대 / 최소의 차 구하기
                            temp = max(score_list) - min(score_list)
                            # 차이 최소값 업데이트
                            min_result = min(min_result, temp)

print(min_result)