def binarysearch(arr, search):
    arr.sort()
    lower = 0
    upper = len(arr) - 1
    while (lower <= upper):
        mid = (lower + upper) // 2
        if arr[mid] == search:
            return(mid)
        elif arr[mid] < search:
            lower = mid + 1
        else:
            upper = mid - 1
    return(f"not found")




arr = [4, 22, 36, 50, 83, 121, 180]
print(binarysearch(arr, 40))
