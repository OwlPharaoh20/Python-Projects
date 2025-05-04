#Load existing items
#1. Create a new item
#2. List items
#3. mark item as complete
#4. save items


import json

file_name = "todo_list.json"


#Load items
def load_tasks():
     try:
         with open(file_name, "r") as file:
              return json.load(file)
     except:
       return {"tasks": []}


#Save items
def save_tasks(tasks):
    try:
         with open(file_name, "w") as file:
              return json.dump(tasks, file)
    except:
       return {"tasks": []}


    
    

#View all tasks
def view_tasks(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks found.")

    else:
        print("Your To-do list:")
        for idx, task in enumerate(task_list):
            status = "[completed]" if task.get("complete", False) else "[pending]"
            print(f"{idx + 1}. {task['description']} | {status}")


    
     



#Create a new task
def create_task(tasks):
    description = input("Enter task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False}) 
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task description cannot be empty.")



#Mark task as complete
def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks):
              tasks["tasks"][task_number -1]["complete"] = True
              save_tasks(tasks)
              print("Task marked as complete!")
        else:
             print("Invalid task Number.")
    except:
        print("Enter a valid number.")

    
     


#Main function 
def main():

    save_tasks({"tasks": [{"description": "saved task", "complete": False}]})
    tasks = load_tasks() 
    print(tasks)


    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Goodbye")
            break
        else: 
            print("Invalid choice. Please try again.")


main()