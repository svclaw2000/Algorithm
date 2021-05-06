# 00:30 / 00:20

nums = list(map(lambda x: bool(int(x)), input()))
ret = 0

while nums:
    if nums[0] != nums[-1]:                                 # 시작과 끝이 다르면 잘라서 같게 만듬
        start = 0
        while nums[start] == nums[start+1]:                 # start와 start+1이 다를 때까지 돌아감
            start += 1
        nums = nums[start+1:]
        ret += 1
    else:
        start, end = 0, len(nums)-1
        while start < end and nums[start] == nums[start+1]: # start와 start+1이 다를 때까지 돌아감
            start += 1
        if start == end:                                    #끝
            break
        while nums[end] == nums[end-1]:                     # end와 end-1이 다를 때까지 돌아감
            end -= 1
        nums = nums[start+1:end]
        ret += 1
print(ret)