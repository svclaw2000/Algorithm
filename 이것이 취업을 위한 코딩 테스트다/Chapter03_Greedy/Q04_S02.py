N, K = map(int, input().split())
ret = 0

while True:
    left = N % K    # -1을 몇 번 해야 K의 배수가 되는지 확인
    ret += left     # 횟수만큼 출력에 더함
    N -= left
    if N < K:       # 더 이상 나누어 떨어질 일이 없으므로 중지
        break
    N //= K         # K로 나누고 횟수 1 더함
    ret += 1

print(ret + N-1)    # 남은 N-1 만큼 더함 (마지막에 1 남아야 해서)
