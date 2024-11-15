def sumofdigits(num):
    if num == 0:
        return 0
    else:
        return num % 10 + sumofdigits(num // 10)
