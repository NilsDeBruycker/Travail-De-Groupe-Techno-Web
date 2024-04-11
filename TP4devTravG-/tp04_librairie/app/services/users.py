from app.database import database
from app.schemas import UserSchema

def get_user_by_username(username: str):
    for user in database['users']:
        if user['username'] == username:
            return UserSchema.model_validate(user)
    return None


def get_user_by_email(email: str):
    for user in database['users']:
        if user["email"] == email:
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
            database["users"][i]["blocked"]=True
        i+=1

def unblock_user(email):
    i=0
    for user in database["users"]:
        if  database["users"][i]["email"]== email:
            database["users"][i]["blocked"]=False
        i+=1

def promote_user(email: str) -> UserSchema:
    i=0
    for user in database["users"]:
        if  database["users"][i]["email"]== email:
            database["users"][i]["role"]="admin"
        i+=1

def demote_user(email: str) -> UserSchema:
    i=0
    for user in database["users"]:
        if  database["users"][i]["email"]== email:
            database["users"][i]["role"]="normal"
        i+=1