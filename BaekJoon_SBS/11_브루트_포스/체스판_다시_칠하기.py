import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
board = [ list(sys.stdin.readline().rstrip()) for _ in range(n) ]

min_list = []
for i in range(n-7):
    for j in range(m-7):
        count_1 = 0
        count_2 = 0
        for k in range(i, i+8):
            for h in range(j, j+8):
                if (k + h) % 2 == 0:
                    if board[k][h] != "W":
                        count_1 += 1
                    if board[k][h] != "B":
                        count_2 += 1
                else:
                    if board[k][h] != "B":
                        count_1 += 1
                    if board[k][h] != "W":
                        count_2 += 1

        min_list.append(count_1)
        min_list.append(count_2)


print(min(min_list))