class Node:
    def __init__(self):
        self.data = ""
        self.left = -1
        self.right = -1

def Createtree():
    tree = []
    for i in range(1,8):
        node = Node()
        node.left = i
        tree.append(node)
    tree[-1].left = -1
    return tree

def printtree():
    for i,node in enumerate(tree):
        left_data = node.left
        right_data = node.right
        print(f"Node{i}: {node.data}, Left: {left_data}, Right: {right_data}")
    print("")
    print(f"emptylistpointer: {emptylistpointer}, rootnodepointer: {rootnodepointer}")
emptylistpointer = 0
rootnodepointer = -1
tree = Createtree()

def addnode(userdata):
    global emptylistpointer, rootnodepointer
    if rootnodepointer == -1:
        tree[emptylistpointer].data = userdata
        emptylistpointer = tree[emptylistpointer].left
        tree[emptylistpointer].left = -1
        rootnodepointer = emptylistpointer
    else:
        pass

addnode("ANDY")
printtree()
