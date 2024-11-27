# Notes Repository

## Overview
This repository contains a collection of notes, code snippets, and solved challenges across various topics. The aim is to provide a comprehensive resource for programming concepts and problem-solving techniques.

---

## Table of Contents

1. [Assembly Language Notes](#1-assembly-language-notes)  
2. [Prolog Notes](#2-prolog-notes)  
3. [Python Built-ins](#3-python-built-ins)  
4. [Recursive Challenges](#4-recursive-challenges)  
5. [Searching Algorithms](#5-searching-algorithms)  
6. [Sorting Algorithms](#6-sorting-algorithms)  
7. [Advent of Code Solutions](#7-advent-of-code-solutions)  
8. [GitHub Notes](#8-github-notes)  

---

## 1. Assembly Language Notes

### Overview
This section contains notes on assembly language, covering fundamental instructions and concepts.

### Topics Covered
- **Data Movement Instructions**  
  ```
  MOV AX, 5    ; Move 5 into register AX
  PUSH AX      ; Push the value of AX onto the stack
  POP BX       ; Pop the value from the stack into BX
  ```

- **Arithmetic Operations**  
  ```
  ADD AX, BX   ; Add the value in BX to AX
  SUB AX, 10   ; Subtract 10 from AX
  ```

- **Control Flow**  
  ```
  JMP Label    ; Unconditional jump to Label
  Label:
      CALL Subroutine
      RET
  ```

---

## 2. Prolog Notes

### Overview
An introduction to Prolog, focusing on logic programming.

### Topics Covered
- **Defining Facts and Rules**  
  ```
  parent(john, mary).
  parent(mary, alice).

  grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
  ```

- **Querying**  
  ```
  ?- grandparent(john, alice).
  true.
  ```

---

## 3. Python Built-ins

### Overview
Detailed explanations and examples of Python's built-in functions.

### Examples
- **Data Conversion**  
  ```
  number = int("42")  # Convert string to integer
  text = str(123)     # Convert integer to string
  ```

- **Data Processing**  
  ```
  nums = [1, 2, 3, 4]
  squared = list(map(lambda x: x**2, nums))  # [1, 4, 9, 16]
  ```

- **Utility Functions**  
  ```
  value = input("Enter a number: ")
  print("You entered:", value)
  ```

---

## 4. Recursive Challenges

### Topics Covered
- **Factorial Calculation**  
  ```
  def factorial(n):
      if n == 0:
          return 1
      return n * factorial(n - 1)
  ```

- **Fibonacci Sequence**  
  ```
  def fibonacci(n):
      if n <= 1:
          return n
      return fibonacci(n - 1) + fibonacci(n - 2)
  ```

---

## 5. Searching Algorithms

### Examples
- **Linear Search**  
  ```
  def linear_search(arr, target):
      for i, value in enumerate(arr):
          if value == target:
              return i
      return -1
  ```

- **Binary Search**  
  ```
  def binary_search(arr, target):
      low, high = 0, len(arr) - 1
      while low <= high:
          mid = (low + high) // 2
          if arr[mid] == target:
              return mid
          elif arr[mid] < target:
              low = mid + 1
          else:
              high = mid - 1
      return -1
  ```

---

## 6. Sorting Algorithms

### Examples
- **Bubble Sort**  
  ```
  def bubble_sort(arr):
      n = len(arr)
      for i in range(n):
          for j in range(0, n - i - 1):
              if arr[j] > arr[j + 1]:
                  arr[j], arr[j + 1] = arr[j + 1], arr[j]
  ```

- **Merge Sort**  
  ```
  def merge_sort(arr):
      if len(arr) > 1:
          mid = len(arr) // 2
          left = arr[:mid]
          right = arr[mid:]

          merge_sort(left)
          merge_sort(right)

          i = j = k = 0
          while i < len(left) and j < len(right):
              if left[i] < right[j]:
                  arr[k] = left[i]
                  i += 1
              else:
                  arr[k] = right[j]
                  j += 1
              k += 1

          while i < len(left):
              arr[k] = left[i]
              i += 1
              k += 1

          while j < len(right):
              arr[k] = right[j]
              j += 1
              k += 1
  ```

---

## 7. Advent of Code Solutions

### Overview
Solutions to Advent of Code problems, organized by year.

### Example
- **Day 1: Calorie Counting**  
  ```
  with open("input.txt") as f:
      data = list(map(int, f.read().split()))

  print(sum(data))
  ```

---

## 8. GitHub Notes

### Topics Covered
- **Common Git Commands**  
  ```
  git clone <repository-url>
  git commit -m "Commit message"
  git push origin main
  ```

- **Creating Pull Requests**  
  1. Create a branch:  
     ```
     git checkout -b feature-branch
     ```
  2. Push changes:  
     ```
     git push origin feature-branch
     ```
  3. Open a pull request on GitHub.

- **Handling Merge Conflicts**  
  ```
  git merge main
  # Resolve conflicts in the editor
  git add .
  git commit
  ```

---

## Contributing

Contributions are welcome! To contribute:  
1. Fork the repository.  
2. Create a branch for your changes.  
3. Submit a pull request with a clear description.

---
