import sys

def min_cost(n, dp):
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]
    result = min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])
    return result

n = int(sys.stdin.readline().rstrip())
dp = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n) ]

print(min_cost(n,dp))