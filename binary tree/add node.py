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
