QueueArray = ["" for i in range(10)]
headpointer = 0 # DECLARE headpointer: INTEGER
tailpointer = 0 # DECLARE tailpointer: INTEGER
items = 0 # DECLARE items: INTEGER



def Dequeue():
    global QueueArray, headpointer, tailpointer, items
    if items == 0:
        return False
    QueueArray[headpointer] = ""
    if headpointer >= 9:
        headpointer = 0
    else:
        headpointer = headpointer + 1
    items = items - 1
    return True

def Enqueue(DataToAdd):
    global QueueArray, headpointer, tailpointer, items
    if items == 10:
        return False
    QueueArray[tailpointer] = DataToAdd
    if tailpointer >= 9:
        tailpointer = 0
    else:
        tailpointer = tailpointer + 1
    items = items + 1
    return True

for i in range(11):
    value = input("Value: ")
    print(f" Attempt: {Enqueue(value)}")

print(Dequeue())
print(Dequeue())

print(QueueArray)

print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
Enqueue("YOOOO")
Enqueue("fdfdfdfd")
print(Dequeue())
print(QueueArray)
