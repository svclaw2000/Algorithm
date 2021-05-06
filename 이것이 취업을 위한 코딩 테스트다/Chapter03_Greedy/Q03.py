# 00:02 / X

N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]
print(max(map(min, cards)))