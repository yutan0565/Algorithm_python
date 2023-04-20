import sys

def check(mid):
    cost = 0
    for i in spec_list:
        if mid > i:
            cost += (mid - i) ** 2
    if cost <= b:
        return True
    else:
        return False

def bin_search(start, end):
    if start == end:
        return start
    mid = (start + end + 1) // 2
    if check(mid):
        return bin_search(mid, end)
    else:
        return bin_search(start, mid - 1)

n, b = map(int, sys.stdin.readline().split())
spec_list = list(map(int, sys.stdin.readline().split()))
spec_list.sort()
min_power = spec_list[0]
result = bin_search(min_power, 2 * 10 ** 9)
print(result)