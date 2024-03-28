from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends, Body
from fastapi.responses import JSONResponse

from my_app.login_manager import login_manager
from my_app.services.users import get_user_by_username
from my_app.schemas import UserSchema


router = APIRouter(prefix="/users")


@router.post("/login")
def login_route(
        username: Annotated[str, Body()],
        password: Annotated[str, Body()],
):
    user = get_user_by_username(username)
    if user is None or user.password != password:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bad credentials."
        )
    access_token = login_manager.create_access_token(
        data={'sub': user.id}
    )
    
    response = JSONResponse({"status": "success"})
    response.set_cookie(
        key=login_manager.cookie_name,
        value=access_token,
        httponly=True
    )
    return response





@router.post('/logout')
def logout_route():
    response = JSONResponse({'status': 'success'})
    response.delete_cookie(
        key=login_manager.cookie_name,
        httponly=True
    )
    return response


@router.get("/me")
def current_user_route(
    user: UserSchema = Depends(login_manager), #depends renvoie ereure si pas conecté
):
    return user
