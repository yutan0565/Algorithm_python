import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
number = list(map(int, sys.stdin.readline().rstrip().split()))
number_per = permutations(number)

result = 0
for number_list in number_per:
    sum = 0
    for j in range(len(number_list) - 1):
        sum += abs(number_list[j] - number_list[j + 1])
    result = max(result, sum)
print(result)
