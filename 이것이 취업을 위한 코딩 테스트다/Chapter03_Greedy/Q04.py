# 00:02 / X

N, K = map(int, input().split())
ret = 0
while N != 1:
    if N % K == 0:
        N //= K
    else:
        N -= 1
    ret += 1
print(ret)