from load_and_save import save_tasks

def add_task(tasks):
    task = input("Enter the task: ")
    priority = input("Enter priority (High, Medium, Low): ").strip().title()
    tasks.append({"task": task, "priority": priority, "completed": False})
    print(f'Task "{task}" added successfully!')


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("===== Task List =====")
    print("choose filter")
    print("1. All tasks")
    print("2. High priority tasks")
    print("3. Medium priority tasks")
    print("4. Low priority tasks")
    print("5. Completed tasks")
    print("6. Incomplete tasks")
    filter = input("Enter your choice (1-6): ")
    print("===== Tasks =====")
    if filter == "1":
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Incomplete"
            print(f"{index}. {task['task']} - Priority: {task['priority']} - Status: {status}")
    elif filter == "2":
        for index, task in enumerate(tasks, start=1):
            if task["priority"] == "high":
                status = "Completed" if task["completed"] else "Incomplete"
                print(f"{index}. {task['task']} - Priority: {task['priority']} - Status: {status}")
    elif filter == "3":
        for index, task in enumerate(tasks, start=1):
            if task["priority"] == "medium":
                status = "Completed" if task["completed"] else "Incomplete"
                print(f"{index}. {task['task']} - Priority: {task['priority']} - Status: {status}")
    elif filter == "4":
        for index, task in enumerate(tasks, start=1):
            if task["priority"] == "low":
                status = "Completed" if task["completed"] else "Incomplete"
                print(f"{index}. {task['task']} - Priority: {task['priority']} - Status: {status}")
    elif filter == "5":
        for index, task in enumerate(tasks, start=1):
            if task["completed"]:
                print(f"{index}. {task['task']} - Priority: {task['priority']} - Status: Completed")
    elif filter == "6":
        for index, task in enumerate(tasks, start=1):
            if not task["completed"]:
                print(f"{index}. {task['task']} - Priority: {task['priority']} - Status: Incomplete")

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



def edit_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_index = int(input("Enter task number to edit: ")) - 1

        if not 0 <= task_index < len(tasks):
            print("Invalid task number.")
            return

        task = tasks[task_index]

        new_title = input(
            f"New title (press Enter to keep '{task['task']}'): "
        ).strip()

        if new_title:
            task["task"] = new_title

        new_priority = input(
            f"New priority (High/Medium/Low, "
            f"Enter to keep '{task['priority']}'): "
        ).strip().title()

        if new_priority:
            if new_priority not in ["High", "Medium", "Low"]:
                print("Invalid priority. Changes not saved.")
                return
            task["priority"] = new_priority

            save_tasks(tasks)
        print("Task updated successfully!")

    except ValueError:
        print("Please enter a valid task number.")
    