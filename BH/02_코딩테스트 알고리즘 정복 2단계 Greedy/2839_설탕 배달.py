import sys

n = int(sys.stdin.readline().rstrip())

dp = [1000000] * (5000 + 1)
dp[3] = 1
dp[5] = 1
for i in range(6, n+1):
    dp[i] = min(dp[i - 3], dp[i - 5]) +1

if dp[n] >= 1000000:
    print(-1)
else:
    print(dp[n])



"""
import sys

n = int(sys.stdin.readline().rstrip())
if n <= 5:
    if n == 3 or n == 5:
        print(1)
    else:
        print(-1)
else:
    dp = [-1] * (n + 1)
    dp[3] = 1
    dp[5] = 1
    for i in range(6, n+1):
        if dp[i-3] != -1 and dp[i-5] != -1:
            dp[i] = min(dp[i-3] +1 , dp[i - 5] + 1)
        elif dp[i-3] != -1 :
            dp[i] = dp[i-3]+1
        elif dp[i-5] != -1 :
            dp[i] = dp[i - 5] + 1
    print(dp[n])
"""