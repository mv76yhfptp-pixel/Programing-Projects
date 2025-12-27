#This project is going to be about a to-do list
#its going to be able to add and remove tasks 

from Data import load_tasks, save_tasks


data = load_tasks()

if not data:
    save_tasks(data)

print("1. Add Task\n2. View tasks\n3.Remove task\n4. Quit")

while True:
    choice = input("Choose an option: ")
    # Handle choices here

    if choice == "1":
        task = input("Enter new task: ")
        data.append(task)
        save_tasks(data)
        

    elif choice == "2":

        if not data:
            print("No Tasks Found.\n")
        else:
            for i, task in enumerate(data, start=1):
                print(f"{i}. {task}")
    elif choice == "3":
        if not data:
            print("No tasks to remove.\n")
        else:
            for i, task in enumerate(data, 1):
                print(f"{i}. {task}")
            try:   
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(data):
                    removed_task = data.pop(num - 1)
                    save_tasks(data)  # Save updated list
                    print(f"Task '{removed_task}' removed!")
                else:
                    print("Invalid task number.\n")
            except ValueError:
                print("Please enter a valid number.\n")

    elif choice == "4":
        print("Quiting")
        break
