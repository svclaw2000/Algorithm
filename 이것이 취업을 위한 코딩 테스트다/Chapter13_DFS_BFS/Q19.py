# 00:14 / 00:30

from collections import deque

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

queue = deque()
queue.append((1, A[0], add, sub, mul, div))

ret_max = -10e10
ret_min = 10e10
while queue:
    idx, cur, add, sub, mul, div = queue.popleft()
    if add + sub + mul + div == 0:
        ret_max = max(cur, ret_max)
        ret_min = min(cur, ret_min)
        continue
    if add: queue.append((idx+1, cur + A[idx], add-1, sub, mul, div))
    if sub: queue.append((idx+1, cur - A[idx], add, sub-1, mul, div))
    if mul: queue.append((idx+1, cur * A[idx], add, sub, mul-1, div))
    if div: queue.append((idx+1, cur // A[idx] if cur > 0 else -((-cur) // A[idx]), add, sub, mul, div-1))

print(ret_max)
print(ret_min)