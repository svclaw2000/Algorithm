# 00:20 / 00:40

INF = int(1e9)
n = int(input())
m = int(input())

maps = [[INF]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    maps[a-1][b-1] = min(maps[a-1][b-1], c)

for i in range(n):
    maps[i][i] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            maps[a][b] = min(maps[a][b], maps[a][k] + maps[k][b])

print(*[' '.join([str(cell) if cell != INF else '0' for cell in row]) for row in maps], sep='\n')