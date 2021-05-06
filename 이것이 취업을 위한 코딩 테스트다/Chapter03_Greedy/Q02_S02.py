N, M, K = map(int, input().split())
nums = sorted(list(map(int, input().split())))
s1 = (M - M // (K+1)) * nums[-1]    # 가장 큰 수 K번, 두 번째 큰 수 1번이 반복되므로 두 번째 큰 수는 K+1회마다 한 번 나옴
s2 = M // (K+1) * nums[-2]          # 나머지 횟수는 가장 큰 수
print(s1 + s2)