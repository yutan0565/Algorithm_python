import sys

N = int(sys.stdin.readline().strip())
X = list(map(int, sys.stdin.readline().strip().split()))

sort_X = sorted(X)

print(sort_X)

# 내꺼
count = 0
while(len(sort_X) != 0):
    if max(sort_X) > len(sort_X):
        break
    for i in range(max(sort_X)):
        sort_X.pop()
    count += 1
print(count)

#정답

result = 0 # 총 그룹의 수
count = 0 #현재 그룸에 포함된 모험가의 수

for i in sort_X: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이면, 그룹 결성
        result += 1
        count = 0
print(result)





