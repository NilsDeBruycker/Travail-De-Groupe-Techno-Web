from app.schemas import Book
from app.database import database


def save_book(new_book: Book) -> Book:
    database["books"].append(new_book)
    return new_book


def get_all_books() -> list[Book]:
    books_data = database["books"]
    books = [Book.model_validate(data) for data in books_data]
    
    return books


def get_book_by_id(book_id: str) -> Book | None:
    selected_book = [
        book for book in database["books"]
        if book["id"] == book_id
    ]
    if len(selected_book) < 1:
        return None
    selected_book = Book.model_validate(selected_book[0])
    return selected_book
    
def delete_book_by_id(book_id:str):
    i=0
    for book in database["books"]:
        if  database["books"][i]["id"]== book_id:
            del database["books"][i]
        i+=1

def modify_book_by_id(book_id: str,modified_book) -> Book | None:
    i=0
    for book in database["books"]:
        if  database["books"][i]["id"]== book_id:
            database["books"][i] =modified_book 
        i+=1