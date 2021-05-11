# 00:30 / 00:20

nums = input()
print((len([1 for i in range(len(nums)-1) if nums[i] != nums[i+1]]) + 1) // 2)