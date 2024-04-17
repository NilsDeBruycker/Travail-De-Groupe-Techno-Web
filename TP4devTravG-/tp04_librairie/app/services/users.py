from app.database import database
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
                id=user.id,
                username=user.username,
                password=user.password,
            )
    return None


def get_user_by_email(email: str):
    with Session() as session:
        statement = select(User).filter_by(email=email)
        user = session.scalar(statement) 
        if user is not None:
            return UserSchema(
                id=user.id,
                email=user.email,
                password=user.password,
            )
    return None


def sign_up_user(new_user):
    with Session() as session:
       session.add(new_user)
       session.commit()
    return new_user



def get_all_users(session: Session) :
    users = session.query(User).all()

    return users



def block_user(session: Session, email: str):
    user = session.query(User).filter(User.email == email).first()
    if user:
        user.blocked = True
        session.commit()


def ublock_user(session: Session, email: str):
    user = session.query(User).filter(User.email == email).first()
    if user:
        user.blocked = False
        session.commit()


def promote_user(session: Session, email: str) -> User:
    user = session.query(User).filter(User.email == email).first()
    if user:
        user.role = "admin"
        session.commit()

    return user


def demote_user(session: Session, email: str) -> User:
    user = session.query(User).filter(User.email == email).first()
    if user:
        user.role = "normal"
        session.commit()

    return user

def delete_user_by_id( user_id: str):
    with Session as session:
        statement = select(User).filter_by(id=user_id)
        user = session.execute(statement).scalar_one()
        session.delete(user)
        session.commit()
    