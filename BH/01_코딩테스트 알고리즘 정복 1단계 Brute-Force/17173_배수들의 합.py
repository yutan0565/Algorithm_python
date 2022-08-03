import sys


n,m = map(int,sys.stdin.readline().rstrip().split())
k_list = list(map(int,sys.stdin.readline().rstrip().split()))

result = []

for i in range(1, n+1):
    for k in k_list:
        if i%k == 0:
            result.append(i)
            break

print(sum(result))