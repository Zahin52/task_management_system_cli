from datetime import datetime, timedelta
import uuid


class Task:
    #  Added id as a property to uniqly identy task
    #  Added completed_at property to calculate the average task completion time
    def __init__(
        self,
        title,
        description,
        id=None,
        completed=False,
        created_at=None,
        completed_at=None,
    ):
        self.id = str(uuid.uuid4()) if not id else id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now().isoformat() if not created_at else created_at
        self.completed_at = completed_at

    #    Marking task as complete
    def mark_completed(self):
        self.completed = True
        self.completed_at = datetime.now().isoformat()


class TaskManager:

    def __init__(self, storage):
        self.storage = storage

    def add_task(self, title, description):
        # checking if the title is empty or not
        # empty title can not be allowed
        if not title:
            raise ValueError("Task title cannot be empty.")
        task = Task(title, description)
        self.storage.save_task(task)
        return task

    def complete_task(self, task_id):
        task_dict = self.storage.get_task(task_id)
        if task_dict:
            task = Task(**task_dict) if isinstance(task_dict, dict) else task_dict
            task.mark_completed()
            self.storage.update_task(task)
            return True
        return False

    def list_tasks(self, include_completed=False):
        tasks = self.storage.get_all_tasks()
        if not include_completed:
            tasks = [task for task in tasks if not task.completed]
        return tasks

    def generate_report(self):
        tasks = self.storage.get_all_tasks()
        total_tasks = len(tasks)
        completed_tasks = len([task for task in tasks if task.completed])
        pending_tasks = total_tasks - completed_tasks

        # Calculate average time to complete tasks
        total_time = timedelta()
        completed_count = 0

        for task in tasks:
            if task.completed_at:
                created_at = datetime.fromisoformat(task.created_at)
                completed_at = datetime.fromisoformat(task.completed_at)
                total_time += completed_at - created_at
                completed_count += 1

        average_time = total_time / completed_count if completed_count > 0 else "N/A"

        report = {
            "total": total_tasks,
            "completed": completed_tasks,
            "pending": pending_tasks,
            "average_completion_time": (
                str(average_time) if completed_count > 0 else "No completed tasks"
            ),
        }

        return report
