# 00:50 / 00:50

def solution(n, build_frame):
    frame = []
    for x, y, a, b in build_frame:
        if a == 0:
            if b == 1:
                if y == 0 or '%d %d %d' %(x, y-1, 0) in frame or '%d %d %d' %(x-1, y, 1) in frame or '%d %d %d' %(x, y, 1) in frame:
                    frame.append('%d %d %d' %(x, y, a))
            else:
                # 불가능한 경우
                # (x-1, y+1), (x, y+1)에 보가 없고 (x, y+1)에 기둥이 있음
                # (x-1, y+1)에 보가 있고, (x-1, y)에 기둥이 없고, ((x-2, y+1), (x, y+1)에 둘 중에 하나라도 보가 없음)
                # (x, y+1)에 보가 있고, (x+1, y)에 기둥이 없고, ((x-1, y+1), (x+1, y+1)에 둘 중에 하나라도 보가 없음)
                if ('%d %d %d' %(x, y+1, 0) in frame and '%d %d %d' %(x-1, y+1, 1) not in frame and '%d %d %d' %(x, y+1, 1) not in frame) or \
                        ('%d %d %d' %(x-1, y+1, 1) in frame and '%d %d %d' %(x-1, y, 0) not in frame and ('%d %d %d' %(x-2, y+1, 1) not in frame or '%d %d %d' %(x, y+1, 1) not in frame)) or \
                        ('%d %d %d' %(x, y+1, 1) in frame and '%d %d %d' %(x+1, y, 0) not in frame and ('%d %d %d' %(x-1, y+1, 1) not in frame or '%d %d %d' %(x+1, y+1, 1) not in frame)):
                    pass
                else:
                    frame.remove('%d %d %d' %(x, y, a))
        else:
            if b == 1:
                if '%d %d %d' %(x, y-1, 0) in frame or '%d %d %d' %(x+1, y-1, 0) in frame or ('%d %d %d' %(x-1, y, 1) in frame and '%d %d %d' %(x+1, y, 1) in frame):
                    frame.append('%d %d %d' %(x, y, a))
            else:
                # 불가능한 경우
                # (x-1, y+1), (x, y+1)에 보가 없고 (x, y+1)에 기둥이 있음
                # (x-1, y+1)에 보가 있고, (x-1, y)에 기둥이 없고, ((x-2, y+1), (x, y+1)에 둘 중에 하나라도 보가 없음)
                # (x, y+1)에 보가 있고, (x+1, y)에 기둥이 없고, ((x-1, y+1), (x+1, y+1)에 둘 중에 하나라도 보가 없음)
                if ('%d %d %d' %(x-1, y, 1) in frame and '%d %d %d' %(x-1, y-1, 0) not in frame and '%d %d %d' %(x, y-1, 0) not in frame) or \
                        ('%d %d %d' %(x+1, y, 1) in frame and '%d %d %d' %(x+1, y-1, 0) not in frame and '%d %d %d' %(x+2, y-1, 0) not in frame) or \
                        ('%d %d %d' %(x+1, y, 0) in frame and '%d %d %d' %(x+1, y-1, 0) not in frame and '%d %d %d' %(x+1, y, 1) not in frame) or \
                        ('%d %d %d' %(x, y, 0) in frame and '%d %d %d' %(x, y-1, 0) not in frame and '%d %d %d' %(x-1, y, 1) not in frame):
                    pass
                else:
                    frame.remove('%d %d %d' %(x, y, a))
    return sorted([list(map(int, f.split())) for f in frame])

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))