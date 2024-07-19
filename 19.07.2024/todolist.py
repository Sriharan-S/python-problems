def view_tasks(file_path):
    """View all tasks in the todo list."""
    try:
        with open(file_path, 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("Todo List:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task.strip()}")
            else:
                print("The todo list is empty.")
    except FileNotFoundError:
        print("No todo list file found. Please add some tasks first.")

def add_task(file_path, task):
    """Add a new task to the todo list."""
    with open(file_path, 'a') as file:
        file.write(task + '\n')
    print(f"Task added: {task}")

def delete_task(file_path, task_number):
    """Delete a task from the todo list."""
    try:
        with open(file_path, 'r') as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1).strip()
            with open(file_path, 'w') as file:
                file.writelines(tasks)
            print(f"Task deleted: {deleted_task}")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No todo list file found. Please add some tasks first.")

def todo_list_manager():
    file_path = 'todo_list.txt'
    
    while True:
        print("\nTodo List Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            view_tasks(file_path)
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(file_path, task)
        elif choice == '3':
            view_tasks(file_path)
            task_number = int(input("Enter the number of the task to delete: "))
            delete_task(file_path, task_number)
        elif choice == '4':
            print("Exiting the todo list manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

todo_list_manager()
