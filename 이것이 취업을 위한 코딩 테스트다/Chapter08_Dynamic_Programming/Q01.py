# 00:02 / 00:20

X = int(input())
dp = [X] * (X+1)
dp[1] = 0

for i in range(1, X):
    if i*5 <= X and dp[i*5] > dp[i] + 1: dp[i*5] = dp[i] + 1
    if i*3 <= X and dp[i*3] > dp[i] + 1: dp[i*3] = dp[i] + 1
    if i*2 <= X and dp[i*2] > dp[i] + 1: dp[i*2] = dp[i] + 1
    if i+1 <= X and dp[i+1] > dp[i] + 1: dp[i+1] = dp[i] + 1

print(dp[X])