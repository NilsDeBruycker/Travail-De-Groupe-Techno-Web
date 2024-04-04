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
def promote_user(user_id: str) -> UserSchema:
    user = get_user_by_email(user_id)
    if user['role'] == "normal":
        user['role'] = "admin"
        return user
    else:
        return None #user is an admin already

def demote_user(user_id: str) -> UserSchema:
    user = get_user_by_email(user_id)
    if user['role'] == "admin":
        user['role'] = "normal"
        return user
    else:
        return None #user is normal already