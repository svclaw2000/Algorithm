# 00:31 / 00:50 시간초과
from collections import deque

def solution(board):
    N = len(board)
    queue = deque()
    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
    queue.append((0, 0, 0, 1, 0))
    while queue:
        x1, y1, x2, y2, t = queue.popleft()

        for dx, dy in ds:
            nx1 = x1 + dx
            ny1 = y1 + dy
            nx2 = x2 + dx
            ny2 = y2 + dy
            if 0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N:
                if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                    # 회전
                    if x1 == x2 and dx != 0:  # 가로로 놓여있고 세로로 이동 가능, 즉 비어있음
                        tx1, ty1, tx2, ty2 = x1, y1, x1+dx, y1
                        if (tx1 == N-1 and ty1 == N-1) or (tx2 == N-1 and ty2 == N-1):
                            return t+1
                        queue.append((tx1, ty1, tx2, ty2, t+1))
                        tx1, ty1, tx2, ty2 = x2+dx, y2, x2, y2
                        if (tx1 == N-1 and ty1 == N-1) or (tx2 == N-1 and ty2 == N-1):
                            return t+1
                        queue.append((tx1, ty1, tx2, ty2, t+1))
                    elif y1==y2 and dy != 0:           # 세로
                        tx1, ty1, tx2, ty2 = x1, y1, x1, y1+dy
                        if (tx1 == N-1 and ty1 == N-1) or (tx2 == N-1 and ty2 == N-1):
                            return t+1
                        queue.append((tx1, ty1, tx2, ty2, t+1))
                        tx1, ty1, tx2, ty2 = x2, y2+dy, x2, y2
                        if (tx1 == N-1 and ty1 == N-1) or (tx2 == N-1 and ty2 == N-1):
                            return t+1
                        queue.append((tx1, ty1, tx2, ty2, t+1))
                    # 이동
                    if (nx1 == N-1 and ny1 == N-1) or (nx2 == N-1 and ny2 == N-1):
                        return t+1
                    queue.append((nx1, ny1, nx2, ny2, t+1))
    return 0

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))