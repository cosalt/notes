def removestr(string):
    integers = [int(letter) for letter in string if letter.isdigit()]
    if not integers:
        return None
    return(int(str(integers[0])+str(integers[-1])))
total = []
with open("text.txt") as t:
    for line in t:
        total.append(removestr(line))
print(sum(total))
