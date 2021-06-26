n = int(input())
dp = [0] * n
dp[0] = 1

i2 = i3 = i5 = 0                        # 현재 값이 2, 3, 5와 곱해진 횟수
next2, next3, next5 = 2, 3, 5           # 현재 값에서 2, 3, 5를 곱했을 때 다음 값

for i in range(1, n):
    dp[i] = min(next2, next3, next5)    # 가장 작은 다음 값 선택
    if dp[i] == next2:                  # 못 생긴 수 중에서 순차적으로 2를 곱해서 다음 수 선정
        i2 += 1
        next2 = dp[i2] * 2
    if dp[i] == next3:                  # 2, 3의 공배수 일 수도 있으니까 elif가 아닌 if
        i3 += 1
        next3 = dp[i3] * 3
    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5

print(dp[-1])