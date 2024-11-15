def calc(num, power):
    if power == 1:
        return num
    else:
        return calc(num, power-1) * num
