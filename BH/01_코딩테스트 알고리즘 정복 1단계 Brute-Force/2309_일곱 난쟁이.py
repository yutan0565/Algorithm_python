import sys
from itertools import combinations


h_list = []
for _ in range(9):
    h_list.append(int(sys.stdin.readline().rstrip()))
total = sum(h_list)


not_group = combinations(range(9), 2)

for g in not_group:
    new_not = [ h_list[i] for i in range(9) if i in g ]
    if total - sum(new_not) == 100:
        result = [ h_list[i] for i in range(9) if i not in g ]
        break

result.sort()

for r in result:
    print(r)