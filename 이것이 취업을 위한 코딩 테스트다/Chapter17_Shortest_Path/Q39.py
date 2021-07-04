# 00:14 / 00:40
import heapq

INF = int(1e9)
ds = ((-1, 0), (0, 1), (1, 0), (0, -1))

T = int(input())
for _ in range(T):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    min_dist = [[INF]*N for _ in range(N)]
    min_dist[0][0] = maps[0][0]
    heap = []
    heapq.heappush(heap, (maps[0][0], 0, 0))

    while heap:
        cur_dist, cur_x, cur_y = heapq.heappop(heap)
        if min_dist[cur_x][cur_y] < cur_dist:
            continue

        for dx, dy in ds:
            nx, ny = cur_x + dx, cur_y + dy
            if 0 <= nx < N and 0 <= ny < N:
                nd = maps[nx][ny]
                if cur_dist + nd < min_dist[nx][ny]:
                    min_dist[nx][ny] = cur_dist + nd
                    heapq.heappush(heap, (cur_dist + nd, nx, ny))

    print(min_dist[-1][-1])