LinkedList = [[-1, i+1] for i in range(20)] # DECLARE LinkedList of ARRAY[0:20} of ARRAY[0:20}
LinkedList[-1][-1] = -1

FirstNode = -1 # DECLARE FirstNode : INTEGER
FirstEmpty = 0 # DECLARE FirstEmpty : INTEGER

def InsertData():
    global FirstNode, FirstEmpty
    if FirstEmpty == -1:
        return LinkedList
    else:
        count = 0
        while count != 5:
            num = int(input("Enter a positive integer: "))
            if num < 0:
                continue
            else:
                count += 1
                if FirstNode == -1:
                    FirstNode = 0
                    LinkedList[FirstNode][0] = num
                else:
                    LinkedList[FirstEmpty][0] = num

                FirstEmpty += 1
    return LinkedList

def OutputLinkedList():
    pointer = FirstNode
    while pointer != -1:
        print(f"Node Pointer: {pointer}, Data: {LinkedList[pointer][0]}")
        pointer = LinkedList[pointer][1]
    else:
        return print("end of linkedlist")



def RemoveData(removing):
    global LinkedList, FirstNode
    pointer = FirstNode

    if pointer == -1:
        return LinkedList

    if LinkedList[pointer][0] == removing:
        FirstNode = LinkedList[pointer][1]
        LinkedList[pointer][0] = -1
        return LinkedList

    while pointer != -1:
        next_pointer = LinkedList[pointer][1]
        if next_pointer != -1 and LinkedList[next_pointer][0] == removing:
            LinkedList[pointer][1] = LinkedList[next_pointer][1]
            LinkedList[next_pointer][0] = -1
            return LinkedList

        pointer = next_pointer

    return LinkedList

InsertData()
OutputLinkedList()

RemoveData(5)
print("After")
OutputLinkedList()
