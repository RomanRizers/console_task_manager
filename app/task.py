from datetime import datetime
from typing import Optional


class Task:
    """Базовый класс создания задач."""
    def __init__(
        self,
        title: str,
        description: str,
        category: str,
        due_date: str,
        priority: str,
        status: str = "Не выполнена",
        task_id: Optional[int] = None,
    ):
        self.id = task_id if task_id is not None else 1
        self.title = title
        self.description = description
        self.category = category
        self.due_date = self.validate_date(due_date)
        self.priority = priority
        self.status = status

    @staticmethod
    def validate_date(date_str: str) -> str:
        """Валидация даты."""
        if not date_str:
            raise ValueError("Срок выполнения не может быть пустым.")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            raise ValueError("Неверный формат даты. Используйте YYYY-MM-DD.")

    def mark_as_done(self):
        """Помечает задачу как выполненную."""
        self.status = "Выполнена"

    def to_dict(self) -> dict:
        """Преобразует задачу в словарь для сохранения в JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Создает задачу из словаря."""
        return cls(
            task_id=int(data.get("id")),
            title=data["title"],
            description=data["description"],
            category=data["category"],
            due_date=data["due_date"],
            priority=data["priority"],
            status=data["status"],
        )
