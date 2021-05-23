from collections import deque

N, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
virus = []

for i, row in enumerate(table):
    for j, cell in enumerate(row):
        if cell > 0:
            virus.append((cell, 0, i, j))       # (종류, 현재 시간, x, y)

virus.sort()                                    # 종류 순으로 정렬
virus = deque(virus)

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while virus:                                    # virus가 비면 스톱
    v, s, i, j = virus.popleft()
    if s == S:                                  # 시간 되면 스톱
        break
    for dx, dy in ds:
        nx, ny = i + dx, j + dy
        if 0 <= nx < N and 0 <= ny < N:
            if table[nx][ny] == 0:              # 해당 위치가 비어있으면
                table[nx][ny] = v               # 바이러스 채우고
                virus.append((v, s+1, nx, ny))  # 큐에 집어넣음
print(table[X-1][Y-1])