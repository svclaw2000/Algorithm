# 02:00 / 00:40
import itertools

N, M = map(int, input().split())
home, chicken = [], []
for i in range(N):
    inp = input().split()
    for j, p in enumerate(inp):
        if p == '1':
            home.append((i, j))
        elif p == '2':
            chicken.append((i, j))

print(min([sum([min([abs(c[0]-h[0])+abs(c[1]-h[1]) for c in cs]) for h in home]) for cs in itertools.combinations(chicken, M)]))