import sys

n = int(sys.stdin.readline().rstrip())
p_list = [ list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

p_list.sort(key = lambda x : (x[0], x[1]))
for p in p_list:
    print(p[0],p[1])
