import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    dp = [[0,0] for _ in range(n+1)]

    if n == 0:
        print(1, 0)
    if n == 1:
        print(0, 1)

    if n >= 2:
        dp[0] = [1, 0]
        dp[1] = [0, 1]
        for i in range(2, n+1):
            dp[i][0] = dp[i-1][0]  + dp[i-2][0]
            dp[i][1] = dp[i-1][1]  + dp[i-2][1]
        print(dp[n][0], dp[n][1])

# 기존 방식
# def fibo(n):
#     global count_0
#     global count_1
#     if n == 0:
#         count_0 += 1
#         return 0
#     if n == 1:
#         count_1 += 1
#         return 1
#     return fibo(n-1) + fibo(n-2)
#
# t = int(sys.stdin.readline().rstrip())
# for _ in range(t):
#     n = int(sys.stdin.readline().rstrip())
#     global count_0
#     global count_1
#     count_0 = 0
#     count_1 = 0
#     fibo(n)
#     print(count_0, count_1)
zero = [1, 0, 1]
one = [0, 1, 1]


def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print('{} {}'.format(zero[num], one[num]))


T = int(input())

for _ in range(T):
    fibonacci(int(input()))