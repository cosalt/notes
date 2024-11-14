def IterativeCalculate(num):
    arr = []
    for i in range(1, num + 1):
        if (num % i) == 0:
            arr.append(i)
    return sum(arr)



def recursivecalculate(num, i, total=0):
    if i != 0:
        if (num % i) == 0:
            total = total + i
        return rec(num, i-1, total)
    return total

print(recursivecalculate(10, 10))
