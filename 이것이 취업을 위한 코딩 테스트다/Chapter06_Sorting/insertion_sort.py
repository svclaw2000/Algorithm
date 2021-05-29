array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    idx = i
    while idx > 0 and array[idx] < array[idx-1]:
        array[idx-1], array[idx] = array[idx], array[idx-1]
        idx -= 1

print(array)