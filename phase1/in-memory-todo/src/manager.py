from typing import List, Optional
from models import Task

class TaskManager:
    """Manages the lifecycle of tasks in memory."""
    
    def __init__(self):
        self.tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: str) -> Task:
        """Add a new task to the list."""
        task = Task(id=self._next_id, title=title, description=description)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def view_tasks(self) -> List[Task]:
        """Return the list of all tasks."""
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Retrieve a task by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """Update an existing task's title or description."""
        task = self.get_task_by_id(task_id)
        if task:
            if title:
                task.title = title
            if description:
                task.description = description
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """Remove a task from the list by ID."""
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def toggle_complete(self, task_id: int) -> bool:
        """Toggle the completion status of a task."""
        task = self.get_task_by_id(task_id)
        if task:
            task.is_completed = not task.is_completed
            return True
        return False
