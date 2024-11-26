tasks = {}
import subprocess
import os
import time

def menu():
    print(f"1. Add new task\n2. Update\n3. Delete\n4. View all\n5. Exit")


def addtask():
    task = input("task: ").strip()
    status = input("status(NS, IP, Comp: ")
    if status not in ["NS", "IP", "Comp"]:
        print("not valid status")
        return

    if task in tasks:
        print(f"Task '{task}' already exists.")
    else:
        tasks[task] = status
        print(f"Task '{task}' added with status '{status}'.")

def updatetask():
    task = input("Enter the task to update: ").strip()
    if task not in tasks:
        print(f"Task '{task}' not found.")
        return
    status = input("Enter the new status (NS for Not Started, IP for In Progress, Comp for Completed): ").strip()

    if status not in ["NS", "IP", "Comp"]:
        print("Invalid status! Please use 'NS', 'IP', or 'Comp'.")
        return

    tasks[task] = status
    print(f"Task '{task}' updated to status '{status}'.")


def deletetask():
    task = input("Enter the task to delete: ").strip()

    if task not in tasks:
        print(f"Task '{task}' not found.")
        return

    del(tasks[task])

def viewall():
    for index, (key, value) in enumerate(tasks.items()):
        print(f"Index {index}: {key}: {value}")


while True:
    print("\n")
    menu()
    os.system('cls')
    try:
        do = int(input("1-5: "))
    except:
        while True:
            image_path = 'no.png'
            subprocess.run(['start', image_path], shell=True)
            time.sleep(0.1)
        continue
    if do not in [1,2,3,4,5]:
        print("no")
        while True:
            image_path = 'no.png'
            subprocess.run(['start', image_path], shell=True)
            time.sleep(0.1)
            x = int(input("stop: "))
            if x == 0:
                break
        print("\n\n")
    elif do == 1:
        print("")
        addtask()
        continue
    elif do == 2:
        print("")
        updatetask()
        continue
    elif do == 3:
        print("")
        deletetask()
        continue
    elif do == 4:
        print("")
        viewall()
        continue
    elif do == 5:
        break



"""student1 = {
    "name":"Ray",
    "year":13,
    "house":"edwards",
    "subjects": ["economics", 'math', 'computer science']
            }


l = list(student1.keys())

for i in l:
    print(i)

print("\n\n\n\n")
for index, (key, value) in enumerate(student1.items()):
    print(f"Index {index}: {key}: {value}")"""
