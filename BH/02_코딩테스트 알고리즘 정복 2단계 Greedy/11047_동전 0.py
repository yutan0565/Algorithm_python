import sys

n,k = map(int, sys.stdin.readline().rstrip().split())
mon_list = [ int(sys.stdin.readline().rstrip()) for _ in range(n)]
mon_list.sort(reverse=True)

count = 0
for i in range(n):
    if k // mon_list[i] >= 1:
        count += k // mon_list[i]
        k = k%mon_list[i]

print(count)
