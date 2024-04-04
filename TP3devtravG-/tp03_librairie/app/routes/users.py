from typing import Annotated
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi import APIRouter, HTTPException, status, Request, Form, Depends, Body
from app.login_manager import login_manager
from app.services.users import get_user_by_username,sign_up_user
from app.schemas import UserSchema
from pydantic import ValidationError
from fastapi.templating import Jinja2Templates
router = APIRouter(prefix="/users")
templates = Jinja2Templates(directory="templates")
import app.services.users as user_service

@router.get("/login")
def go_tosignup(request:Request):    
    return templates.TemplateResponse(
        "login.html",
        context={'request': request}
    )

@router.post("/login")
def login_route(
        username: Annotated[str, Form()],
        email:Annotated[str, Form()],
        password: Annotated[str, Form()],
):
    user = get_user_by_username(username)
    if user is None or user.password != password:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bad credentials."
        )
    if user.blocked==True:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="blocked."
        )
    access_token = login_manager.create_access_token(
        data={'sub': user.email}
    )
    
    response = RedirectResponse(url="/books/", status_code=302)
    response.set_cookie(
        key=login_manager.cookie_name,
        value=access_token,
        httponly=True
    )
    return response

@router.get("/sign_up")
def go_tosignup(request:Request):    
    return templates.TemplateResponse(
        "signup.html",
        context={'request': request}
    )

@router.post("/sign_up")
def sign_up_route(username: Annotated[str, Form()],email:Annotated[str, Form()],password: Annotated[str, Form()],password2: Annotated[str, Form()]):
    if password==password2:
        new_user = {
            "username": username,
            "email": email,
            "password": password,
            "role":"normal",
            "blocked":False}
        
        try:
            new_user = UserSchema.model_validate(new_user)
        except ValidationError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid name or author or edditor for the book.",
            )
        sign_up_user(new_user)

        return RedirectResponse(url="/books/", status_code=302)
    else:
        return HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="confirmation password is not the same password"
        )

@router.post('/logout')
def logout_route():
    response = JSONResponse({'status': 'success'})
    response.delete_cookie(
        key=login_manager.cookie_name,
        httponly=True
    )
    return response

@router.post("/block")
def go_to_block_page(request:Request,email:Annotated[str, Form()],user: UserSchema = Depends(login_manager),):
    user_service.block_user(email)
    return RedirectResponse(url="/users/", status_code=302)
@router.post("/unblock")
def go_to_block_page(request:Request,email:Annotated[str, Form()],user: UserSchema = Depends(login_manager),):
    user_service.unblock_user(email)
    return RedirectResponse(url="/users/", status_code=302)

@router.get("/me")
def current_user_route(
    user: UserSchema = Depends(login_manager), #depends renvoie ereure si pas conecté
):
    return user

@router.get("/")
def show_all_users(request:Request,user: UserSchema = Depends(login_manager)):
    users = user_service.get_all_users()
    if user.role!="admin":
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="only admins can use this page"
        )
    return templates.TemplateResponse(
        "manage_users.html",
        context={'request': request,'current_user': user ,'users': users}
        )
