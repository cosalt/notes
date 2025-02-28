linkedlist = [[-1,i+1] for i in range(20)]
linkedlist[-1][1] = -1
# [integer, pointer]

print(linkedlist)

FirstNode = -1 # DECLARE FirstNode: Integer
FirstEmpty = 0 # DECLARE FirstEmpty: Integer

def InsertData():
    global linkedlist, FirstEmpty
    for i in range(5):
        if FirstEmpty == -1:
            print("The linked list is full!")
            return
        else:
            userdata = int(input("Data: "))

            linkedlist[FirstEmpty][0] = userdata
            temp = FirstNode
            FirstNode = linkedlist[FirstEmpty][1]
            FirstEmpty = linkedlist[FirstEmpty][1]
            linkedlist[temp][1] = FirstNode



    print(linkedlist)

InsertData()
print(f"FirstNode {FirstNode}")
print(f"FirstEmpty {FirstEmpty}")
