array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    idx = i
    for j in range(i, len(array)):
        if array[j] < array[idx]:
            idx = j
    array[i], array[idx] = array[idx], array[i]

print(array)