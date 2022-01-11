import sys

N = int(sys.stdin.readline())

for i in range(N):
    score = 0
    temp = list(sys.stdin.readline())
    temp_score = 1
    for ans in temp:
        if ans == 'O':
            score += temp_score
            temp_score += 1
        else:
            temp_score = 1
    print(score)






