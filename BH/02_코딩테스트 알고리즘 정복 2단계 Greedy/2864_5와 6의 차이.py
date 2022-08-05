import sys

a,b = map(int, sys.stdin.readline().rstrip().split())

a_list = list(map(int,str(a)))
b_list = list(map(int,str(b)))

a_min = []
a_max = []

b_min = []
b_max = []

for i in range(len(a_list)):
    if a_list[i] == 5 or a_list[i] == 6:
        a_min.append(5)
        a_max.append(6)
    else:
        a_min.append(a_list[i])
        a_max.append(a_list[i])

for i in range(len(b_list)):
    if b_list[i] == 5 or b_list[i] == 6:
        b_min.append(5)
        b_max.append(6)
    else:
        b_min.append(b_list[i])
        b_max.append(b_list[i])


a_min_i = 0
a_max_i = 0

b_min_i = 0
b_max_i = 0

for i in range(len(a_list)):
    a_min_i += a_min[i] * (10**(len(a_list)-i-1))
    a_max_i += a_max[i] * (10**(len(a_list)-i-1))

for i in range(len(b_list)):
    b_min_i += b_min[i] * (10**(len(b_list)-i-1))
    b_max_i += b_max[i] * (10**(len(b_list)-i-1))

print("{} {}".format(a_min_i+b_min_i, a_max_i+b_max_i))