import sys

N = int(sys.stdin.readline())

score = list(map(int, sys.stdin.readline().split()))

new_score = [ i/max(score)*100 for i in score]


print(sum(new_score)/len(new_score))

