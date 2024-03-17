tasks = []


def addTask():
    task = input("Please input a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to th list ")

def listTask():
    if not tasks:
        print("There are no available tasks")
    else:
        print("Current task: ")
        for index, task in enumerate(tasks):
            print(f"Task {index} . {task}")

def deleteTask():
    listTask()
    try:
        taskToDelete = int(input("Input number what I should delete:"))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} was successfully removed ")
        else:
            print(f"Task #{taskToDelete} was not found")    
            
    except:
        print("Invalid input")
if __name__== "__main__":
    print("Welcome to the to do list app: ")
    while True: 
        print("\n")
        print("Please choose one from following options: ")
        print("-------------------------------------------")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. View all tasks")
        print("4. Exit")
        print("---------------------------------------------")
        choice = input("Enter your choice: ")
        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif (choice == "3"):
            listTask()
        elif (choice == "4"):
            break
        else:
            print("Not valid input")
            
            
    print("Goodbye (waving)")
        