import sys

s = int(sys.stdin.readline().rstrip())

i = 1
sum = 0
count = 0

while True:
    sum += i
    i += 1
    if sum > s:
        break
    count +=1
print(count)

