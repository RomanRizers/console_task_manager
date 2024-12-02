from typing import List
from app.task import Task


class StorageStrategy:
    """Интерфейс стратегии хранения задач."""

    def load_tasks(self) -> List[Task]:
        """Загружает задачи из хранилища."""
        raise NotImplementedError("Метод load_tasks() должен быть реализован в подклассе.")

    def save_tasks(self, tasks: List[Task], file_path: str = None):
        """Сохраняет задачи в хранилище."""
        raise NotImplementedError("Метод save_tasks() должен быть реализован в подклассе.")
