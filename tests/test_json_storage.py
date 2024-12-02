import pytest
import os
from storage.json_storage import JSONStorage
from app.task import Task


@pytest.fixture
def json_storage(tmp_path):
    """Фикстура для тестового JSON-хранилища."""
    test_file = tmp_path / "test_tasks.json"
    return JSONStorage(file_path=str(test_file))


def test_save_and_load_tasks(json_storage):
    """Тест сохранения и загрузки задач."""
    task = Task(
        title="Сохранение и загрузка",
        description="Тест",
        category="Тесты",
        due_date="2024-12-31",
        priority="Выcоский"
    )
    json_storage.save_tasks([task])
    loaded_tasks = json_storage.load_tasks()
    assert len(loaded_tasks) == 1
    assert loaded_tasks[0].title == "Сохранение и загрузка"


def test_load_tasks_from_nonexistent_file(json_storage):
    """Тест загрузки из несуществующего файла."""
    assert os.path.exists(json_storage.file_path) is False
    tasks = json_storage.load_tasks()
    assert tasks == []
