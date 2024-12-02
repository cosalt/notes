def binary_search(num):
    currentnode = rootnodepointer
    while currentnode != -1:
        if tree[currentnode].data > num:
            currentnode = tree[currentnode].left
        elif tree[currentnode].data < num:
            currentnode = tree[currentnode].right
        else:
            return "found"
    else:
        return "not found"
