import sys

C = int(sys.stdin.readline())

for i in range(C):
    score = list(map(int, sys.stdin.readline().split()))
    avg = sum(score[1:])/len(score[1:])
    count = 0
    for i in score[1:]:
        if i > avg:
            count+=1
    rate = count/score[0]*100
    print("{:.3f}%".format(rate))