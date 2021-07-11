# 00:10 / 00:50

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

N, M = map(int, input().split())
parent = [0] * (N+1)
for i in range(1, N+1):
    roads = [j+1 for j, r in enumerate(list(map(int, input().split()))) if r == 1]
    for road in roads:
        a = find_parent(parent, i)
        b = find_parent(parent, road)
        if a != b:
            parent[a] = parent[b] = min(a, b)
schedule = list(map(int, input().split()))

last_parent = find_parent(parent, schedule[0])
for s in schedule:
    if last_parent != find_parent(parent, s):
        print('NO')
else:
    print('YES')