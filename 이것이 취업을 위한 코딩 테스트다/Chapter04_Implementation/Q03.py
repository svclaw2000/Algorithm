# 00:14 / 00:40

N, M = map(int, input().split())
x, y, d = map(int, input().split())
table = [input().split() for _ in range(N)]

ds = ((-1,  0),
      ( 0,  1),
      ( 1,  0),
      ( 0, -1))

ret = 0
while True:
    if table[x+ds[0][0]][y+ds[0][1]] != '0' and table[x+ds[1][0]][y+ds[1][1]] != '0' and \
            table[x+ds[2][0]][y+ds[2][1]] != '0' and table[x+ds[3][0]][y+ds[3][1]] != '0':
        if table[x-ds[d][0]][y-ds[d][1]] == '1':
            break
        else:
            x -= ds[d][0]
            y -= ds[d][1]
    d = (d-1) % 4
    if table[x+ds[d][0]][y+ds[d][1]] == '0':
        x += ds[d][0]
        y += ds[d][1]
        table[x][y] = '2'
        ret += 1
print(ret)
