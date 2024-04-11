from uuid import uuid4
from typing import Annotated
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from fastapi.responses import RedirectResponse
from app.schemas import Book
import app.services.Books as service
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, HTTPException, status, Request, Form, Depends, Body
from fastapi.staticfiles import StaticFiles
from app.login_manager import login_manager
from app.services.users import get_user_by_username
from app.schemas import UserSchema
from typing import Optional
router = APIRouter(prefix="/books", tags=["Books"])
templates = Jinja2Templates(directory="templates")
static= StaticFiles(directory="static")




@router.get('/')
def get_all_Books(request:Request,user: UserSchema = Depends(login_manager.optional)):
    Books = service.get_all_books()
    return templates.TemplateResponse(
        "all_books.html",
        context={'request': request,'current_user': user ,'books': Books}
        )

    



@router.get('/new')
def get_book(request: Request, user: UserSchema = Depends(login_manager.optional)):
    login_manager
    if user==None:
        return templates.TemplateResponse(
        "login.html",
        context={'request': request,}
    )
    elif user.blocked==True:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="blocked."
        )
    elif user.role!="admin":
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="only admins can use this page"
        )
    return templates.TemplateResponse(
        "new_book.html",
        context={'request': request,}
    )


@router.post('/new')
def create_new_book(name: Annotated[str, Form()], Author: Annotated[str, Form()],Editor:Annotated[str, Form()]='none'):
    new_book_data = {
        "id": str(uuid4()),
        "name": name,
        "Author": Author,
        "Editor":Editor,
    }
    try:
        new_book_test = Book.model_validate(new_book_data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid name or author or edditor for the book.",
        )
    service.save_book(new_book_data)
    return RedirectResponse(url="/books/", status_code=302)

@router.get('/modify')
def go_to_modify(request: Request, user: UserSchema = Depends(login_manager.optional)):
    if user is None:
        return templates.TemplateResponse(
        "login.html",
        context={'request': request,}
    ) #depends renvoie a login si pas conecté
    elif user.blocked==True:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="blocked."
        )
    elif user.role!="admin":
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="only admins can use this page"
        )
    return templates.TemplateResponse(
        "modify_book.html",
        context={'request': request,}
    )

@router.post('/modify')
def modify_book(id : Annotated[str, Form()],name: Annotated[str, Form()], Author: Annotated[str, Form()],Editor: Annotated[str, Form()]="none"):
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
        new_book_test = Book.model_validate(new_book_data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid name or author or edditor or id for the book.",
        )
    if name.isspace() or Author.isspace()or Editor.isspace():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="error one of the field is empty or only contain white space")
    service.modify_book_by_id(id,new_book_data)
    return RedirectResponse(url="/books/", status_code=302)


@router.post('/delete')
def deletebook(id: Annotated[str, Form()], user: UserSchema = Depends(login_manager.optional)):
    if user is None:
        return templates.TemplateResponse(
        "login.html"
    )
    elif user.blocked==True:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="blocked."
        )
    elif user.role!="admin":
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="only admins can use this page"
        )
   
    if not service.is_book_exist(id):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
                detail=" id not found"
        )
    service.delete_book_by_id(id)
    return RedirectResponse(url="/books/", status_code=302)
