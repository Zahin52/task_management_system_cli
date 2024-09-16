import json
import os
from task_manager import Task
class Storage:

    def __init__(self):
        self.filepath = "tasks.json"
        self.tasks = self._load_task()

    def _load_task(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as file:
                    list_of_tasks = [Task(**task) for task in json.load(file)]
                    return list_of_tasks
            except json.JSONDecodeError:
                return []
        return []
    
    def _save_tasks(self):
        with open(self.filepath, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file, indent=4)
    
    def save_task(self, task):
        print(task)
        self.tasks.append(task)
        self._save_tasks()

    def update_task(self, updated_task):
        for i, task in enumerate(self.tasks):
            if task.id == updated_task.id:  # Use ID for task identification
                self.tasks[i] = updated_task
                break
        self._save_tasks() # Updating the local DB (json file)

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self):
        return self.tasks

    def clear_all_tasks(self):
        self.tasks = []
