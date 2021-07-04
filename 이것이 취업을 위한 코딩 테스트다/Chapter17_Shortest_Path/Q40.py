# 00:07 / 00:40
import heapq

INF = int(1e9)
N, M = map(int, input().split())
maps = {i:[] for i in range(1, N+1)}
for _ in range(M):
    A, B = map(int, input().split())
    maps[A].append(B)
    maps[B].append(A)

min_dist = [INF]*(N+1)
min_dist[1] = 0

heap = []
heapq.heappush(heap, (0, 1))

while heap:
    cd, cx = heapq.heappop(heap)
    if min_dist[cx] < cd:
        continue

    for nx in maps[cx]:
        if cd + 1 < min_dist[nx]:
            min_dist[nx] = cd + 1
            heapq.heappush(heap, (cd+1, nx))

max_dist = max(min_dist[1:])
print(min_dist.index(max_dist), max_dist, min_dist.count(max_dist))