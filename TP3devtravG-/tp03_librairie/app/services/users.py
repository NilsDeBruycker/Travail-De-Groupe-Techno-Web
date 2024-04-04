from fastapi import Depends, HTTPException, Request
from app import login_manager
from app.database import database
from app.schemas import UserSchema

def get_user_by_username(username: str):
    for user in database['users']:
        if user['username'] == username:
            return UserSchema.model_validate(user)
    return None


def get_user_by_email(id: str):
    for user in database['users']:
        if user['email'] == id:
            return UserSchema.model_validate(user)
    return None

def sign_up_user(new_user):
    database["users"].append(new_user)
    return new_user

def get_all_users() -> list[UserSchema]:
    user_data = database["users"]
    books = [UserSchema.model_validate(user) for user in user_data]
    
    return books

def block_user(email):
    i=0
    for user in database["users"]:
        if  database["users"][i]["email"]== email:
            database["users"][i]["blocked"]==True

def unblock_user(email):
    i=0
    for user in database["users"]:
        if  database["users"][i]["email"]== email:
            database["users"][i]["blocked"]==False
