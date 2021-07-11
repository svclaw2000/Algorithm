# 00:18 / 00:40

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

N, M = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]
roads.sort(key=lambda x: x[2])
parent = [i for i in range(N+1)]

total_cost = []
for a, b, c in roads:
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[a] = parent[b] = min(a, b)
        total_cost.append(c)

print(sum(total_cost[:-1]))