import json

file_name = "tasks.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: tasks.json contains invalid JSON.")
        return []


def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file)