# 00:40 / 00:20 제한 시간 초과

def solution(N, stages):
    count = [0] * (N+2)
    for s in stages:
        count[s] += 1
    arr = [(count[i]/sum(count[i:]) if count[i] > 0 else 0, i) for i in range(1, N+1)]
    arr.sort(key=lambda x: (-x[0], x[1]))
    return [c[1] for c in arr]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))