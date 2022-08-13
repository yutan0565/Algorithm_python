import sys

n = int(sys.stdin.readline().rstrip())
w_list = []
for _ in range(n):
    w_list.append(int(sys.stdin.readline().rstrip()))

w_list.sort(reverse=True)

result = []

for i in range(n):
    result.append(w_list[i] *(i+1))
print(max(result))
