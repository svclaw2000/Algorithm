# 00:04 / 00:40

N, M = map(int, input().split())
maps = [[0]*N for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    maps[A-1][B-1] = -1
    maps[B-1][A-1] = 1

for k in range(N):
    for a in range(N):
        for b in range(N):
            if maps[a][k] == maps[k][b] != 0:
                maps[a][b] = maps[a][k]

print(sum([1 for row in maps if row.count(0) == 1]))