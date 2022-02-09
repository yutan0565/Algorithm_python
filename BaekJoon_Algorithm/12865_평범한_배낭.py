import sys

"""
물건 N개
\무게 w   가치 v

k 는 무게 제한
"""

N, K = map(int,sys.stdin.readline().rstrip().split())

dp = [ [0]*(K+1) for _ in range(N+1) ]

for i in range(1, N+1):
    w, v = map(int, sys.stdin.readline().rstrip().split())

    for j in range(1, K+1):
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(  dp[i-1][j-w] + v ,dp[i-1][j]  )

print(dp[-1][-1])


