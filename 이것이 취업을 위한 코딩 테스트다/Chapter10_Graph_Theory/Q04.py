# 00:18 / 00:50
from collections import deque

N = int(input())
time = [0]
indegree = [0]
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    inp = list(map(int, input().split()))
    time.append(inp[0])
    indegree.append(len(inp[1:-1]))
    for x in inp[1:-1]:
        graph[x].append(i)

print(time)
print(graph)

ret = time.copy()
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    for i in graph[cur]:
        ret[i] = max(ret[i], ret[cur] + time[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(*ret[1:], sep='\n')