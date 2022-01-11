import sys

N = int(sys.stdin.readline())

number_list = [i for i in range(1,N+1)]
count = 0

for number in number_list:
    if len(number_list) < 100:
        count = len(number_list)
    else:
        if int(number) < 100:
            count += 1
        else:
            temp = list(map(int, str(number)))
            temp_2 = []
            temp_2.append(temp[1]- temp[0])
            temp_2.append(temp[2] - temp[1])
            if temp_2[0] == temp_2[1]:
                count += 1

print(count)

