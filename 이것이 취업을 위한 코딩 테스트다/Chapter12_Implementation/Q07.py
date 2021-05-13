# 00:02 / 00:20

a = list(map(int, input()))
n = len(a) // 2
print('LUCKY' if sum(a[:n]) == sum(a[n:]) else 'READY')