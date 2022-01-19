import sys

N = int(sys.stdin.readline().rstrip())

count = 0


for i in range(N):
    s_list = list(sys.stdin.readline().rstrip())

    temp_list = []
    flag =""
    flag_2 = True
    for s in s_list:

        if s not in temp_list:
            temp_list.append(s)
            flag = s
        else:
            if s == flag:
                pass
            else:
                flag_2 = False
    if flag_2 :
        count += 1

print(count)





