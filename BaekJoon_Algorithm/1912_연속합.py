import sys

n = int(sys.stdin.readline().rstrip())
number_list = list(map(int, sys.stdin.readline().rstrip().split()))

INF  = 1e9
dp = [-INF] * n


dp[0] = number_list[0]

for i in range(1, n):
    dp[i] = number_list[i]
    if dp[i] + dp[i-1] > dp[i]:
        dp[i] = dp[i] + dp[i-1]

print(max(dp))


