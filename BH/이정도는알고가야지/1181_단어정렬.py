import sys

n = int(sys.stdin.readline().rstrip())
w_list = [sys.stdin.readline().rstrip() for _ in range(n)]
w_list = list(set(w_list))

w_list.sort()
w_list.sort(key = lambda x : len(x))

for w in w_list:
    print(w)
