import heapq

N, M = map(int, input().split())
road = {i: [] for i in range(1, N+1)}
for _ in range(M):
    s, e = map(int, input().split())
    road[s].append(e)
    road[e].append(s)
X, K = map(int, input().split())

INF = int(1e9)

s_to_k = [INF for i in range(N+1)]
s_to_k[1] = 0

heap = []
heapq.heappush(heap, (0, 1))

while heap:
    cur_dist, cur_end = heapq.heappop(heap)

    if s_to_k[cur_end] < cur_dist:
        continue

    for new_end in road[cur_end]:
        if s_to_k[new_end] > cur_dist+1:
            s_to_k[new_end] = cur_dist + 1
            heapq.heappush(heap, (cur_dist+1, new_end))

k_to_x = [INF for i in range(N+1)]
k_to_x[K] = 0
heapq.heappush(heap, (0, K))

while heap:
    cur_dist, cur_end = heapq.heappop(heap)

    if k_to_x[cur_end] < cur_dist:
        continue

    for new_end in road[cur_end]:
        if k_to_x[new_end] > cur_dist+1:
            k_to_x[new_end] = cur_dist + 1
            heapq.heappush(heap, (cur_dist+1, new_end))

if s_to_k[K] == INF or k_to_x[X] == INF:
    print(-1)
else:
    print(s_to_k[K] + k_to_x[X])