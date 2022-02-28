import sys
import math
from itertools import combinations

n,m = map(int, sys.stdin.readline().rstrip().split())
card = list(map(int, sys.stdin.readline().rstrip().split()))
card_set = combinations(card, 3)

max = 2e10
result = 0

for set in card_set:
    set_sum = sum(set)
    temp = m - set_sum
    if temp < max and temp>=0:
        max = temp
        result = set_sum
print(result)