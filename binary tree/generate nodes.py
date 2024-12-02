def generatenodes():
    for num in range(5000):
        addnode(num)
        print(f"Added node with value {num}")
        printtree()
        print("\n")

generatenodes()
