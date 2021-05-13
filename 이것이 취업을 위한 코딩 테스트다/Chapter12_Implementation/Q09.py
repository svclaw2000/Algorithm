# 00:23 / 00:30

def solution(s):
    n = len(s)
    ret = n
    for l in range(1, n+1):
        cur = ''
        cnt = 0
        res = ''
        for i in range(n//l):
            if cur == s[i*l:(i+1)*l]:
                cnt += 1
            else:
                res += (str(cnt) if cnt > 1 else '') + cur
                cur = s[i*l:(i+1)*l]
                cnt = 1
        res += (str(cnt) if cnt > 1 else '') + cur
        res += (s[-(n%l):] if n % l != 0 else '')

        if len(res) < ret:
            ret = len(res)
    return ret

print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))