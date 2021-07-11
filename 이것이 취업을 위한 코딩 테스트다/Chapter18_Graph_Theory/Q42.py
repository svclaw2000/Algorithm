# 00:07 / 00:50

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

G = int(input())
P = int(input())
parent = list(range(G+1))
ret = 0
for _ in range(P):
    p = find_parent(parent, int(input()))
    if p == 0:
        break
    parent[p] = p-1
    ret += 1
print(ret)