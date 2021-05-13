# 00:20 / 00:40

def solution(key, lock):
    m = len(key)
    n = len(lock)
    for _ in range(4):
        for x in range(-m+1, n):
            for y in range(-m+1, n):
                cant = False
                for i in range(n):
                    if cant: break
                    for j in range(n):
                        if x <= i < x+m and y <= j < y+m:
                            if key[i-x][j-y] == lock[i][j]:
                                cant = True
                                break
                        elif lock[i][j] == 0:
                            cant = True
                            break
                if not cant:
                    return True
        key = [[key[m-1-j][i] for j in range(m)] for i in range(m)]
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))