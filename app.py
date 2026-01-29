"""
Simple Task Manager Application
A command-line task management tool
"""

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task_description, priority='medium'):
        """Add a new task to the list"""
        task = {
            'id': len(self.tasks) + 1,
            'description': task_description,
            'priority': priority,
            'completed': False
        }
        self.tasks.append(task)
        return task
    
    def complete_task(self, task_id):
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                return task
        return None
    
    def list_tasks(self, filter_completed=None, filter_priority=None):
        """List all tasks with optional filtering"""
        filtered_tasks = self.tasks
        
        if filter_completed is not None:
            filtered_tasks = [t for t in filtered_tasks if t['completed'] == filter_completed]
        
        if filter_priority:
            filtered_tasks = [t for t in filtered_tasks if t.get('priority', 'medium') == filter_priority]
        
        if not filtered_tasks:
            print("No tasks found.")
            return
        
        for task in filtered_tasks:
            status = "✓" if task['completed'] else "○"
            priority = task.get('priority', 'medium')
            print(f"{status} [{task['id']}] [{priority.upper()}] {task['description']}")
    
    def remove_task(self, task_id):
        """Remove a task from the list"""
        self.tasks = [task for task in self.tasks if task['id'] != task_id]


def main():
    """Main application entry point"""
    manager = TaskManager()
    
    print("Welcome to Task Manager!")
    print("Commands: add, list, complete, remove, exit")
    
    while True:
        command = input("\nEnter command: ").strip().lower()
        
        if command == "exit":
            print("Goodbye!")
            break
        elif command == "add":
            description = input("Enter task description: ")
            priority = input("Enter priority (low/medium/high, default: medium): ").strip().lower() or 'medium'
            if priority not in ['low', 'medium', 'high']:
                priority = 'medium'
            manager.add_task(description, priority)
            print("Task added successfully!")
        elif command == "list":
            filter_type = input("Filter by (completed/incomplete/priority/all, default: all): ").strip().lower() or 'all'
            if filter_type == 'completed':
                manager.list_tasks(filter_completed=True)
            elif filter_type == 'incomplete':
                manager.list_tasks(filter_completed=False)
            elif filter_type == 'priority':
                priority = input("Enter priority (low/medium/high): ").strip().lower()
                manager.list_tasks(filter_priority=priority)
            else:
                manager.list_tasks()
        elif command == "complete":
            try:
                task_id = int(input("Enter task ID: "))
                if manager.complete_task(task_id):
                    print("Task marked as completed!")
                else:
                    print("Task not found!")
            except ValueError:
                print("Invalid task ID!")
        elif command == "remove":
            try:
                task_id = int(input("Enter task ID: "))
                manager.remove_task(task_id)
                print("Task removed successfully!")
            except ValueError:
                print("Invalid task ID!")
        else:
            print("Unknown command. Try: add, list, complete, remove, exit")


if __name__ == "__main__":
    main()

