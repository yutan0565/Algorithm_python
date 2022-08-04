import sys

n,k = map(int,sys.stdin.readline().rstrip().split())
n_list = list(map(int,sys.stdin.readline().rstrip().split()))

gap_list = []
for i in range(n-1):
    gap_list.append(n_list[i+1] - n_list[i])
gap_list.sort()


result = sum(gap_list[:n-k])
print(result)
