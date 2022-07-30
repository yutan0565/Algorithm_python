import sys

n = int(sys.stdin.readline().rstrip())
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    min_value = 1e9
    j = 1
    while (j**2) <= i:
        min_value = min(min_value, dp[i - (j**2)])
        j += 1
    dp[i] = min_value + 1
print(dp[n])
