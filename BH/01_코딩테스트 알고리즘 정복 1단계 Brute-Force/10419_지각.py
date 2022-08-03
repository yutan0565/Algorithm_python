import sys

t = int(sys.stdin.readline().rstrip())
late_list = []
for _ in range(t):
    late_list.append(int(sys.stdin.readline().rstrip()))


result = []
for l in late_list:
    temp_max = -float('inf')
    for i in range((l+1)//3+1):
        if i + i**2 <=l:
            temp_max = max(i, temp_max)
    result.append(temp_max)

for t in result:
    print(t)