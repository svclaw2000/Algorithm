# 00:20 / 00:40
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
table = [input().split() for _ in range(N)]
empty = []
init_virus = []
for i, row in enumerate(table):
    for j, cell in enumerate(row):
        if cell == '2':
            init_virus.append((i, j))
        elif cell == '0':
            empty.append((i, j))
cases = combinations(empty, 3)

ret = 0
for case in cases:
    visited = [[True if cell == '1' else False for cell in row] for row in table]
    for x, y in case:
        visited[x][y] = True
    virus = deque(init_virus)
    while virus:
        x, y = virus.popleft()
        if not (0 <= x < N and 0 <= y < M):
            continue
        if visited[x][y] or table[x][y] == '1' or (x, y) in case:
            continue
        visited[x][y] = True
        virus.append((x-1, y))
        virus.append((x+1, y))
        virus.append((x, y-1))
        virus.append((x, y+1))
    result = sum([1 for i in range(N) for j in range(M) if not visited[i][j]])
    if result > ret:
        ret = result
print(ret)