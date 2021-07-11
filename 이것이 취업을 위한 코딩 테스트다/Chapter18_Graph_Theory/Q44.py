# 00:16 / 00:40
from itertools import combinations

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

N = int(input())
x = []
y = []
z = []
for i in range(1, N+1):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

roads = []
for i in range(N-1):
    roads.append((x[i][1], x[i+1][1], x[i+1][0] - x[i][0]))
    roads.append((y[i][1], y[i+1][1], y[i+1][0] - y[i][0]))
    roads.append((z[i][1], z[i+1][1], z[i+1][0] - z[i][0]))

roads.sort(key=lambda x: x[2])

parent = list(range(N+1))
ret = 0

for a, b, c in roads:
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[a] = parent[b] = min(a, b)
        ret += c

print(ret)