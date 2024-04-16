from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.schemas import book
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


"""def get_all_books() -> list[Book]:
    with Session() as session:
     statement = select(Book)
     books_data = session.scalars(statement).unique().all()
        return [
            Book(
                id=task.id,
                name=task.name,
                description=task.description,
                creation_date=task.creation_date,
                
            
            for task in tasks_data
        ]"""

def delete_book_by_id(book_id:str):
    with Session as session:
        statement=select(Book).filter_by(id=book_id)
        book=session.execute(statement).scalar_one()
        session.delete(book)
        session.commit()
def is_book_exist(book_id:str):
    i=0
    for book in database["books"]:
        if  database["books"][i]["id"]== book_id:

            return True
        i+=1
    return False

def modify_book_by_id(book_id: str,modified_book) -> Book | None:
    i=0
    for book in database["books"]:
        if  database["books"][i]["id"]== book_id:
            database["books"][i] =modified_book 
        i+=1