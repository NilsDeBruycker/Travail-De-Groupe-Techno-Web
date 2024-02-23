from uuid import uuid4

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.schemas import books
import app.services.Books as service


router = APIRouter(prefix="/books", tags=["Tasks"])


@router.get('/')
def get_all_tasks():
    tasks = service.get_all_tasks()
    return JSONResponse(
        content=[task.model_dump() for task in tasks],
        status_code=200,
    )


@router.get('/{task_id}')
def get_task(task_id: str):
    task = service.get_task_by_id(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No task found with this ID.",
        )
    return JSONResponse(task.model_dump())


@router.post('/')
def create_new_task(name: str, description: str):
    new_task_data = {
        "id": str(uuid4()),
        "name": name,
        "description": description,
    }
    try:
        new_task = books.model_validate(new_task_data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid name or description for the task.",
        )
    service.save_task(new_task)
    return JSONResponse(new_task.model_dump())
