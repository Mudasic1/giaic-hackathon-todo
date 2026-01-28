from dataclasses import dataclass

@dataclass
class Task:
    """Task model for the Todo application."""
    id: int
    title: str
    description: str
    is_completed: bool = False
