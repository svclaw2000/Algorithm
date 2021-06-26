# 00:20 / 00:30

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    line = list(map(int, input().split()))

    table = [line[i*m:(i+1)*m] for i in range(n)]

    dp = [[0] * m for _ in range(n+2)]
    for r in range(n):
        dp[r+1][0] = table[r][0]

    for c in range(1, m):
        for r in range(n):
            dp[r+1][c] = max(dp[r][c-1] + table[r][c], dp[r+1][c-1] + table[r][c], dp[r+2][c-1] + table[r][c])

    print(max([dp[r+1][-1] for r in range(n)]))