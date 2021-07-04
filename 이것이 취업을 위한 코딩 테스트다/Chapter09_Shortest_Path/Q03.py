import heapq

N, M, C = map(int, input().split())
road = {i:{} for i in range(1, N+1)}
for _ in range(M):
    X, Y, Z = map(int, input().split())
    road[X][Y] = Z

INF = int(1e9)

heap = []
heapq.heappush(heap, (0, C))

min_dist = [INF for _ in range(N+1)]
min_dist[C] = 0

while heap:
    cur_dist, cur_end = heapq.heappop(heap)
    if min_dist[cur_end] > cur_dist:
        continue

    for new_end in road[cur_end]:
        new_dist = road[cur_end][new_end]
        if min_dist[new_end] > cur_dist + new_dist:
            min_dist[new_end] = cur_dist + new_dist
            heapq.heappush(heap, (cur_dist+new_dist, new_end))

passed = [i for i in min_dist if i != INF]
print(len(passed)-1, max(passed))