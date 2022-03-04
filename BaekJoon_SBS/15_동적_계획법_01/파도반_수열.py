import sys

def pado(n):
    dp = [0] * (101)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]

    return dp[n]


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(pado(n))