# 00:31 / 00:20 제한시간초과

def solution(w):
    if not w:                       # 1
        return w
    cnt = 0
    idx = 0
    right = True
    u_right = False
    for i, c in enumerate(w):
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
        if idx == 0 and cnt == 0:   # [0, idx)까지 더 이상 쪼갤 수 없는 균형잡힌 문자열
            if right:
                u_right = True
            idx = i+1
        if cnt < 0:
            right = False
    u, v = w[:idx], w[idx:]         # 2
    if u_right:                     # 3
        return u + solution(v)      # 3-1
    ret = '(' + solution(v) + ')'
    for c in u[1:-1]:
        if c == '(':
            ret += ')'
        else:
            ret += '('
    return ret

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))