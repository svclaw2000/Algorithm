# 03:00 / 00:50

import itertools

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):                                     # 원으로 만들기 위해 간격 동일하게 2배로 연장
        weak.append(weak[i]+n)

    answer = len(dist) + 1                                      # 최대 인원수 + 1로 초기화
    seq_list = list(itertools.permutations(dist, len(dist)))    # 순열로 친구들의 모든 가능한 순서 생성

    for start in range(length):                                 # 각 취약지점에서 시작해 봄
        for friends in seq_list:
            count = 1                                           # 친구 한 명 투입
            position = weak[start] + friends[count-1]           # 친구가 도달하는 마지막 위치
            for index in range(start, start + length):          # 시작점부터 모든 취약지점 확인
                if position < weak[index]:                      # 다음 지점까지 가지 못하면 친구 추가
                    count += 1
                    if count > len(dist):                       # 모든 친구 투입하고도 다 못돌면 다음 seq
                        break
                    position = weak[index] + friends[count-1]
            answer = min(count, answer)
    if answer > len(dist):
        return -1
    return answer

print(solution(12, [1,5,6,10], [1,2,3,4]))
print(solution(12, [1,3,4,9,10], [3,5,7]))