# 00:03 / 00:20

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
for _ in range(M):
    t, a, b = map(int, input().split())
    if t == 0:
        if parent[a] != parent[b]:
            parent[a] = parent[b] = min(find_parent(parent, a), find_parent(parent, b))
    else:
        if parent[a] == parent[b]:
            print('YES')
        else:
            print('NO')