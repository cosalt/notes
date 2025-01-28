class node:
    def __init__(self):
        self.Data = ""
        self.Pointer = -1


arr = []


for i in range(6):
    node1 = node()
    if i == 5:
        pass
    else:
        node1.Pointer = i + 1
        node1.Data = ''
    arr.append(node1)

def printarr():
    global startpointer, emptypointer
    if startpointer == -1:
        print("no.")
    else:
        temp = startpointer
        while temp != -1:
            node = arr[temp]
            print(f"Pointer: {node.Pointer} Data: {node.Data}")
            temp = node.Pointer


emptypointer = 0
startpointer = -1


def addnode(data):
    global startpointer, emptypointer
    if startpointer == -1:
        arr[emptypointer].Data = data
        startpointer = emptypointer
        temp = emptypointer
        emptypointer = arr[emptypointer].Pointer
        arr[temp].Pointer = -1
    else:
        arr[emptypointer].Data = data
        temp = emptypointer

        emptypointer = arr[emptypointer].Pointer
        arr[temp].Pointer = -1
        
        for i in range(len(arr)):
            if arr[i].Pointer == -1:
                


addnode(3)
printarr()
