# 00:17 / 00:20

N = int(input())
d = list(map(int, input().split()))

d.sort()

print(d[(N-1)//2])