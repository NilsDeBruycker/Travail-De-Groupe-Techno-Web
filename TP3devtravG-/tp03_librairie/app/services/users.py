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