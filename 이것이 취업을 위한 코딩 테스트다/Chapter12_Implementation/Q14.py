# 03:00 / 00:50

import itertools

def solution(n, weak, dist):
    weak.sort()
    dist.sort(reverse=True)

    weak_dist = [(weak[i]-weak[i-1]) % n for i in range(len(weak))]*2
    for num in range(1, len(dist)+1):
        for start in range(len(weak)):
            cur_dist = weak_dist[start:start+len(weak)]
            # 임의로 num-1개 빼기
            if num > 1:
                out = list(itertools.combinations(range(len(weak)), num-1))
                for i in range(num):
                    pass


    answer = 0
    return answer

print(solution(12, [1,5,6,10], [1,2,3,4]))
print(solution(12, [1,3,4,9,10], [3,5,7]))