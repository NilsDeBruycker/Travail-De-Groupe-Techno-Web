from uuid import uuid4
from typing import Annotated
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from fastapi.responses import RedirectResponse
from app.schemas import Book
import app.services.Books as service
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, HTTPException, status, Request, Form
from fastapi.staticfiles import StaticFiles


router = APIRouter(prefix="/books", tags=["Books"])
templates = Jinja2Templates(directory="templates")
static= StaticFiles(directory="static")




@router.get('/')
def get_all_Books(request:Request):
    Books = service.get_all_books()
    return templates.TemplateResponse(
        "all_books.html",
        context={'request': request, 'books': Books}
    )

    



@router.get('/new')
def get_book(request: Request):
    return templates.TemplateResponse(
        "new_book.html",
        context={'request': request,}
    )


@router.post('/new')
def create_new_book(name: Annotated[str, Form()], Author: Annotated[str, Form()],Editor: Annotated[str, Form()]):
    new_book_data = {
        "id": str(uuid4()),
        "name": name,
        "Author": Author,
        "Editor":Editor,
    }
    try:
        new_book = Book.model_validate(new_book_data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid name or author or edditor for the book.",
        )
    service.save_book(new_book)
    return RedirectResponse(url="/books/", status_code=302)

@router.get('/modify')
def go_to_modify(request: Request):
    return templates.TemplateResponse(
        "modify_book.html",
        context={'request': request,}
    )

@router.post('/modify')
def modify_book(id : Annotated[str, Form()],name: Annotated[str, Form()], Author: Annotated[str, Form()],Editor: Annotated[str, Form()]):
    if not service.is_book_exist(id):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
                detail=" id not found"
                )
    new_book_data = {
        "id":id,
        "name": name,
        "Author": Author,
        "Editor":Editor,
    }
    try:
        new_book = Book.model_validate(new_book_data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid name or author or edditor or id for the book.",
        )
    if name.isspace() or Author.isspace()or Editor.isspace():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="error one of the field is empty or only contain white space")
    service.modify_book_by_id(id,new_book)
    return RedirectResponse(url="/books/", status_code=302)


@router.post('/delete')
def deletebook(id: Annotated[str, Form()]):
    if not service.is_book_exist(id):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
                detail=" id not found"
        )
    service.delete_book_by_id(id)
    return RedirectResponse(url="/books/", status_code=302)
