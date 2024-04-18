from uuid import uuid4
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.schemas import books
from app.database import Session
from app.models.book import Book
from app.schemas.books import Book as Bookshemat


def save_book(new_book: Bookshemat):
    with Session() as session:
        new_book_entity = Book(
            id= new_book.id,
            name= new_book.name,
            Prix=new_book.Prix,
            owner_email=new_book.Owner,
            status=new_book.status, 
            Author= new_book.Author ,
            Editor= new_book.Editor,
            )
        session.add(new_book_entity)
        session.commit()

def get_public_book():
    with Session() as session:
     statement = select(Book).filter_by(status="en vente")
     books_data = session.scalars(statement).unique().all()
    return [
        Book(
            id=book.id,
            name=book.name,
            Prix=book.Prix,
            owner=book.owner,
            status=book.status,
            Author=book.Author,
            Edditor=book.Editor,
        )
        
        for book in books_data
    ]

def get_own_books(user):
    with Session() as session:
     statement = select(Book).filter(Book.owner_email==user.email)
     books_data = session.scalars(statement).unique().all()
    return [
        Book(
            id=book.id,
            name=book.name,
            Prix=book.Prix,
            owner=book.owner,
            status=book.status,
            Author=book.Author,
            Edditor=book.Editor,
        )
        
        for book in books_data
    ]

def get_all_books() -> list[Book]:
    with Session() as session:
     statement = select(Book)
     books_data = session.scalars(statement).unique().all()
    return [
        Book(
            id=book.id,
            name=book.name,
            Prix=book.Prix,
            owner=book.owner,
            status=book.status,
            Author=book.Author,
            Edditor=book.Editor,
        )
        
        for book in books_data
    ]

def delete_book_by_id(book_id:str):
    with Session() as session:
        statement=select(Book).filter_by(id=book_id)
        book=session.scalars(statement).one()
        session.delete(book)
        session.commit()

def is_book_exist(book_id:str):
    with Session() as session:
        statement=select(Book).filter_by(id=book_id)
        book=session.scalar(statement)
        if book is not None:
            return True
        else :
            return False

def get_book_by_id(book_id):
     with Session() as session:
        statement=select(Book).filter_by(id=book_id)
        book=session.scalars(statement).one()
        return Book(
            id=book.id,
            name=book.name,
            Prix=book.Prix,
            owner=book.owner,
            status=book.status,
            Author=book.Author,
            Edditor=book.Editor,
        )

def modify_book_by_id(book_id: str,modified_book) -> Book | None:
    with Session() as session:
        statement=select(Book).filter_by(id=book_id)
        book=session.scalars(statement).one()
        book.owner_email=modified_book["Owner"]
        book.name=modified_book["name"]
        book.status=modified_book["status"]
        book.Prix=modified_book["prix"]
        book.Author=modified_book["Author"],
        book.Editor=modified_book["Edditor"]
        session.commit()