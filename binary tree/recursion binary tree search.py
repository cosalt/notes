def binarysearch(node, num):
    if tree[node].data == num:
        print("found")
        return
    if node == -1:
        print("not found")
        return

    if tree[node].data > num:
        binarysearch(tree[node].left, num)
    else:
        binarysearch(tree[node].right, num)
