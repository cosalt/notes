arr = ["12,ray,m,1", "23,john, f, 2"]

array = []
for i,j in enumerate(arr):
    array.append(arr[i].split(","))
    
print(array)
