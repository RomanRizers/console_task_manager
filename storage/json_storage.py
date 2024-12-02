import json
from typing import List
from app.task import Task
from storage.storage_strategy import StorageStrategy


class JSONStorage(StorageStrategy):
    """Класс для работы с задачами в формате JSON."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_tasks(self) -> List[Task]:
        """Загружает задачи из JSON-файла."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            raise ValueError("Ошибка чтения JSON-файла.")

    def save_tasks(self, tasks: List[Task], file_path: str = None):
        """Сохраняет задачи в JSON-файл."""
        if file_path is None:
            file_path = self.file_path
        data = [task.to_dict() for task in tasks]
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
