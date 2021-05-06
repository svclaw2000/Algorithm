# 00:05 / 00:30

N, M = map(int, input().split())
balls = list(map(int, input().split()))
count = [balls.count(i) for i in range(1, M+1)]             # 각 공의 개수
print(sum([count[i]*sum(count[i+1:]) for i in range(M-1)])) # 무게 A의 수*무게 B의 수. 겹치지 않게 무게 A의 수는 뺌