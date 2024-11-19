def binarysearch(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (right + left) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return - 1
