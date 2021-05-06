# 00:05 / 00:30

N = int(input())
people = sorted(list(map(int, input().split())))
ret = 0                     # 그룹 수
i = 0                       # 현재 인원
while i < N:
    i += 1                  # 인원 + 1
    if people[i-1] <= i:    # 현재 그룹에서 가장 큰 공포도가 인원수보다 작으면 그룹 출발
        people = people[i:] # 출발한 사람들은 인원에서 제외
        ret += 1            # 그룹 + 1
        N -= i              # 전체 인원수에서 빼기
        i = 0               # 출발 했으므로 그룹 내 인원 0
print(ret)