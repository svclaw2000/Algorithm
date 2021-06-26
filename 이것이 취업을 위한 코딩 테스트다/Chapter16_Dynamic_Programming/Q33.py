N = int(input())
meeting = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)

for cur in range(N):
    days, pay = meeting[cur]
    if cur + days <= N:
        for i in range(cur+days, N+1):
            dp[i] = max(dp[i], dp[cur] + pay)

print(max(dp))