# 00:10

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

dp = [10001] * (M+1)
dp[0] = 0

for m in range(M+1):
    for n in arr:
        if m+n <= M and dp[m+n] > dp[m] + 1: dp[m+n] = dp[m] + 1

print(dp[-1] if dp[-1] < 10001 else -1)