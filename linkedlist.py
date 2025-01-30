class node:
    def __init__(self):
        self.Data = ""
        self.Pointer = -1


arr = []


for i in range(20):
    node1 = node()
    if i == 5:
        pass
    else:
        node1.Pointer = i + 1
        node1.Data = ''
    arr.append(node1)

def printarr():
    global startpointer, emptypointer
    print("")
    if startpointer == -1:
        print("no.")
    else:
        temp = startpointer
        while temp != -1:
            node = arr[temp]
            print(f"Data: {node.Data} Pointer: {node.Pointer}")
            temp = node.Pointer
    print(f"EmptyListPointer: {emptypointer}\nStartListPointer: {startpointer}")

emptypointer = 0
startpointer = -1

def addnode(data):
    global startpointer, emptypointer, arr
    if emptypointer == -1:
        print("full. ")
        return None
    
    temp = emptypointer
    emptypointer = arr[emptypointer].Pointer
    arr[temp].Data = data
    arr[temp].Pointer = -1

    if startpointer == -1:
        startpointer = temp
    else:
        prev = -1
        current = startpointer
        while current != -1 and arr[current].Data < data:
            prev = current
            current = arr[current].Pointer
        if prev == -1:
            arr[temp].Pointer = startpointer
            startpointer = temp
        else:
            arr[temp].Pointer = arr[prev].Pointer
            arr[prev].Pointer = temp
    return arr


addnode(3)
addnode(4)
addnode(5)
for j in arr:
    print(j.Pointer)
printarr()


addnode(4.5)
printarr()

def removenode(data):
    global startpointer, emptypointer, arr
    if emptypointer == -1:
        print("full. ")
        return None

    temp = startpointer
    prev = -1

    while temp != -1:
        if arr[temp].Data == data:
            if prev == -1:
                startpointer = arr[temp].Pointer
            else:
                arr[prev].Pointer = arr[temp].Pointer
            arr[temp].Pointer = emptypointer
            emptypointer = temp

            print(f"Node with data {data} removed.")
            return
        prev = temp
        temp = arr[temp].Pointer

removenode(4.5)
printarr()


addnode(8)
addnode(7)
addnode(6)
addnode(9)
printarr()
