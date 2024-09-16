import unittest
from datetime import datetime, timedelta
from unittest.mock import MagicMock
from task_manager import Task, TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.storage = MagicMock()  # Mocking storage to avoid file I/O
        self.manager = TaskManager(self.storage)

    def test_add_task(self):
        task = self.manager.add_task("Test Task", "Description")
        self.storage.save_task.assert_called_once()
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Description")
        self.assertIsNotNone(task.id)  # Ensure the task has a unique ID

    def test_list_tasks_exclude_completed(self):
        tasks = [
            Task("Task 1", "Description 1"),
            Task("Task 2", "Description 2"),
            Task("Task 3", "Description 3")
        ]
        tasks[1].completed = True
        self.storage.get_all_tasks.return_value = tasks
        result = self.manager.list_tasks()
        self.assertEqual(len(result), 2)
        self.assertNotIn(tasks[1], result)

    def test_generate_report(self):
        tasks = [
            Task("Task 1", "Description 1"),
            Task("Task 2", "Description 2"),
            Task("Task 3", "Description 3")
        ]
        tasks[0].completed = True
        tasks[0].completed_at = (datetime.now() - timedelta(days=2)).isoformat()
        tasks[1].completed = True
        tasks[1].completed_at = (datetime.now() - timedelta(days=1)).isoformat()

        self.storage.get_all_tasks.return_value = tasks
        report = self.manager.generate_report()

        self.assertEqual(report["total"], 3)
        self.assertEqual(report["completed"], 2)
        self.assertEqual(report["pending"], 1)
        self.assertNotEqual(report["average_completion_time"], "N/A")

    def test_complete_nonexistent_task(self):
        self.storage.get_task.return_value = None
        result = self.manager.complete_task("non-existent-id")
        self.assertFalse(result)
        
    #  Added some additional test
    def test_complete_task_with_timing(self):
        task = Task("Task 1", "Description")
        self.storage.get_task.return_value = task
        self.manager.complete_task(task.id)
        self.assertTrue(task.completed)
        self.assertIsNotNone(task.completed_at)

    def test_average_completion_time_calculation(self):
        task1 = Task("Task 1", "Description 1")
        task1.completed = True
        task1.completed_at = (datetime.now() - timedelta(hours=5)).isoformat()
        
        task2 = Task("Task 2", "Description 2")
        task2.completed = True
        task2.completed_at = (datetime.now() - timedelta(hours=10)).isoformat()
        
        self.storage.get_all_tasks.return_value = [task1, task2]

        report = self.manager.generate_report()
        self.assertEqual(report["completed"], 2)
        self.assertNotEqual(report["average_completion_time"], "N/A")

    def test_empty_task_list(self):
        self.storage.get_all_tasks.return_value = []
        result = self.manager.list_tasks()
        self.assertEqual(len(result), 0)

    def test_add_task_invalid_data(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("", "Description")


if __name__ == "__main__":
    unittest.main()
