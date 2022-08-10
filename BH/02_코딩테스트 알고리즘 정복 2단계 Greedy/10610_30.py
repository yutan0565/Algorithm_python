import sys

num_list = list(map(str,sys.stdin.readline().rstrip()))
num_list.sort(reverse=True)
sum = 0
for i in num_list:
    sum += int(i)

if sum % 3 != 0 or "0" not in num_list:
    print(-1)
else:
    print(''.join(num_list))

# group_list = permutations(num_list)
#
# result = -20
#
# for g in group_list:
#     if g[-1] != '0' or g[0] == '0':
#         continue
#     new_num = ""
#     for i in g:
#         new_num = new_num + i
#     new = int(new_num)
#
#     if new %30 == 0:
#         result = max(result, new)
# if result == -20:
#     print(-1)
# else:
#     print(result)