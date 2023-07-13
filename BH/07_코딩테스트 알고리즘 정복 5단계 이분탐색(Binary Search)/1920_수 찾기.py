import sys

def bin_search(num):
    left_index, right_index = 0, n-1
    while 1:
        if left_index > right_index: break
        mid_index = (left_index + right_index) // 2
        mid_value = n_list[mid_index]
        if mid_value == num:
            return 1
        if mid_value > num:
            right_index = mid_index-1
        else:
            left_index = mid_index + 1
    return 0

n = int(sys.stdin.readline().rstrip())
n_list = list(map(int,sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
m_list = list(map(int,sys.stdin.readline().rstrip().split()))

n_list.sort()
for num in m_list:
    if bin_search(num):
        print(1)
    else:
        print(0)