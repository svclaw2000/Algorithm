# 00:08 / 00:30

food_times = [3, 1, 2]
k = 5
cur = 0

s = sum([t > cur for t in food_times])
while k >= s:
    k -= s
    cur += 1
    s = sum([t > cur for t in food_times])

for i, t in enumerate([t > cur for t in food_times]):
    if t:
        if k == 0:
            print(i+1)
            break
        k -= 1