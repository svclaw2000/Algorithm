# 00:33 / 00:40 Failed
from collections import deque

N, L, R = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]
ret = 0

ds = ((-1, 0), (0, 1), (1, 0), (0, -1))

while True:
    group = [[0 for cell in row] for row in nations]
    queue = deque()
    cur_i = 0
    for x, row in enumerate(nations):
        for y, cell in enumerate(row):
            if group[x][y] == 0:
                cur_i += 1
                group[x][y] = cur_i
                queue.append((x, y))
            while queue:
                x, y = queue.popleft()
                for dx, dy in ds:
                    nx = x + dx
                    ny = y + dy
                    if not (0 <= nx < N and 0 <= ny < N):
                        continue
                    if group[nx][ny] == 0 and L <= abs(nations[nx][ny] - nations[x][y]) <= R:
                        group[nx][ny] = cur_i
                        queue.append((nx, ny))
    if cur_i == N*N:
        break
    for i in range(1, cur_i+1):
        pos = [(x, y) for x in range(N) for y in range(N) if group[x][y] == i]
        n = sum([nations[x][y] for x, y in pos]) // len(pos)
        for x, y in pos:
            nations[x][y] = n
    ret += 1

print(ret)
