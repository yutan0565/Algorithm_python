import sys

a,b,c,n = map(int, sys.stdin.readline().rstrip().split())

dp = [0]*(301)
temp = [a,b,c]

for i in range(a, n+1):
    if i in temp:
        dp[i] = 1
        continue
    for j in temp:
        if i >= j and dp[i-j] == 1:
            dp[i] = 1
print(dp[n])


