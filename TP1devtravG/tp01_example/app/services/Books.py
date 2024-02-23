from app.schemas import Book
from app.database import database


def save_task(new_task: Book) -> Book:
    database["tasks"].append(new_task)
    return new_task


def get_all_tasks() -> list[Book]:
    tasks_data = database["books"]
    tasks = [Book.model_validate(data) for data in tasks_data]
    return tasks


def get_task_by_id(task_id: str) -> Book | None:
    selected_task = [
        task for task in database["tasks"]
        if task["id"] == task_id
    ]
    if len(selected_task) < 1:
        return None
    selected_task = Book.model_validate(selected_task[0])
    return selected_task
    
