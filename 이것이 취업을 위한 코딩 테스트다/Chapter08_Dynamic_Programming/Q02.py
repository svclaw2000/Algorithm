# 00:10 / 00:30

N = int(input())
house = list(map(int, input().split()))

dp = [0] * N
dp[0] = house[0]
dp[1] = max(house[0], house[1])

for i in range(2, N):
    dp[i] = max(dp[i-2] + house[i], dp[i-1])

print(dp[-1])