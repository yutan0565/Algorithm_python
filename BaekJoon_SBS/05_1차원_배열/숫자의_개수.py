import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
"""
number = str(a*b*c)
for i in range(10):
    count = 0
    for j in number:
        if str(i) in j:
            count+=1
    print(count)
"""
number_list = list(str(a*b*c))

answer = [0 for i in range(10)]

for num in number_list:
    answer[int(num)] += 1

for ans in answer:
    print(ans)