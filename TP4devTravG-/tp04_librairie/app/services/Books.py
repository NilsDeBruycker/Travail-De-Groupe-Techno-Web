from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.schemas import books
from app.database import Session
from app.models.book import Book


def save_book(new_book: Book) -> Book:
    with Session() as session:
        new_book_entity = Book(
            id= str,
            name= new_book.name, 
            Author= new_book.Author ,
            Editor= new_book.Editor)
        session.add(new_book_entity)
        session.commit()


def get_all_books() -> list[Book]:
    with Session() as session:
     statement = select(Book)
     books_data = session.scalars(statement).unique().all()
    return [
        Book(
            id=book.id,
            name=book.name,
            prix=book.prix,
            owner=book.owner,
            status=book.status,
        )
        
        for book in books_data
    ]

def delete_book_by_id(book_id:str):
    with Session() as session:
        statement=select(Book).filter_by(id=book_id)
        book=session.execute(statement).scalar_one()
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

def modify_book_by_id(book_id: str,modified_book) -> Book | None:
    with Session() as session:
        statement=select(Book).filter_by(id=book_id)
        book=session.scalars(statement).one()
        book.owner_email=modified_book["Owner"]
        book.name=modified_book["name"]
        book.Prix=modified_book["prix"]
        session.commit()