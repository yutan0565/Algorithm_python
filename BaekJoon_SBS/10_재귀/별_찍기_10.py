import sys

## 다시 확인
def draw_star(n):
    global temp

    if n == 3:
        temp[0][:3] = temp[2][:3] = [1] * 3
        temp[1][:3] = [1, 0, 1]

        return

    a = n // 3
    draw_star(n // 3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                temp[a * i + k][a * j:a * (j + 1)] = temp[k][:a]


n = int(sys.stdin.readline())
temp = [[0 for i in range(n)] for i in range(n)]

draw_star(n)
for i in temp:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()
