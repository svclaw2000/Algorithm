# 00:18 / 00:30
from collections import deque

N, M, K, X = map(int, input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    road[s].append(e)

min_dist = [N] * (N+1)                      # X부터 각 도시로 가는 최단거리

queue = deque()
queue.append((X, 0))
while queue:
    x, d = queue.popleft()
    if min_dist[x] > d:
        min_dist[x] = d
        for e in road[x]:
            queue.append((e, d+1))

ret = [i for i, d in enumerate(min_dist) if d==K]

if ret:
    print(*ret, sep='\n')
else:
    print(-1)