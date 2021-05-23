# 00:10 / 00:30

N, M = map(int, input().split())
maze = [input() for _ in range(N)]

def run(i, j, dist, d):
    if not 0 <= i < N or not 0 <= j < M or maze[i][j] == '0' or dist > N*M:
        return N * M
    if i == N-1 and j == M-1:
        return dist
    ret = []
    if not d == 'U': ret.append(run(i+1, j, dist+1, 'D'))
    if not d == 'D': ret.append(run(i-1, j, dist+1, 'U'))
    if not d == 'L': ret.append(run(i, j+1, dist+1, 'R'))
    if not d == 'R': ret.append(run(i, j-1, dist+1, 'L'))
    return min(ret)

print(run(0, 0, 1, ''))