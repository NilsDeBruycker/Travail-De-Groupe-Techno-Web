from app.schemas import UserSchema
from sqlalchemy.orm import Session
from app.models.book import User  
from sqlalchemy import select


def get_user_by_username(username: str):
    with Session() as session:
        statement = select(User).filter_by(username=username)
        user = session.scalar(statement) 
        if user is not None:
            return UserSchema(
                username=user.username,
                email=user.email,
                password=user.password,
                role=user.role,
                blocked=user.blocked,
            )
    return None


def get_user_by_email(email: str):
    with Session() as session:
        statement = select(User).filter_by(email=email)
        user = session.scalar(statement) 
        if user is not None:
            return UserSchema(
                email=user.email,
                username=user.username,
                password=user.password,
                user=user.role,
                blocked=user.blocked,
            )
    return None


def sign_up_user(new_user):
    with Session() as session:
       session.add(new_user)
       session.commit()
    return new_user



def get_all_users() :
    with Session() as session:
        statement = select(User)
        users_data = session.scalars(statement).unique().all()
        return [
            User(
                email=user.email,
                password=user.password,
                username=user.username,
                role=user.role,
                blocked=user.blocked,
            )     
            
            for user in users_data
        ]



def block_user(email: str):
    with Session() as session:
        user = session.query(User).filter(User.email == email).first()
        if user is not None:
            user.blocked = True
            session.commit()


def unblock_user(email: str):
    with Session() as session:
        user = session.query(User).filter(User.email == email).first()
        if user is not None:
            user.blocked = False
            session.commit()


def promote_user(email: str) -> User:
    with Session() as session:    
        user = session.query(User).filter(User.email == email).first()
        if user is not None:
            user.role = "admin"
            session.commit()

    return user


def demote_user(email: str) -> User:
    with Session() as session:
        user = session.query(User).filter(User.email == email).first()
        if user:
            user.role = "normal"
            session.commit()

    return user

def delete_user_by_id( user_id: str):
    with Session() as session:
        statement = select(User).filter_by(id=user_id)
        user = session.execute(statement).scalar_one()
        session.delete(user)
        session.commit()
    