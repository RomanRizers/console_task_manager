import pytest
from app.task import Task


def test_task_creation():
    """Тест создания задачи."""
    task = Task(
        title="Тест",
        description="Тест",
        category="Тесты",
        due_date="2024-12-31",
        priority="Высокий"
    )
    assert task.title == "Тест"
    assert task.description == "Тест"
    assert task.category == "Тесты"
    assert task.due_date == "2024-12-31"
    assert task.priority == "Высокий"
    assert task.status == "Не выполнена"


def test_task_invalid_date():
    """Тест валидации неверной даты."""
    with pytest.raises(ValueError):
        Task(
            title="Invalid Date Task",
            description="Проверка на ввод даты",
            category="Тесты",
            due_date="31-12-2024",
            priority="Низкий"
        )


def test_task_mark_as_done():
    """Тест изменения статуса задачи на 'Выполнена'."""
    task = Task(
        title="Проверка на статус",
        description="Тест статуса",
        category="Тесты",
        due_date="2024-12-31",
        priority="Высокий"
    )
    task.mark_as_done()
    assert task.status == "Выполнена"
