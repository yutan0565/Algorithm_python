import sys


temp = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(3)]

x = []
y = []

for i in temp:
    x.append(i[0])
    y.append(i[1])

result_x = 0
result_y = 0

if x[0] == x[1]:
    result_x = x[2]
elif x[0] == x[2]:
    result_x = x[1]
else:
    result_x = x[0]

if y[0] == y[1]:
    result_y = y[2]
elif y[0] == y[2]:
    result_y = y[1]
else:
    result_y = y[0]

print(result_x, result_y)