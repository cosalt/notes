class Node:
    def __init__(self):
        self.data = -1
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
        rootnodepointer = emptylistpointer
    else:
        currentnode = rootnodepointer
        while True:
            if userdata < tree[currentnode].data:
                if tree[currentnode].left == -1:
                    tree[currentnode].left = emptylistpointer
                    break
                else:
                    currentnode = tree[currentnode].left
            else:
                if tree[currentnode].right == -1:
                    tree[currentnode].right = emptylistpointer
                    break
                else:
                    currentnode = tree[currentnode].right
    tree[emptylistpointer].data = userdata
    temp = tree[emptylistpointer].left
    tree[emptylistpointer].left = -1
    tree[emptylistpointer].right = -1
    emptylistpointer = temp
