def Linear_Search(list, target): # define a function, with parameters of list and target(must have a value when called upon)
  for i in range(len(list)): # loops through the list using the length of numbers, i is an integer
    if list[i] == target: # compares list[index] to the target, if true, does the indented
      return True # can be change to i to return index of where it was found in the list
  return False # can be changed to -1 to return it isn't in the index






