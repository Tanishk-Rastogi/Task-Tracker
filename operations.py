def add_task(tasks):
    task = input("Enter the task: ")
    priority = input("Enter the priority (High, Medium, Low): ")
    tasks.append({"task": task, "priority": priority, "completed": False})
    print(f'Task "{task}" added successfully!')


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("===== Tasks =====")
    for priority in ["high", "medium", "low"]:
        for index, task in enumerate(tasks, start=1):
            if task["priority"] == priority:
                status = "Completed" if task["completed"] else "Incomplete"
                print(f"{index}. {task['task']} - "f"Priority: {priority} - Status: {status}")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to mark as complete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print(f'Task "{tasks[task_index]["task"]}" marked as complete!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f'Task "{deleted_task["task"]}" deleted successfully!')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
