from app.task_manager import TaskManager
from storage.json_storage import JSONStorage
from app.task import Task


def print_table(headers, rows):
    """Функция для табличного вывода."""
    col_widths = [
        max(len(str(header)), max(len(str(row[i])) for row in rows))
        for i, header in enumerate(headers)
    ]
    header_row = " | ".join(
        f"{header:<{col_widths[i]}}" for i, header in enumerate(headers)
    )
    print(header_row)
    print("-" * (sum(col_widths) + len(col_widths) * 3 - 2))

    for row in rows:
        print(" | ".join(
            f"{str(cell):<{col_widths[i]}}" for i, cell in enumerate(row)
        ))


def view_tasks(manager):
    """Просмотр задач."""
    tasks = manager.get_tasks()
    if not tasks:
        print("Задачи отсутствуют.")
    else:
        headers = ["ID", "Title", "Description", "Category", "Due Date", "Priority", "Status"]
        rows = [
            [
                task.id, task.title, task.description, task.category,
                task.due_date, task.priority,
                "Выполнена" if task.status == "Выполнена" else "Не выполнена"
            ] for task in tasks
        ]
        print_table(headers, rows)


def add_task(manager):
    """Добавление новой задачи."""
    title = input("Введите заголовок: ")
    description = input("Введите описание: ")
    category = input("Введите категорию: ")
    due_date = input("Введите дату (YYYY-MM-DD): ")
    priority = input("Введите приоритет: ")
    try:
        task = Task(title, description, category, due_date, priority)
        manager.add_task(task)
        print("Задача успешно добавлена.")
    except ValueError as e:
        print(f"Ошибка: {e}")


def mark_task_done(manager):
    """Отметить задачу как выполненную."""
    try:
        task_id = int(input("Введите ID задачи: "))
        manager.mark_task_done(task_id)
        print("Задача отмечена как выполненная.")
    except ValueError:
        print("ID задачи должен быть числом.")


def delete_task(manager):
    """Удаление задачи."""
    try:
        task_id = int(input("Введите ID задачи: "))
        manager.delete_task(task_id)
        print("Задача успешно удалена.")
    except ValueError:
        print("ID задачи должен быть числом.")


def find_tasks(manager):
    """Поиск задач."""
    keyword = input("Введите ключевое слово для поиска: ")
    found_tasks = manager.find_tasks(keyword)
    if not found_tasks:
        print("Задачи по вашему запросу не найдены.")
    else:
        headers = ["ID", "Title", "Description", "Category", "Due Date", "Priority", "Status"]
        rows = [
            [
                task.id, task.title, task.description, task.category,
                task.due_date, task.priority,
                "Done" if task.done else "Pending"
            ] for task in found_tasks
        ]
        print_table(headers, rows)


def import_tasks(manager):
    """Импорт задач из файла."""
    filename = input("Введите имя файла для импорта (включая расширение): ")
    try:
        manager.import_tasks(filename)
        print(f"Задачи успешно импортированы из файла '{filename}'.")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден в папке data.")
    except Exception as e:
        print(f"Ошибка при импорте задач: {e}")


def export_tasks(manager):
    """Экспорт задач в файл."""
    filename = input("Введите имя файла для экспорта (включая расширение): ")
    try:
        manager.export_tasks(filename)
        print(f"Задачи успешно экспортированы в файл '{filename}'.")
    except Exception as e:
        print(f"Ошибка при экспорте задач: {e}")


def main():
    """Главная функция программы."""
    storage = JSONStorage("data/tasks.json")
    manager = TaskManager(storage)

    menu = {
        1: ("Просмотреть задачи", lambda: view_tasks(manager)),
        2: ("Добавить задачу", lambda: add_task(manager)),
        3: ("Отметить задачу выполненной", lambda: mark_task_done(manager)),
        4: ("Удалить задачу", lambda: delete_task(manager)),
        5: ("Поиск задач", lambda: find_tasks(manager)),
        6: ("Импорт задач из пользовательского файла", lambda: import_tasks(manager)),
        7: ("Экспорт задач в пользовательский файл", lambda: export_tasks(manager)),
        8: ("Выйти", lambda: exit())
    }

    while True:
        print("\n" + "=" * 40)
        print("Меню:")
        for key, (label, _) in menu.items():
            print(f"{key}. {label}")
        print("=" * 40)

        try:
            choice = int(input("Выберите действие: "))
            if choice in menu:
                menu[choice][1]()
            else:
                print("Некорректный выбор. Попробуйте снова.")
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
