import sys

n = int(sys.stdin.readline().rstrip())
info = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n) ]
result = []

for i in range(n):
    count = 1
    for j in range(n):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            count += 1
    result.append(count)

for i in result:
    print(i,end=" ")


