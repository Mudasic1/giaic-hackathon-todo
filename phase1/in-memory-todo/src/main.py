import sys
from manager import TaskManager

def display_menu():
    print("\n--- TODO CLI (Phase 1) ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Toggle Complete")
    print("5. Delete Task")
    print("6. Exit")

def main():
    manager = TaskManager()
    
    while True:
        display_menu()
        choice = input("Enter choice: ").strip()
        
        if choice == '1':
            title = input("Enter title: ").strip()
            description = input("Enter description: ").strip()
            task = manager.add_task(title, description)
            print(f"Task added with ID: {task.id}")
            
        elif choice == '2':
            tasks = manager.view_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                print("\n--- Tasks ---")
                for t in tasks:
                    status = "Completed" if t.is_completed else "Pending"
                    print(f"ID: {t.id} | Title: {t.title} | Status: {status}")
                    print(f"   Description: {t.description}")
                    
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to update: "))
                title = input("Enter new title (leave blank to keep current): ").strip()
                description = input("Enter new description (leave blank to keep current): ").strip()
                
                if manager.update_task(task_id, title if title else None, description if description else None):
                    print("Task updated successfully.")
                else:
                    print(f"Error: Task with ID {task_id} not found.")
            except ValueError:
                print("Error: Invalid ID format. Please enter a number.")
                
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to toggle: "))
                if manager.toggle_complete(task_id):
                    print("Status toggled successfully.")
                else:
                    print(f"Error: Task with ID {task_id} not found.")
            except ValueError:
                print("Error: Invalid ID format. Please enter a number.")
                
        elif choice == '5':
            try:
                task_id = int(input("Enter task ID to delete: "))
                if manager.delete_task(task_id):
                    print("Task deleted successfully.")
                else:
                    print(f"Error: Task with ID {task_id} not found.")
            except ValueError:
                print("Error: Invalid ID format. Please enter a number.")
                
        elif choice == '6':
            print("Exiting. Goodbye!")
            sys.exit(0)
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
