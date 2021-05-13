# 00:03 / 00:20

a = list(input())
nums = list(map(str, range(10)))
eng = sorted([c for c in a if c not in nums])
num = sum([int(i) for i in a if i in nums])
print(''.join(eng) + str(num))