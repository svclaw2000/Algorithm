n = int(input())
coins = sorted(list(map(int, input().split())))

target = 1              # 1 만들 수 있는지 확인
for c in coins:
    if target < c:      # 1 ~ K 까지 만들 수 있으면 A < K인 A가 추가됐을 때 A+K까지 만들 수 있음
        break
    else:
        target += c
print(target)