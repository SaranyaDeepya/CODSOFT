import json

class TodoList:
    def __init__(self, storage_file='storage.json'):
        self.storage_file = storage_file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()

    def list_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "Done" if task['done'] else "Not Done"
            print(f"{index}. {task['task']} - {status}")

    def update_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['task'] = new_task
            self.save_tasks()
        else:
            print("Task not found.")

    def mark_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['done'] = True
            self.save_tasks()
        else:
            print("Task not found.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()
        else:
            print("Task not found.")
