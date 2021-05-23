from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

ds = ((-1, 0), (0, 1), (1, 0), (0, -1))

def dfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in ds:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < N or not 0 <= ny < M or maze[nx][ny] == 0: # 범위 벗어나거나 괴물이면 무시
                continue
            if maze[nx][ny] == 1:                                       # 최초 방문(거리 1) 시 최단거리 저장 및 다른 곳 탐색
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[-1][-1]

print(dfs(0, 0))