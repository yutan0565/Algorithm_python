import sys

n = int(sys.stdin.readline())

number_list = list(map(int, sys.stdin.readline().split()))

count = 0

for number in number_list:
    if number == 1:
        continue

    flag = True
    for i in range(2, number):
        if number % i == 0:
            flag = False
            break
    if flag :
        count += 1
print(count)