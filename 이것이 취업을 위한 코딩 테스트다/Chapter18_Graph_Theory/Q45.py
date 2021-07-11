# 00:17 / 01:00
from collections import deque

for _ in range(int(input())):
    n = int(input())
    past_rank = [0] + list(map(int, input().split()))
    m = int(input())
    change = [list(map(int, input().split())) for _ in range(m)]

    indegree = [0] * (n+1)
    matrix = [[False] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            matrix[past_rank[i]][past_rank[j]] = True
            indegree[past_rank[j]] += 1

    for a, b in change:
        if matrix[a][b]:
            matrix[a][b] = False
            matrix[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            matrix[a][b] = True
            matrix[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    ret = []
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    result = None

    for i in range(1, n+1):
        if not q:
            result = 'IMPOSSIBLE'
            break
        if len(q) >= 2:
            result = '?'
            break

        cur = q.popleft()
        ret.append(cur)
        for j in range(1, n+1):
            if matrix[cur][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if result:
        print(result)
    else:
        print(*ret)