array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

small = min(array)
count = [0] * (max(array) - small + 1)

for i in array:
    count[i - small] += 1

result = []
for i, c in enumerate(count):
    for _ in range(c):
        result.append(i + small)

print(result)