import pytest
from app.task import Task
from app.task_manager import TaskManager
from storage.json_storage import JSONStorage


@pytest.fixture
def task_manager(tmp_path):
    """Фикстура для тестового менеджера задач."""
    test_file = tmp_path / "test_tasks.json"
    storage = JSONStorage(file_path=str(test_file))
    return TaskManager(storage=storage)


def test_add_task(task_manager):
    """Тест добавления новой задачи."""
    task = Task(
        title="Добавление",
        description="Тест",
        category="Тесты",
        due_date="2024-12-31",
        priority="Средний"
    )
    task_manager.add_task(task)
    tasks = task_manager.get_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Добавление"


def test_mark_task_done(task_manager):
    """Тест пометки задачи как выполненной."""
    task = Task(
        title="Изменение статуса",
        description="Статус",
        category="Tесты",
        due_date="2024-12-31",
        priority="Высокий"
    )
    task_manager.add_task(task)
    task_manager.mark_task_done(task.id)
    assert task_manager.get_tasks()[0].status == "Выполнена"


def test_delete_task(task_manager):
    """Тест удаления задачи."""
    task = Task(
        title="Удаление задачи",
        description="Тест на удаление",
        category="Тесты",
        due_date="2024-12-31",
        priority="Низкий"
    )
    task_manager.add_task(task)
    task_manager.delete_task(task.id)
    assert len(task_manager.get_tasks()) == 0
