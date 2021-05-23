# 00:25 / 00:60
from itertools import combinations

N = int(input())
floor = [input().split() for _ in range(N)]
empty = []
teacher = []

for i, row in enumerate(floor):
    for j, cell in enumerate(row):
        if cell == 'X':
            empty.append((i, j))
        elif cell == 'T':
            teacher.append((i, j))

cases = combinations(empty, 3)

ds = ((-1, 0), (0, 1), (1, 0), (0, -1))

success = False
for case in cases:
    if success: break
    failed = False
    for tx, ty in teacher:
        if failed: break
        for dx, dy in ds:
            if failed: break
            cx, cy = tx, ty
            while True:
                cx += dx
                cy += dy
                if not (0 <= cx < N and 0 <= cy < N):
                    break
                if floor[cx][cy] == 'O' or floor[cx][cy] == 'T' or (cx, cy) in case:
                    break
                if floor[cx][cy] == 'S':
                    failed = True
                    break
    success = not failed

print('YES' if success else 'NO')