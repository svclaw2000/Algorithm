# 00:19 / 00:40

from collections import deque

N = int(input())
K = int(input())
apples = [input() for _ in range(K)]
L = int(input())
directions = []
for _ in range(L):
    inp = input().split()
    directions.append((int(inp[0]), inp[1]))

ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
x, y, d = 1, 1, 0
ret = 0
cur_d = 0
snake = deque(['0 0'])
while True:
    if cur_d < L and directions[cur_d][0] == ret:
        d = ((d+1) % 4) if (directions[cur_d][1] == 'D') else ((d-1) % 4)
        cur_d += 1
    x += ds[d][0]
    y += ds[d][1]
    cur_pos = '%d %d' %(x, y)
    if not (0 < x <= N and 0 < y <= N) or cur_pos in snake:
        break
    snake.append(cur_pos)
    if cur_pos in apples:
        apples.remove(cur_pos)
    else:
        snake.popleft()
    ret += 1
print(ret+1)