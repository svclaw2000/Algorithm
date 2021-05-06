# 00:05 / 00:30

N, M, K = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ret, c = 0, 0
for _ in range(M):
    if c < K:
        ret += nums[-1]
        c += 1
    else:
        c = 0
        ret += nums[-2]
print(ret)
