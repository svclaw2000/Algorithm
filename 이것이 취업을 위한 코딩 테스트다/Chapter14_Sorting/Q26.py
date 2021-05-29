# 00:07 / 00:30 Failed

import heapq

N = int(input())
arr = []
for _  in range(N):
    heapq.heappush(arr, int(input()))               # 입력하면서 정렬

result = 0
while len(arr) > 1:
    s = heapq.heappop(arr) + heapq.heappop(arr)     # 가장 작은 두 묶음 선택
    heapq.heappush(arr, s)                          # 새로운 묶음으로 넣음
    result += s                                     # 결과에 비교횟수 추가

print(result)