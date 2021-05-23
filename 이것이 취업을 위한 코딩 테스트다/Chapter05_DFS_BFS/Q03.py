# 00:12 / 00:30

N, M = map(int, input().split())
case = [input() for _ in range(N)]
visited = [[False]*M for _ in range(N)]                 # 방문 여부

ret = 0

def visit(i, j):
    if not 0 <= i < N or not 0 <= j < M or case[i][j] == '1' or visited[i][j]:
        return                                          # 범위를 벗어나거나 벽이거나 방문했으면 끝
    visited[i][j] = True                                # 방문 표시
    visit(i-1, j)                                       # 4개의 방향으로 탐색 시도
    visit(i+1, j)
    visit(i, j-1)
    visit(i, j+1)

for i in range(N):
    for j in range(M):
        if case[i][j] == '0' and not visited[i][j]:     # 방문하지 않았고 비어있으면
            ret += 1
            visit(i, j)                                 # 인접 공간 채우기

print(ret)