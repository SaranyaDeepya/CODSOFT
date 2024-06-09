from todo import TodoList

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.list_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_index, new_task)
        elif choice == '4':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            todo_list.mark_done(task_index)
        elif choice == '5':
            task_index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
