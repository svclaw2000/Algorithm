# 00:06 / 00:40

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

N, M = map(int, input().split())
parent = list(range(N+1))
roads = [list(map(int, input().split())) for _ in range(M)]
roads.sort(key=lambda x: x[2])

min_cost = 0
total_cost = 0
for a, b, c in roads:
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[a] = parent[b] = min(a, b)
        min_cost += c
    total_cost += c

print(total_cost - min_cost)