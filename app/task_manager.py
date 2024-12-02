import os
from typing import List, Optional
from app.task import Task
from storage.json_storage import JSONStorage


class TaskManager:
    """Менеджер задач, управляющий задачами."""
    def __init__(self, storage: JSONStorage, data_folder: str = "data"):
        self.storage = storage
        self.tasks: List[Task] = []
        self.data_folder = data_folder

    def _get_file_path(self, filename: str) -> str:
        """Возвращает полный путь к файлу внутри папки data."""
        return os.path.join(self.data_folder, filename)

    def import_tasks(self, filename: str):
        """Импортирует задачи из пользовательского файла."""
        file_path = self._get_file_path(filename)
        self.storage.file_path = file_path
        self.tasks = self.storage.load_tasks()

    def export_tasks(self, filename: str):
        """Экспортирует текущие задачи в пользовательский файл."""
        file_path = self._get_file_path(filename)
        self.storage.save_tasks(self.tasks, file_path)

    def generate_id(self) -> int:
        """Генерирует новый уникальный числовой ID для задачи."""
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def add_task(self, task: Task):
        """Добавляет новую задачу и присваивает ей уникальный ID."""
        task.id = self.generate_id()
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)

    def get_tasks(self, category: Optional[str] = None) -> List[Task]:
        """Возвращает список задач, фильтруя по категории, если указана."""
        if category:
            return [task for task in self.tasks if task.category == category]
        return self.tasks

    def find_tasks(self, keyword: str) -> List[Task]:
        """Ищет задачи по ключевым словам в названии или описании."""
        return [
            task
            for task in self.tasks
            if keyword.lower() in task.title.lower()
            or keyword.lower() in task.description.lower()
        ]

    def delete_task(self, task_id: int):
        """Удаляет задачу."""
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.storage.save_tasks(self.tasks)

    def mark_task_done(self, task_id: int):
        """Помечает задачу выполненной."""
        for task in self.tasks:
            if task.id == task_id:
                task.mark_as_done()
                self.storage.save_tasks(self.tasks)
                return
        return
