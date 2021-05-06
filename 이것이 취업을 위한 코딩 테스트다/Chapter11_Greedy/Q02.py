# 00:03 / 00:30

nums = list(map(int, input()))
ret = nums[0]
for n in nums[1:]:
    if ret == 0 or ret == 1 or n == 0 or n == 1:    # 현재 결과 또는 현재 수가 0 또는 1이면 더함
        ret += n
    else:                                           # 아니면 곱함
        ret *= n
print(ret)