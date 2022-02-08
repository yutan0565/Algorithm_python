import sys

N = int(sys.stdin.readline().rstrip())
c = [ list(map(int, sys.stdin.readline().rstrip().split()))  for _ in range(N)]

#INF = int(1e9)

dp = [0]  * N

for i in range(N):   # 현재 날짜
    if i + c[i][0]  <= N:
        dp[i] = c[i][1]
        for j in range(i):
            if j + c[j][0] -1 < i:
                dp[i] = max( dp[i] , c[i][1] + dp[j] )

print(max(dp))


