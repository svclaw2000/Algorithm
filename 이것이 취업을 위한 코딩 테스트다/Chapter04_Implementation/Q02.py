# 00:10 / 00:20

a, b = input()
a = ord(a) - ord('a') + 1
b = int(b)

ds = ((-2, -1),
      (-2,  1),
      (-1, -2),
      (-1,  2),
      ( 1, -2),
      ( 1,  2),
      ( 2, -1),
      ( 2,  1))

ret = 0
for d in ds:
    if 0 < a+d[0] <= 8 and 0 < b+d[1] <= 8:
        ret += 1
print(ret)