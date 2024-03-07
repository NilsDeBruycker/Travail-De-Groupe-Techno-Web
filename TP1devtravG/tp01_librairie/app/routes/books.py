from uuid import uuid4

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.schemas import Book
import app.services.Books as service


router = APIRouter(prefix="/books", tags=["Books"])


@router.get('/')
def get_all_Books():
    Books = service.get_all_books()

    return JSONResponse({
        'books': [book.model_dump() for book in Books],
        'nb_books': len(Books)
    })
    



@router.get('/{task_id}')
def get_book(book_id: str):
    book = service.get_book_by_id(book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No book found with this ID.",
        )
    return JSONResponse(book.model_dump())


@router.post('/')
def create_new_book(name: str, Author: str,edditor: str):
    new_book_data = {
        "id": str(uuid4()),
        "name": name,
        "Author": Author,
        "Editor":edditor,
    }
    try:
        new_book = Book.model_validate(new_book_data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid name or description for the task.",
        )
    if name.isspace() or Author.isspace()or edditor.isspace():
        return JSONResponse("error one of the field is empty or only contain white space")
    service.save_book(new_book)
    return JSONResponse(new_book.model_dump())

@router.post('/modify')
def modify_book(id :str,name: str, Author: str,edditor: str):
    new_book_data = {
        "id": id,
        "name": name,
        "Author": Author,
        "Editor":edditor,
    }
    try:
        new_book = Book.model_validate(new_book_data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid name or author or edditor or id for the book.",
        )
    if name.isspace() or Author.isspace()or edditor.isspace():
        return JSONResponse("error one of the field is empty or only contain white space")
    service.modify_book_by_id(id,new_book)
    return JSONResponse(new_book.model_dump(), status_code=200)


@router.delete('/delete{task_id}')
def delete_book(delete_id:str):
    if not service.is_book_exist(delete_id):
        return JSONResponse(
            status_code=404,
            content={"message": "Book not found."}
        )

    service.delete_book_by_id(delete_id)

    return JSONResponse(
        status_code=200,
        content={"message": "Book deleted successfully."}
    )
