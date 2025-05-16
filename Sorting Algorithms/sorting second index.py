#bubble
n = len(array)
for i in range(n):
    for j in range(0, n - i - 1):
        if array[j][1] > array[j + 1][1]:
            array[j], array[j + 1] = array[j + 1], array[j]

#insertion
for i in range(1, len(array)):
    key = array[i]
    j = i - 1
    while j >= 0 and array[j][1] > key[1]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key
