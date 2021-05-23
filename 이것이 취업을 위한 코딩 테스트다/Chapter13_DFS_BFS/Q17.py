# 00:37 / 00:50 Failed
from collections import deque

N, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
viruses = [deque() for _ in range(K+1)]

for i, row in enumerate(table):
    for j, cell in enumerate(row):
        if cell > 0:
            viruses[cell].append((i, j))                        # 해당 바이러스 리스트에 위치 기록

sec = 0
while table[X-1][Y-1] == 0 and sec < S:                         # 목표 칸이 채워지거나 시간 되면 스톱
    for v_i, virus in enumerate(viruses):                       # 바이러스 종류 순서대로 실행
        for _ in range(len(virus)):                             # 해당 시점까지의 바이러스 위치만 사용
            i, j = virus.popleft()
            if not (0 <= i < N and 0 <= j < N):                 # (i, j)가 범위를 벗어나면 무시
                continue
            if table[i][j] > 0 and table[i][j] != v_i:          # (i, j)가 채워져있고 다른 바이러스면 무시
                continue
            table[i][j] = v_i                                   # (i, j)가 비어있거나 자기 바이러스인 경우
            virus.append((i-1, j))                              # 주변으로 퍼져나감
            virus.append((i+1, j))
            virus.append((i, j-1))
            virus.append((i, j+1))
    sec += 1
print(table[X-1][Y-1])